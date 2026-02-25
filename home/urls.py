from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('chartCuisine/<str:dateStart>/<str:dateEnd>', views.chartCuisine, name='chartCuisine'),

]
