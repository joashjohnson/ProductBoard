from django.contrib import admin
from .models import lists, Board, Card


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ['BoardTitle']

@admin.register(lists)
class ListAdmin(admin.ModelAdmin):
    list_display = ['listName']


@admin.register(Card)
class ListAdmin(admin.ModelAdmin):
    list_display = ['Cardtitle']