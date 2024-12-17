
from django.urls import path

from comandas import htmx_views
from . import views

urlpatterns = [
    path('', views.comandas, name='comandas'),
    path('viewcomanda/', views.viewComanda, name='viewcomanda'),
    path('createComanda/', views.createComanda, name='createComanda'),



]


htmx_urlpatterns = [
    # path('listProduct/', htmx_views.listProduct, name='listProduct'),
    path('listProduct/<int:comanda_id>/', htmx_views.listProduct, name='listProduct'),
    path('addProduct<int:product_id>/<int:comanda_id>/', htmx_views.addProduct, name='addProduct'),
    path('removeProductComanda<int:productComanda_id>/', htmx_views.removeProductComanda, name='removeProductComanda'),
    # path('removeProduct/', views.removeProduct, name='removeProduct'),

]

urlpatterns += htmx_urlpatterns