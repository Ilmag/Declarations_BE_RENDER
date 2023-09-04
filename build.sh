#!/usr/bin/env bash
# exit on error
set -o errexit

pip install django
pip install dj-database-url
pip install psycopg2
pip install whitenoise
pip install gunicorn
pip install django-rest-framework
pip install django-filter

python manage.py collectstatic --no-input
python manage.py migrate