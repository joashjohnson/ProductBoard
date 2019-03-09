from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(lists, Card, Board)
class listsAdmin(admin.ModelAdmin):
    list_display= ['listName']