from django.urls import path
from . import views

urlpatterns = [
     path('accounts/login/', views.login_view, name='login'),
     path('accounts/logout', views.logout_view, name='logout'),
    ]
