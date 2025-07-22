#!/usr/bin/env sh
set -ex

/usr/local/src/homepage/manage.py migrate
/usr/local/src/homepage/manage.py check --deploy

/usr/local/src/homepage/manage.py runserver --noreload --nostatic 0.0.0.0:8000
