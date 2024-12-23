
from django.urls import path

from balcao import htmx_views
from . import views

urlpatterns = [
    # path('', views.comandas, name='comandas'),
    path('', views.viewBalcao, name='viewBalcao'),
    # path('createComanda/', views.createComanda, name='createComanda'),

]


htmx_urlpatterns = [
    # path('listProduct/', htmx_views.listProduct, name='listProduct'),
    path('listProduct/<int:comanda_id>/', htmx_views.listProductBalcao, name='listProductBalcao'),
    path('addProduct<int:product_id>/<int:comanda_id>/', htmx_views.addProductBalcao, name='addProductBalcao'),
    path('removeProductComanda<int:productComanda_id>/', htmx_views.removeProductBalcao, name='removeProductBalcao'),
    # path('closeComanda<int:comanda_id>/', htmx_views.closeComanda, name='closeComanda'),
    # path('reopenComanda<int:comanda_id>/', htmx_views.reopenComanda, name='reopenComanda'),
    path('paymentComanda<int:comanda_id>/', htmx_views.paymentBalcao, name='paymentBalcao'),
]

urlpatterns += htmx_urlpatterns