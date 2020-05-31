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
from .models import Bills

def check_grp(user):
    try:
        group = Group.objects.get(name = "Receptionist")
        return True if group in user.groups.all() else False
    except:
        return False

def all_bill():
    all_bills = Bills.objects.all()
    list_bills = []
    for bill in all_bills:
        temp_list = []
        temp_list.append(str(bill.id))
        temp_list.append(str(bill.patient))
        temp_list.append(str(bill.date))
        temp_list.append(str(bill.time)[:8])
        temp_list.append(str(bill.detail))
        temp_list.append(str(bill.status))
        list_bills.append(temp_list)

    return list_bills


@login_required()
def viewbills(request):
    if check_grp(request.user) == True:
        if(request.method == "POST"):
            un = request.POST.get('username')
            return HttpResponseRedirect('/bills/'+ str(un) + '/')
        else:
            list_bills = all_bill() 
            return render(request,'viewbill.html')
    
    else:
        messages.add_message(request, messages.WARNING ,"Accses Denied")
        return HttpResponseRedirect('/')


@login_required()
def bill(request,username):
    user = User.objects.get(username = username)
    patient = User_detail.objects.get(user=user)
    bills = Bills.objects.filter(patient=patient)
    if(request.method=='POST'):
        for bill in bills:
            bill.status = True
            bill.save()
        messages.add_message(request, messages.WARNING ,"Bill Paid")
        return HttpResponseRedirect('/bills/')
    subtotal = 0
    flag =0
    if check_grp(request.user) ==True:
        flag=1
    for bill in bills:
        if(bill.status==False):
            subtotal+=bill.amount
        

    tax = (4*subtotal)/100
    gt = tax+subtotal
    return render(request,'bills.html',{'bills':bills , "user": username , "tax":tax , "subt":subtotal ,"gt" :gt,'flag':flag})
    