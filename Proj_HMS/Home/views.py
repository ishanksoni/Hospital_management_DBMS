from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import options

@login_required(login_url = '/login/')

def home(request):    
    menu = options.menu_processor(request)

    messages.add_message(request, messages.INFO, 'Welcome to The Hospital Portal.')
    return render(request,'Home.html',{'menu':menu})