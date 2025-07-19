#!/usr/bin/env sh
set -ex

/usr/local/src/tracker/backend/manage.py migrate
/usr/local/src/tracker/backend/manage.py check --deploy

nginx
node /usr/local/src/tracker/frontend/.output/server/index.mjs &
/usr/local/src/tracker/backend/manage.py runserver --noreload --nostatic 0.0.0.0:8001
