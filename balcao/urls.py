
from django.urls import path

from balcao import htmx_views
from . import views

urlpatterns = [
    path('', views.viewBalcao, name='viewBalcao'),

]


htmx_urlpatterns = [
    path('listProductBalcao/<int:comanda_id>/<str:search_product>/', htmx_views.listProductBalcao, name='listProductBalcao'),
    path('addProductBalcao<int:product_id>/<int:comanda_id>/<int:qtd>/', htmx_views.addProductBalcao, name='addProductBalcao'),
    path('addProductBalcaoTeclado<int:product_id>/<int:comanda_id>/<int:qtd>/', htmx_views.addProductBalcaoTeclado, name='addProductBalcaoTeclado'),
    path('removeProductBalcao<int:productComanda_id>/', htmx_views.removeProductBalcao, name='removeProductBalcao'),
    path('paymentBalcao<int:comanda_id>/', htmx_views.paymentBalcao, name='paymentBalcao'),
]

urlpatterns += htmx_urlpatterns