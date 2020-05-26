from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User,Group
from django.template.context_processors import csrf
from django.contrib import messages
from Profile.models import User_detail
from django.contrib.auth.decorators import login_required
from Appointment.views import *

def check_grp(user):
    try:
        group = Group.objects.get(name="Receptionist")
        return True if group in user.groups.all() else False
    except:
        return False


@login_required(login_url = '/login/')
def register(request):
    if check_grp(request.user) == True:
        if(request.method=='POST'):
            fn = request.POST.get('firstname')
            ln = request.POST.get('lastname')
            email = request.POST.get('eamil')
            cn = request.POST.get('contact')
            un = request.POST.get('username')
            p1 = request.POST.get('password')
            p2 = request.POST.get('confirm-password')
            gen = request.POST.get('gender')
            dob = request.POST.get('dob')
            bldg = request.POST.get('bldg')
            adres = request.POST.get('address')
            if( User.objects.filter(username = un).exists()):
                messages.add_message(request, messages.WARNING ,"username already exists")
                return HttpResponseRedirect('/register/')
            if(p1!=p2):
                messages.add_message(request, messages.WARNING ,"password didnot matched")
                return HttpResponseRedirect('/register/')

            new_user = User.objects.create_user(username=un,email=email,password=p1,first_name = fn , last_name = ln)
            new_user.save()


            details = User_detail(user = new_user , gender = gen , blood_group = bldg ,contact_no = int(cn) , address = adres, dob= dob)
            details.save()
            group = Group.objects.get(name= 'Patients')
            new_user.groups.add(group)
            
                # messages.add_message(request, messages.WARNING ,"Error occured in database")
                # return HttpResponseRedirect('/register/')
            messages.add_message(request, messages.WARNING , 'Successfully Registered' + un)
            return HttpResponse("successfully registered")
        else:   
            return render(request,'register.html')
    else:
        messages.add_message(request, messages.WARNING ,"Hold right there !!Accses Denied")
        return HttpResponseRedirect('/')

            
    

