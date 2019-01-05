from django.contrib import admin
from .models import user_persona
from Products.models import myProducts
# Register your models here.

@admin.register(user_persona)
class ProductAdmin(admin.ModelAdmin):
    list_display= ['PersonaName']