#!/usr/bin/env bash


# Fail fast
set -e

source setup.sh
echo 'Running migrations'
flask db upgrade
gunicorn -c gunicorn_config.py wsgi:app_instance
