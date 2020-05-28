from django import forms
from django.forms.widgets import *
from .models import Appointments
from django.contrib.admin import widgets
from Profile.models import Doctor_details

class AppointmentForm(forms.Form):
    user_name = forms.CharField(max_length=20)
    doctor_name= forms.ModelChoiceField(queryset=Doctor_details.objects.all())
    # date = forms.DateField(widget= SelectDateWidget(empty_label="enter date"))
    # time = forms.TimeField()
    Comment = forms.CharField(max_length=500 , widget=Textarea)

