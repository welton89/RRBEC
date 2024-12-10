
from django.urls import path
from . import views

urlpatterns = [
    path('', views.typePay, name='typePay'),



]
