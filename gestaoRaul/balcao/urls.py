
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
    path('listProduct/<int:comanda_id>/', htmx_views.listProduct, name='listProduct'),
    path('addProduct<int:product_id>/<int:comanda_id>/', htmx_views.addProduct, name='addProduct'),
    path('removeProductComanda<int:productComanda_id>/', htmx_views.removeProductComanda, name='removeProductComanda'),
    # path('closeComanda<int:comanda_id>/', htmx_views.closeComanda, name='closeComanda'),
    # path('reopenComanda<int:comanda_id>/', htmx_views.reopenComanda, name='reopenComanda'),
    path('paymentComanda<int:comanda_id>/', htmx_views.paymentComanda, name='paymentComanda'),
]

urlpatterns += htmx_urlpatterns