from django.urls import path
from django.shortcuts import redirect

from . import views

urlpatterns = [
    path('', views.index, name='root_path'),
    path('sw/ssp', views.send_file, name='send_file'),
]
