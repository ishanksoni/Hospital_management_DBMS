from django.db import models
from django.contrib.auth.models import User

class User_detail(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE)
    contact_no = models.CharField(max_length = 15)
    address = models.CharField(max_length = 200)
    gender = models.CharField(max_length = 10,default="other")

    dob = models.DateField()

    blood_group = models.CharField(max_length=3)

    def __str__(self):
        return self.user.username