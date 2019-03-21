from django.urls import path
from . import views


urlpatterns = [
    path('kanban/', views.index_board, name='BoardIndex')
    ]