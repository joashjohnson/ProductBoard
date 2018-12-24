from django.db import models

# Create your models here.
class productFeedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=1000)
    message = models.TextField()
    def __unicode__(self):
        return self.name