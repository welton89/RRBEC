
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.clients, name='clients'),
    path('createClient', views.createClient, name='createClient'),
    path('editClient', views.editClient, name='editClient'),
    path('payDebt', views.payDebt, name='payDebt'),
    path('viewClient/<int:clientId>', views.viewClient, name='viewClient'),



]
