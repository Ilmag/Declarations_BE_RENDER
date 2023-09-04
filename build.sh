#!/usr/bin/env bash
# exit on error
set -o errexit

pip install django
pip install django-rest-framework
pip install psycopg2
pip install django-cors-headers
pip install django-filter

python manage.py collectstatic --no-input
python manage.py migrate