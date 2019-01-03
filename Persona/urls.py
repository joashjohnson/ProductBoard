from django.urls import path
from . import views

urlpatterns = [
    path('persona/', views.pindex, name='pindex'),
    path('persona/create/', views.create_persona, name='pcreate'),
    path('persona/edit/<int:pk>', views.edit_persona, name='pedit'),
    path('persona/delete/<int:pk>', views.del_persona, name='pdelete'),
    path('product/<int:fk>/persona/', views.product_persona, name='personalisting')
    ]
