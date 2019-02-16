#!/usr/bin/env sh


# Fail fast
set -e

source setup.sh
echo 'Running migrations ...'
flask db upgrade
exec gunicorn -c gunicorn_config.py wsgi:app_instance
