
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mesas, name='mesas'),
    path('onOffmesa/', views.onOffmesa, name='onOffmesa'),




]
