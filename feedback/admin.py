from django.contrib import admin
from .models import productFeedback

@admin.register(productFeedback)
# Register your models here.
class productFeedbackAdmin(admin.ModelAdmin):
    list_display= ['name','email']