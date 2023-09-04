#!/usr/bin/env bash
# exit on error
set -o errexit

pip install django
pip install dj-database-url
pip install psycopg2
pip install whitenoise

python manage.py collectstatic --no-input
python manage.py migrate