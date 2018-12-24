from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.Create, name='create'),
    path('delete/<int:pk>', views.Delete, name='delete'),
    path('edit/<int:pk>/product/', views.Edit, name='edit'),
    ]
