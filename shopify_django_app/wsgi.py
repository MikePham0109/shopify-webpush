"""
WSGI config for shopify_django_app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopify_django_app.settings')

on_heroku = os.environ.get("ON_HEROKU")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shopify_django_app.settings')
    

application = get_wsgi_application()
