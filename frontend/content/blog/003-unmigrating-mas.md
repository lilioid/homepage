---
num: 3
title: Un-Migrating users from MAS
author: lilly
short_desc: >
  A guide on how to un-migrate user accounts and sessions from Matrix-Authentication-Service
lang: en
tags: [ tech ]
created_at: "2025-01-10 17:00:00+02"
draft: false
---

The [Matrix Messaging System](https://matrix.org/) is currently in the process of developing and deploying a new authentication layer called [Matrix-Authentication-Service](https://github.com/element-hq/matrix-authentication-service) ([announcement](https://matrix.org/blog/2023/09/matrix-2-0/#native-open-id-connect)).
MAS aims to unify all authentication which a homeserver and client application need to implement to be OpenID-Connect by being the OpenID-Connect provider that is authenticated against.
However, MAS is still in development and does not yet support some authentication related features (namely [Application Services Login](https://element-hq.github.io/matrix-authentication-service/as-login.html)[^1]).

## The premise

At the University of Hamburg's student body, we offer hosted matrix services for around 600 users.
Because MAS seems to be the future, we of course wanted to migrate.
Thankfully, the MAS project even provides a handy [migration guide](https://element-hq.github.io/matrix-authentication-service/setup/migration.html). Nice!<br>
Unfortunately for us, we only realized that Application Services Login is not supported after doing the migration. Not so nice :(<br>
So, naturally, we reverted the change and even existing sessions just kept working. Let's forget about this affair and keep running on the old setup. Everyone was happy.

After some weeks passed (and all precautionary DB snapshots were now outdated) though, we noticed that when logging into our homeserver, a user would not be logged into their existing account, but that a new account would be created instead.
The issue was traced to our earlier *Synapse to MAS* migration, which not only transferred existing user sessions to MAS but also replaced all references to the user IDs provided by our upstream OIDC provider with ones associated to MAS users.
Here's a small diagram, illustrating which user IDs existed at this point and who had authority over them:

```text
┌────────────────────────┐
│ Upstream OIDC Provider │
└─────────┬──────────────┘
          │ provides an upstream user id
          │
          ↓
┌───────────────────────────────────┐
│ MAS (has an internal id per user) │
└─────────┬─────────────────────────┘
          │ provides a user id derived (at runtime) from MAS user id
          │
          ↓
┌──────────────────────────────────────────────────┐
│ Synapse Homeserver (has an internal id per user) │
└──────────────────────────────────────────────────┘
```

The issue is that now, when MAS is disabled and a user tries to log into their account, synapse does not recognize the upstream OIDC provider's user ID and provisions a new account.

## Data Layout of MAS and Synapse

Synapse and MAS each store their data in a database.
In our case, this was a postgresql database server with one database per application.

The following tables are relevant to user-mapping and un-migrating:

- For synapse, the `user_external_ids` table holds the association between synapse accounts and upstream user IDs.
  The important columns here are `external_id` for the user ID provided by an upstream provider (`sub` claim of the access token) and `user_id` which contains the matrix user ID in the form `@alice:example.com`.

```text
          Table "public.user_external_ids"
   Column     | Type | Collation | Nullable | Default
---------------+------+-----------+----------+---------
auth_provider | text |           | not null |
external_id   | text |           | not null |
user_id       | text |           | not null |
```

- For MAS, the `upstream_oauth_links` table holds external user IDs and links them to internal ones.
  Additionally, the `users` table contains the central user object and notably includes a username.
  So where synapse would know `@alice:example.com`, MAS stores `alice` in its `users` table.

```text
                          Table "public.upstream_oauth_links"
           Column           |           Type           | Collation | Nullable | Default
----------------------------+--------------------------+-----------+----------+---------
 upstream_oauth_link_id     | uuid                     |           | not null |
 upstream_oauth_provider_id | uuid                     |           | not null |
 user_id                    | uuid                     |           |          |
 subject                    | text                     |           | not null |
 created_at                 | timestamp with time zone |           | not null |
```

```text
                               Table "public.users"
        Column         |           Type           | Collation | Nullable | Default
-----------------------+--------------------------+-----------+----------+---------
 user_id               | uuid                     |           | not null |
 username              | text                     |           | not null |
 created_at            | timestamp with time zone |           | not null |
 primary_user_email_id | uuid                     |           |          |
 locked_at             | timestamp with time zone |           |          |
 can_request_admin     | boolean                  |           | not null | false
```


## Un-Migrating User Accounts

We used a small python script to fetch data from the MAS database, reconstruct the matrix ID (used by synapse to identify a user) and update the external user association in synapse's database.

Note that the script was only tested in a setup where exactly one upstream provider was used and where all accounts were provisioned by that provider.

```python
#!/usr/bin/env python3
# LICENSE: CC-0 or MIT
import psycopg2

SYNAPSE_DB="matrix_synapse"
MAS_DB="matrix_authentication_service"
MATRIX_DOMAIN="example.com"
SYNAPSE_PROVIDER_NAME="oidc"


if __name__ == "__main__":
  syn_conn = psycopg2.connect(f"dbname={SYNAPSE_DB}")
  syn_cur = syn_conn.cursor()
  syn_cur.execute("BEGIN TRANSACTION")

  mas_conn = psycopg2.connect(f"dbname={MAS_DB}")
  mas_cur = mas_conn.cursor()

  # find all users that logged into MAS via OIDC and select their upstream id as well as username
  mas_cur.execute(
      """
      SELECT
          users.username,
          upstream_oauth_links.subject
      FROM upstream_oauth_links
      JOIN users ON users.user_id = upstream_oauth_links.user_id
      """,
  )
  for user_name, user_subject in mas_cur.fetchall():
    # reconstruct the matrix id from the username and matrix server domain
    matrix_id = f"@{user_name}:{MATRIX_DOMAIN}"
    print(f"Un-Migrating user {matrix_id} (id={user_subject})")

    # update upstream user id in synapse but only if it is not already correct
    syn_cur.execute(
        """
        UPDATE user_external_ids
        SET
            auth_provider = %(auth_provider)s,
            external_id = %(external_id)s
        WHERE user_id=%(user_id)s
        AND NOT EXISTS (
            SELECT 1 FROM user_external_ids
            WHERE user_id = %(user_id)s AND external_id = %(external_id)s
        )
        """,
        {
          "auth_provider": SYNAPSE_PROVIDER_NAME,
          "external_id": user_subject,
          "user_id": matrix_id
        }
    )

  syn_cur.execute("COMMIT")
  syn_conn.close()
  mas_conn.close()
```


[^1]: Application Service login is when a [Synapse Appservice](https://element-hq.github.io/synapse/latest/application_services.html) e.g. [mautrix-bridges](https://docs.mau.fi/bridges/general/registering-appservices.html) authenticates against the homeserver with elevated privileges in order to puppet multiple user accounts. Those are the virtual matrix accounts of users on the other side of the bridge.
