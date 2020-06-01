from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User,Group
from django.template.context_processors import csrf
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from Home.context import Context



@login_required(login_url = '/login/')
def profile(request,username):
    context = Context(request)
    menu = {}
    user = User.objects.get(username = username)
    menu['First Name'] = user.first_name
    menu['Last Name'] = user.last_name
    menu['Email'] = user.email
    menu['Date_Joined'] = user.date_joined.date
    try:
        patient = User_detail.objects.get(user=user)
        fields = patient.__dict__
        for field,value in fields.items():
            if(field =='_state' or field == 'id' or field =='user_id' or field == 'doctor_id'):
                continue
            menu[field] = value

    except:
        pass

    try:
        doctor = Doctor_details.objects.get(user = user)
        fields = doctor.__dict__
        for field,value in fields.items():
            if(field =='_state' or field == 'id' or field =='user_id'):
                continue
            menu[field] = value

    except:
        pass
         
    if(request.user.username == username):
        # print(menu)
       
        context['menu'] = menu
        return render(request,'profile.html',context)

    try:
        doctor = Doctor_details.objects.get(user = request.user)
        # print(menu)
        
        context['menu'] = menu
        return render(request,'profile.html',context)
    except:
        messages.add_message(request, messages.WARNING ,"Accses Denied")
        return HttpResponseRedirect('/')


