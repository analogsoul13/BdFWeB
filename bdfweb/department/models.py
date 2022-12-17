from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Department (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    depname = models.CharField(max_length=100, default="")
    contact = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=300)
    deppic = models.FileField(null=True)
    deppin = models.CharField(max_length=6, null=True)
    depidpic = models.FileField(null=True)
    aboutdep = models.CharField(max_length=600)
    status = models.CharField(max_length=20)
    regdate = models.DateTimeField(auto_now_add=True)
    adminremark = models.CharField(max_length=500)
    updationdate = models.DateField(null=True)
    
    def __str__(self):
        return self.user.username






