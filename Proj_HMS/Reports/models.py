from django.db import models
from django.contrib.auth.models import User
from Profile.models import *


class Report(models.Model):
    doctor = models.ForeignKey(Doctor_details ,on_delete=models.CASCADE)
    patient = models.ForeignKey(User_detail, on_delete =models.CASCADE)
    history = models.TextField(max_length=1000)
    observ = models.TextField(max_length=1000)
    dis = models.TextField(max_length=1000)
    test = models.TextField(max_length=1000)
    medic = models.TextField(max_length=1000)
    cmnt = models.TextField(max_length=1000)
    date = models.DateField(default = None)

    class Meta:
        db_table = "report"

    def __str__(self):
        return self.patient.user.username

