
from django.urls import path

from comandas import htmx_views
from . import views

urlpatterns = [
    path('', views.comandas, name='comandas'),
    path('viewcomanda/', views.viewComanda, name='viewcomanda'),
    path('createComanda/', views.createComanda, name='createComanda'),
    path('editComanda/', views.editComanda, name='editComanda'),
    path('addContaCliente/', views.addContaCliente, name='addContaCliente'),
    path('notificacao/', views.notificacao, name='notificacao'),
    path('editOrders/<int:productComanda_id>/<str:obs>', views.editOrders, name='editOrders'),
    path('closeComanda/<int:comanda_id>/', views.closeComanda, name='closeComanda'),
    path('listProduct/<int:comanda_id>/<str:product>/', views.listProduct, name='listProduct'),
    path('product=<int:product_id>/comanda=<int:comanda_id>/', views.addProduct, name='addProduct'),



]


htmx_urlpatterns = [
    path('removeProductComanda/<int:productComanda_id>/', htmx_views.removeProductComanda, name='removeProductComanda'),
    path('reopenComanda<int:comanda_id>/', htmx_views.reopenComanda, name='reopenComanda'),
    path('paymentComanda<int:comanda_id>/', htmx_views.paymentComanda, name='paymentComanda'),
    path('paymentParcial<int:comanda_id>/', htmx_views.paymentParcial, name='paymentParcial'),
]

urlpatterns += htmx_urlpatterns