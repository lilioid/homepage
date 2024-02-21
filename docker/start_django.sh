#!/usr/bin/bash
set -e

D=/usr/local/src/homepage/src/
$D/manage.py migrate
$D/manage.py collectstatic --noinput
$D/manage.py check --deploy

exec gunicorn \
  --workers=$(nproc --all) \
  --pythonpath /usr/local/src/homepage/src/ \
  homepage.wsgi:application
