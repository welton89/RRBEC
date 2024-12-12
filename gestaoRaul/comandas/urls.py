
from django.urls import path
from . import views

urlpatterns = [
    path('', views.comandas, name='comandas'),
    path('viewcomanda/', views.viewComanda, name='viewcomanda'),



]
