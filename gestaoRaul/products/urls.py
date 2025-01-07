
from django.urls import path
from . import views

urlpatterns = [
    path('', views.products, name='products'),
    path('create_product', views.createProduct, name='create_product'),
    path('onOffproduct', views.onOffProduct, name='onOffproduct'),
    path('searchProduct', views.searchProduct, name='searchProduct'),
    path('editProduct/<int:productId>/', views.editProduct, name='editProduct'),

]
