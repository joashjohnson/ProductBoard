from django.contrib import admin
from .models import myProducts

# Register your models here.
@admin.register(myProducts)
class ProductAdmin(admin.ModelAdmin):
    list_display= ['ProductTitle','SubmissionDate']