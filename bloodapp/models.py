from django.contrib.gis.db import models
from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.gis.db import models
import uuid 
from jsonfield import JSONField


class Donor_details(models.Model):
    first_name = models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    email = models.EmailField(max_length = 254) 
    Bloodgroup = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)
    last_blood_given_on = models.DateField() 
    
    def __str__(self):
        return self.Bloodgroup


class Bloodbank(models.Model):
    bloodbank_name = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length = 254,blank=True, null=True) 
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.bloodbank_name


class Request_details(models.Model):
    Bloodbank = models.ForeignKey(Bloodbank,on_delete=models.CASCADE)
    registration_id =  models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length = 254,blank=True, null=True) 
    Bloodgroup = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    donor_details =JSONField(blank=True, null=True)
 