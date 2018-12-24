from django.urls import path
from . import views

urlpatterns = [
    path('persona/', views.pindex, name='pindex'),
    ]
