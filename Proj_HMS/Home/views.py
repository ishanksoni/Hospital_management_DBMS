from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import options

@login_required(login_url = '/login/')

def home(request):    
    actions = options.action(request)
    return render(request,'Home.html',{'actions':actions})