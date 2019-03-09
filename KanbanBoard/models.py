from django.db import models
from Products.models import *
from django.contrib.auth.models import User
# Create your models here.

class lists(models.Model):
    listName = models.CharField(max_length=120)
    BoardLists = models.ForeignKey('Board',default=1, on_delete=models.CASCADE)
    listorder = models.IntegerField()

    def __str__(self):
        return self.listName

class Card(models.Model):
    listitem = models.ForeignKey('lists', default=1, on_delete=models.CASCADE)
    Cardtitle = models.CharField(max_length=120)
    Cardimage = models.ImageField(upload_to='card_images', blank=True)
    CardDescription = models.TextField()
    CardAssigned = models.ManyToManyField(User)

    def __str__(self):
        return self.Cardtitle

class Board(models.Model):
    BoardTitle = models.CharField(max_length=120)
    AccessList = models.ManyToManyField(User)
    BoardProductList = models.ForeignKey(myProducts, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.BoardTitle