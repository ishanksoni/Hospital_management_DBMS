from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User,Group
from django.template.context_processors import csrf
from django.contrib import messages
from .models import User_detail
from django.contrib.auth.decorators import login_required

@login_required(login_url = '/login/')
def profile(request):
    return render(request,'profile.html')

