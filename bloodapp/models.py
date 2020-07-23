from django.contrib.gis.db import models
from django.db import models
# from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.gis.db import models

import uuid 
from jsonfield import JSONField
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)



class Donor_details(models.Model):
    first_name = models.CharField(max_length=100)
    last_name =  models.CharField(max_length=100)
    email = models.EmailField(max_length = 254) 
    Bloodgroup = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)
    last_blood_given_on = models.DateField() 
    
    def __str__(self):
        return self.Bloodgroup


# class Bloodbank(models.Model):
#     bloodbank_name = models.CharField(max_length=100,unique=True)
#     email = models.EmailField(max_length = 254,blank=True, null=True) 
#     location = models.PointField()
#     address = models.CharField(max_length=100)
#     city = models.CharField(max_length=50)
#     phone = models.CharField(max_length=50)

#     def __str__(self):
#         return self.bloodbank_name


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user
 
class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    # notice the absence of a "Password field", that is built in.
    bloodbank_name = models.CharField(max_length=100,unique=True)
    # location = models.PointField(srid=4326, blank=True)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=50)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] # Email & Password are required by default.

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.bloodbank_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    objects = UserManager()

class Request_details(models.Model):
    Bloodbank = models.ForeignKey(User,on_delete=models.CASCADE)
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

