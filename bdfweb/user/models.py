from django.shortcuts import render, redirect
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date


# Create your models here.
# custom user model for otp verification
# need to work on this user model (not working)

class Donor (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15, null=True)
    place = models.CharField(max_length=50)
    userpin = models.CharField(max_length=6)
    userpic = models.FileField(null=True)
    userbloodgroup = models.CharField(max_length=10)
    userdob = models.CharField(max_length=2)
    regdate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class BloodDonation (models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE)
    userbloodgroup = models.CharField(max_length=10)
    contact = models.CharField(max_length=15, null=True)
    place = models.CharField(max_length=50)
    userdob = models.DateField(max_length=8)
    weight = models.CharField(max_length=3, null=True)
    status = models.CharField(max_length=40, null=True)
    donationdate = models.DateTimeField(auto_now_add=True)
    depremark = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.donor


class ReqBlood (models.Model):
    user = models.ForeignKey(Donor, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50)
    age = models.CharField(max_length=2)
    place = models.CharField(max_length=50)
    pin = models.CharField(max_length=6)
    mob = models.CharField(max_length=15, null=True)
    description = models.CharField(max_length=200)
    bloodgroup = models.CharField(max_length=10)
    pic = models.FileField(null=True)
    status = models.CharField(max_length=40, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.mob


class DonorAppointment (models.Model):
    user = models.ForeignKey(Donor, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    age = models.CharField(max_length=2)
    place = models.CharField(max_length=50)
    pin = models.CharField(max_length=6)
    mob = models.CharField(max_length=15, null=True)
    bloodgroup = models.CharField(max_length=10)
    appointmentdate = models.DateField( max_length=10)
    regulardonor = models.CharField(max_length=6)
    status = models.CharField(max_length=40, null=True)
    departmentremark = models.CharField(max_length=300, null=True)
    date = models.DateTimeField(auto_now_add=True)
    updationdate = models.DateField(null=True)

    def __str__(self):
        return self.mob




