from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class myProducts(models.Model):
    ProductTitle = models.CharField(max_length=100)
    Description = models.TextField()
    Objectives = models.TextField()
    Vision = models.TextField()
    SubmissionDate = models.DateTimeField()
    ProductAccessList = models.ManyToManyField(User)

    def __str__(self):
        return self.ProductTitle
