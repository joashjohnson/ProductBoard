from django.db import models

# Create your models here.
class myProducts(models.Model):
    ProductTitle = models.CharField(max_length=100)
    Description = models.TextField()
    Objectives = models.TextField()
    Vision = models.TextField()
    SubmissionDate = models.DateTimeField()
    def __str__(self):
        return self.ProductTitle
        