from django.urls import path
from . import views


urlpatterns = [
     path('idea/', views.index_feature, name='index_Feature'),
     path('product/<int:fk>/idea/', views.product_feature, name='product_Feature'),
     path('product/feature/create', views.create_feature, name='create_Feature'),
     path('product/feature/delete/<int:pk>', views.del_feature, name='delete_Feature'),
     path('product/feature/edit/<int:pk>', views.edit_feature, name='edit_Feature'),
     ]

