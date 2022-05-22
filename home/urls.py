from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('', views.index, name='root_path'),
    # for more redirect's usage options: https://docs.djangoproject.com/en/2.1/topics/http/shortcuts/
    path('static/service-wokers/ssp-sw.js/', lambda request: redirect('/static/service-wokers/ssp-sw.js', permanent=True)),
]
