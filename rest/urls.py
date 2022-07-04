from django.contrib import admin
from django.urls import path

from .views import getdata, home

urlpatterns = [
    path('',home),
    path('getdata',getdata),
]
