from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth   
from django.contrib.auth.models import User,Group
from django.template.context_processors import csrf
from django.contrib import messages
from Profile.models import *
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm
from . models import Appointments
from Bills.models import Bills
import datetime
from Home.context import Context
now_t = datetime.datetime.now()



def check_grp(user):
    try:
        group = Group.objects.get(name = "Receptionist")
        return True if group in user.groups.all() else False
    except:
        return False


@login_required()
def book_appointment(request):
    context = Context(request)
    if check_grp(request.user) == True:
        if(request.method=='POST'):
            form = AppointmentForm(request.POST)

            print("paased")
            if form.is_valid():
                form.cleaned_data
                un      = form.cleaned_data['user_name']
                dn      = form.cleaned_data['doctor_name']
                date    = request.POST.get('date')
                time    =  request.POST.get('time')
                comment = form.cleaned_data['Comment']
                if(User.objects.filter(username = un).exists()):
                    user = User.objects.get(username = un)
                    patient = User_detail.objects.get(user=user)
                    # user = User.objects.get(username = dn)
                    # doctor = Doctor_details.objects().get(user = user)
                    appointment = Appointments(patient = patient ,doctor = dn ,time= time,date= date,comment=comment)
                    appointment.save()
                    new_bill = Bills( patient = patient , amount = 150 ,date = now_t.date() ,time = now_t.time(), detail = "Appointment Charges to")
                    new_bill.save()
                    patient.doctor=dn
                    patient.save()
                    print(patient.doctor)
                    messages.add_message(request, messages.WARNING ,"Successfully added appointment")
                    return HttpResponseRedirect('/')
                else:
                    messages.add_message(request, messages.WARNING ,"Patient not registerd")
                    return HttpResponseRedirect('/register/')

            else:

                return HttpResponseRedirect('/appointments/book/')
        else:
            form = AppointmentForm()
            
            context['form'] = form
            return render(request,'appointment.html',context)
    else:
        messages.add_message(request, messages.WARNING ,"Accses Denied")
        return HttpResponseRedirect('/')


def view_appointments(request):
    context = Context(request)
    try:
        doctor = Doctor_details.objects.get(user =request.user)

    except:
        messages.add_message(request, messages.WARNING ,"Accses Denied")
        return HttpResponseRedirect('/')
        
    all_appointment = Appointments.objects.filter(doctor=doctor)
    up_list = []
    past_list =[]
    list_appointments = []
    for appoint in all_appointment:
        temp_list = {}
        temp_list['patient'] = str(appoint.patient)
        temp_list['date'] = str(appoint.date)
        temp_list['time'] = str(appoint.time)
        temp_list['comment'] = str(appoint.comment)
        if(appoint.date < now_t.date()):
            past_list.append(temp_list)
        elif(appoint.date==now_t.date()):
            if(appoint.time<now_t.time()):
                past_list.append(temp_list)
            else:
                up_list.append(temp_list)

        else:
            up_list.append(temp_list)
        list_appointments.append(temp_list)

    # print(up_list ," up  coming list is -----1-1-1-")
    # print(past_list)
    context['up'] = up_list
    context['pre'] = past_list
    context['now_t'] = now_t
    return render(request,'view.html',context)  
  