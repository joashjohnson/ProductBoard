from django.db import models

# Create your models here.

class user_persona(models.Model):
    PersonaName = models.CharField(max_length=100)
    PersonaDescription = models.TextField()
    PersonaBehaviors = models.TextField()
    PersonaGoals = models.TextField()
    PFrustrationsLimitations = models.TextField()
    Picmage = models.ImageField(upload_to='persona_images', blank=True)
    def __str__(self):
        return self.PersonaName