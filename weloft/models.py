from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

class Apartmentname(models.Model):
    Apt_name = models.CharField(max_length=50, default='')
    def __str__(self):
        return self.Apt_name

class PaymentStatus(models.Model):
    status = models.CharField(max_length=100, default='')

class CustomUser(AbstractUser):
    Apt_name = models.ForeignKey(Apartmentname, on_delete=models.CASCADE)
    Flat_no = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.email

class Maintenance(models.Model):
    Apt_name = models.ForeignKey(Apartmentname, on_delete=models.CASCADE)
    AmtPayable = models.CharField(max_length=100, default='')

class Apartment(models.Model):
    Apt_name = models.ForeignKey(Apartmentname, on_delete=models.CASCADE)
    Apt_address = models.CharField(max_length=100, default='')
    Apt_pincode = models.CharField(max_length=100, default='')
    Apt_district = models.CharField(max_length=100, default='')
    Apt_state = models.CharField(max_length=100, default='')
    Apt_phoneNo = models.CharField(max_length=100, default='', blank=True)

    
class Helpinghand(models.Model):
    Apt_name = models.ForeignKey(Apartmentname, on_delete=models.CASCADE)
    Helper1 = models.CharField(max_length=100, default='', blank=True)
    Helper1_role = models.CharField(max_length=100, default='', blank=True)
    Helper1_contact = models.CharField(max_length=100, default='', blank=True)
    Helper2 = models.CharField(max_length=100, default='', blank=True)
    Helper2_role = models.CharField(max_length=100, default='', blank=True)
    Helper2_contact = models.CharField(max_length=100, default='', blank=True)
    Helper3 = models.CharField(max_length=100, default='', blank=True)
    Helper3_role = models.CharField(max_length=100, default='', blank=True)
    Helper3_contact = models.CharField(max_length=100, default='', blank=True)
    Helper4 = models.CharField(max_length=100, default='', blank=True)
    Helper4_role = models.CharField(max_length=100, default='', blank=True)
    Helper4_contact = models.CharField(max_length=100, default='', blank=True)
    Helper5 = models.CharField(max_length=100, default='', blank=True)
    Helper5_role = models.CharField(max_length=100, default='', blank=True)
    Helper5_contact = models.CharField(max_length=100, default='', blank=True)
    Helper6 = models.CharField(max_length=100, default='', blank=True)
    Helper6_role = models.CharField(max_length=100, default='', blank=True)
    Helper6_contact = models.CharField(max_length=100, default='', blank=True)
    def Helper1_(self):
        return self.Helper1


class Facilities(models.Model):
    Apt_name = models.CharField(max_length=50, default='')
    Facility1 = models.CharField(max_length=100, default='', blank=True)
    Max_Occupancy1 = models.CharField(max_length=100, default='', blank=True)
    Facility2 = models.CharField(max_length=100, default='', blank=True)
    Max_Occupancy2 = models.CharField(max_length=100, default='', blank=True)
    Facility3 = models.CharField(max_length=100, default='', blank=True)
    Max_Occupancy3 = models.CharField(max_length=100, default='', blank=True)
    Facility4 = models.CharField(max_length=100, default='', blank=True)
    Max_Occupancy4 = models.CharField(max_length=100, default='', blank=True)
    Facility5 = models.CharField(max_length=100, default='', blank=True)
    Max_Occupancy5 = models.CharField(max_length=100, default='', blank=True)
