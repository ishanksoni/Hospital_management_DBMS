from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from .views import *


urlpatterns = [
    path('book/',book_appointment),
    path('',view_appointments),
]
