
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url

from LoginApp.views import login,logout
urlpatterns = [
    path('',include('Home.urls')),
    path('admin/', admin.site.urls),
    path('login/',login),
    path('logout/',logout),
    path('profile/',include('Profile.urls')),  
    path('appointments/',include('Appointment.urls')),
]

