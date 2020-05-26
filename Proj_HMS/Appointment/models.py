from django.db import models
from Profile.models import *

from django.contrib.auth.models import User


class Appointments(models.Model):
    patient = models.ForeignKey(User_detail,on_delete= models.CASCADE)
    doctor = models.ForeignKey(Doctor_details,on_delete=models.CASCADE,null = True)
    date  = models.DateField()
    time = models.TimeField()
    comment =models.CharField(max_length=500)

    class Meta:
        db_table = "appointment"

    def __str__(self):
        return self.doctor.user.username


