 
from django.contrib import admin
from django.urls import path, include

from register.views import register
from .views import *

urlpatterns = [
    path('', home),
    path('register/',register),
]