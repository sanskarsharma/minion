#!/usr/bin/env sh


# Fail fast
set -e

source setup.sh

while true; do
    echo 'Attempting to connect to db and run upgrade (migrations) ...'
    flask db upgrade
    if [[ "$?" == "0" ]]; then
        echo 'Migrations ran successfully ...'
        break
    fi
    echo 'Upgrade command failed, retrying in 5 secs...'
    sleep 5
done

echo 'Starting app ...'
exec gunicorn -c gunicorn_config.py wsgi:app_instance
