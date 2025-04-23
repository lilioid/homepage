---
title: Writing feeds for fun and nonprofit
author: lilly
short_desc: >-
    Implementation notes (and heads up) about implementing RSS and atom feeds as well as making them discoverable
lang: en
tags: [ "blog-meta", "tech" ]
created_at: "2024-10-08 14:30:00+02"
edited_at: "2024-12-31 18:30:00+02"
---

What would a blog be without an RSS feed? Or an atom feed?
_It ain't a real one I tell ya!!_
Anyways, so I decided to implement the two feed format so that readers can easily subscribe to my amazing content ;).

First of, there are two different but similar standards modelling the use case of a _feed of information_.
Both of these follow the same model of being served under a specific URL which a client (a.k.a. feed reader) has to regularly check for updates.
Both feed formats are also based on XML and have a similar structure.
Where they differ is the exact naming and meaning of XML tags and attributes as well as the encoding of the information inside them.
More details to that in the two following sections [RSS](#rss) and [Atom](#atom).

## RSS

The RSS feed of this website is at [/blog/feed.rss](/blog/feed.rss) while its source code is at [github.com/lilioid/homepage:src/homepage/templates/blog/feed.rss](https://github.com/lilioid/homepage/blob/main/src/homepage/templates/blog/feed.rss).

RSS is kind of an old standard[^1] (the newest version is from 2009) that is now frozen for eternity.
No new development is happening any more and alternative formats should replace RSS instead (e.g. [Atom](#atom)).
Nonetheless, RSS is a popular mechanism to subscribe to content updates of, for example, a blog like this one.
For this reason, I decided to build an RSS feed despite it being old and frozen.

One of the side effects of RSS being old is that it is kind of weird.
Here are some examples:

- The [RSS Best Practices Profile](https://www.rssboard.org/rss-profile) profile is a much more useful document than the actual specification.
- The specification mentions only a `<channel>` element which contains a logical feed.
  The channel must be wrapped into an `<rss>` element though. I did not find a mention about that in the specification :/
- RSS uses a super weird date format.
  It's the one from [RFC 822](https://datatracker.ietf.org/doc/html/rfc822), obsoleted by [RFC 2822](https://datatracker.ietf.org/doc/html/rfc2822), obsoleted by [RFC 5322](https://datatracker.ietf.org/doc/html/rfc5322), updated by [RFC 6854](https://datatracker.ietf.org/doc/html/rfc6854).
  Not all of these are relevant but it still makes my point of the date format being old and weird.<br>
  The exact format used is for example `Sat, 07 Sep 2002 09:42:31 GMT` (note the repeating day information and that two fields are spelled out) which can be achieved by formatting a [python datetime object](https://docs.python.org/3/library/datetime.html) with `strftime('%a, %d %b %Y %H:%M:%S %z')`.
- Similarly, the mail format is also weird.
  To be precise, the exact mail format is unspecified, but the one that is used as examples in the spec is `name@example.com (Firstname Lastname)`.
  Most people nowadays would expect something like `name <name@example.com>` instead (at least I did) and while it is technically valid to just use that, it is recommended against.


## Atom

The Atom feed of this website is at [/blog/feed.atom](/blog/feed.atom) while its source code is at [github.com/lilioid/homepage:src/homepage/templates/blog/feed.atom](https://github.com/lilioid/homepage/blob/main/src/homepage/templates/blog/feed.atom).

Atom is a standard that aims to develop further on the ideas that were introduced by RSS but clean up the standard and use more modern formats.
In doing so it brought several improvements such as using a proper XML namespace[^2] or replacing the old timestamps with [RFC 3339](https://datatracker.ietf.org/doc/html/rfc3339) timestamps (e.g. `2024-10-01T09:50:00+02:00`).<br>
Modelling information about people has also been improved by not just specifying an "email" field without an explicit format. Instead, atom feeds subdivide `<author>` elements into `<name>` and `<email>` child elements.<br>
Notably, atom feeds also allow duplication of elements as long as they contain their content in different languages and indicate this properly.
This allows feed readers to potentially display the feeds content in the users language.


## Feed Discoverability

While having feeds is useful, they need to be discoverable so that users can use them.
Explicitly linking to feed URLs is one way but additionally, HTML includes a way to link to the syndication feed associated with the current document[^3].

This is done by adding a `<link>` tag to the HTML `<head>` that contains relation and type information as can be seen in the code block below:

```html
<!-- A link to the RSS feed -->
<link rel="alternate" type="application/rss+xml" href="/blog/feed.rss" title="Lillys Thoughts">

<!-- A link to the atom feed -->
<link rel="alternate" type="application/atom+xml" href="/blog/feed.atom" title="Lillys Thoughts">
```

When these links are implemented, a user can just enter _https://li.lly.sh_ in their feed reader which then scans for these links and displays a choice of feeds to subscribe to.



[^1]: RSS Specification: [https://www.rssboard.org/rss-specification](https://www.rssboard.org/rss-specification)
[^2]: A way to allow XML consumers to validate the allowed formats and attributes of tags used in an XML document. Different namespaces can even be mixed inside the same document which allows consumers to only regard the ones they are interested in and know how to handle.
[^3]: [MDN Documentation on the "rel" HTML attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel#alternate)
