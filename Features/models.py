from django.db import models
from Products.models import *
# Create your models here.
from datetime import datetime

class Ideas(models.Model):
    iProduct = models.ForeignKey(myProducts, on_delete=models.CASCADE)
    AREA_CHOICES =[('B','Backlog'), ('U','Unsorted'), ('C','Completed')]
    Title= models.CharField(max_length=100)
    Desciption = models.TextField()
    problems = models.TextField()
    business_reasons = models.TextField()
    impact = models.IntegerField()
    effort = models.IntegerField()
    createdby = models.CharField(max_length=100)
    owner = models.CharField(max_length=100)
    datecreated = models.DateTimeField(default=datetime.now, blank=True)
    area = models.CharField(max_length=100,choices=AREA_CHOICES, default=AREA_CHOICES[1][1])