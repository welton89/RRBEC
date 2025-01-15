
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.clients, name='clients'),
    path('createClient', views.createClient, name='createClient'),
    path('payDebt', views.payDebt, name='payDebt'),



]
