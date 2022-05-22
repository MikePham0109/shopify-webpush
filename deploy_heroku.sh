#!/bin/bash

# Please run heroku login before running this script

# heroku container:login
# heroku container:push shopify_django_app_web -a ssp-webpush
# heroku container:release shopify_django_app_web -a ssp-webpush

# heroku git:remote -a ssp-webpush

#heroku buildpacks:set heroku/python -a ssp-webpush

git push heroku master