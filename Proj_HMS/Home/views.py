from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . import options
from .covid19 import *

@login_required(login_url = '/login/')

def home(request):
    if request.method == 'POST':
        state = request.POST.get("state")
        dat = findstate(state)
        actions = options.action(request)
        return render(request,'Home.html',{'actions':actions,'death':death,'total':total_case,'dis':dis,'rt':dat['rt']
        ,'de':dat['de'],'di':dat['di'],'st':state,'ls':ls})

    else:
        dat =findstate("Rajasthan")
        actions = options.action(request)
        return render(request,'Home.html',{'actions':actions,'death':death,'total':total_case,'dis':dis,'rt':dat['rt']
        ,'de':dat['de'],'di':dat['di'],'st':"Rajasthan",'ls':ls})