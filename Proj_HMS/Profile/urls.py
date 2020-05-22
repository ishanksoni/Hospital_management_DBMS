from .views import *
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url


urlpatterns = [
    path('',profile),
]