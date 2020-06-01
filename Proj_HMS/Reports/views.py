from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User,Group
from django.template.context_processors import csrf
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required
from Bills.views import check_grp
from datetime import datetime
from Home.context import Context


now_t = datetime.now()
@login_required()
def viewreports(request):
    context = Context(request)
    if Doctor_details.objects.filter(user =request.user).exists():
        if(request.method == "POST"):
            un = request.POST.get('username')
            
            return HttpResponseRedirect('/reports/'+ str(un) + '/')
        else:
            return render(request,'user.html',context)
    else:
        messages.add_message(request, messages.WARNING ,"Accses Denied")
        return HttpResponseRedirect('/')
@login_required()
def report(request,username):
    context = Context(request)
    user = User.objects.get(username=username)
    patient = User_detail.objects.get(user=user)

    if(Report.objects.filter(patient=patient).exists()):
        all_report = Report.objects.filter(patient=patient)
        context =Context(request)
        context['reports'] = all_report
        return render(request,'Viewreport.html',context)
        
    else:   
        messages.add_message(request, messages.WARNING ,"No report Found")
        return HttpResponseRedirect('/')

@login_required()
def gen_report(request):
    context = Context(request)
    if(request.method =="POST"):
        user = request.user
        try:
            doctor = Doctor_details.objects.get(user = request.user)
        except:
            messages.add_message(request, messages.WARNING ,"Access Denied")
            return HttpResponseRedirect('/')

        try:
            un = request.POST.get('username')
            user= User.objects.get(username=un)
            patient = User_detail.objects.get(user=user)
        except:
            messages.add_message(request, messages.WARNING ,"User name not registered")
            return HttpResponseRedirect('/reports/new/')
        nre = Report(doctor = doctor,patient = patient ,history = request.POST.get('history') ,observ = request.POST.get('observ') ,dis = request.POST.get('discrip') ,test = request.POST.get('test'),medic = request.POST.get('medic') ,cmnt = request.POST.get('comment') ,date = now_t.date()   )
        print(type(nre))
        nre.save()


        return HttpResponseRedirect('/')
    else:
        return render(request,'report.html',context)



