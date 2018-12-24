from django.contrib import admin
from .models import user_persona
# Register your models here.

@admin.register(user_persona)
class ProductAdmin(admin.ModelAdmin):
    list_display= ['PersonaName']