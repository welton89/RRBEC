
from django.urls import path
from . import views

urlpatterns = [
    path('', views.comandas, name='comandas'),



]
