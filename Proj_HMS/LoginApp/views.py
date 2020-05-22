from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib import messages


def login(request):
    if request.method == 'POST':
        username =  request.POST.get('username','')
        password  = request.POST.get('password','')

        user = auth.authenticate(username=username,password = password)

        if user is not None:
            auth.login(request,user)
            messages.add_message(request, messages.INFO, 'Your are now Logged in.')

            return HttpResponseRedirect('/')

        else:
            messages.add_message(request, messages.INFO,'FAILED LOGIN')
            return render(request,'login.html')

    else:
        return render(request,'login.html')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    messages.add_message(request, messages.INFO, 'You are Successfully Logged Out')
    messages.add_message(request, messages.INFO, 'Thanks for visiting.')
    return HttpResponseRedirect('/login')

    