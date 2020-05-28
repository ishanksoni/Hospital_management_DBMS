from django.db import models
from Profile.models import *
from django.contrib.auth.models import User

class Bills(models.Model):
    patient = models.ForeignKey(User_detail,on_delete= models.CASCADE)
    amount = models.IntegerField()
    date  = models.DateField()
    time = models.TimeField()
    detail =models.CharField(max_length=500)
    status = models.BooleanField(default=False)
    class Meta:
        db_table= "bills"


    def __str__(self):
        return self.patient.user.username
