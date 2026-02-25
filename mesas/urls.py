
from django.urls import path
from . import views

urlpatterns = [
    path('', views.mesas, name='mesas'),
    path('mapMesas/', views.mapMesas, name='mapMesas'),
    path('locationMesa/<int:mesaId>/<str:location>/', views.locationMesa, name='locationMesa'),


]
