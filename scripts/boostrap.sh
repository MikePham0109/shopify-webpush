#/bin/bash

pipenv run python manage.py migrate --settings shopify_django_app.heroku_settings
pipenv run python manage.py runserver 0.0.0.0:8000
