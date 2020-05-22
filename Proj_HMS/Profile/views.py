from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib import messages
from .models import User_detail

def profile(request):
    return render(request,'profile.html')

def registor(request):
    if(request.method=='POST'):
        
        pass
    else:
        return render(request,'register.html')


       