from django.db import models
from Products.models import *
# Create your models here.
from datetime import datetime
from django.contrib.auth.models import User


class Ideas(models.Model):
    iProduct = models.ForeignKey(myProducts, on_delete=models.CASCADE)
    AREA_CHOICES =[('B','Backlog'), ('U','Unsorted'), ('C','Completed'), ('O','Optimisation Testing'), ('I','In Progress'), ('I','Investigation'), ('D','Discovery')]
    Title= models.CharField(max_length=100)
    Desciption = models.TextField()
    problems = models.TextField()
    business_reasons = models.TextField()
    impact = models.IntegerField()
    effort = models.IntegerField()
    createdby = models.ForeignKey(User, on_delete= models.SET_NULL, blank=True,null=True,related_name='a')
    owner = models.ForeignKey(User,on_delete= models.SET_NULL, blank=True,null=True,related_name='b')
    datecreated = models.DateTimeField(default=datetime.now, blank=True)
    area = models.CharField(max_length=100,choices=AREA_CHOICES, default=AREA_CHOICES[1][1])