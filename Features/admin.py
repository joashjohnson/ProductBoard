from django.contrib import admin
from .models import Ideas
# Register your models here.


@admin.register(Ideas)
class IdeasAdmin(admin.ModelAdmin):
    list_display = ['Title', 'impact', 'effort', 'area', 'createdby']