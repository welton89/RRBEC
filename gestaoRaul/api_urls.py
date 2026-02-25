from django.urls import path, include
from rest_framework.routers import DefaultRouter
from orders.api_views import OrderViewSet
from products.api_views import ProductViewSet
from clients.api_views import ClientViewSet
from mesas.api_views import MesaViewSet
from comandas.api_views import ComandaViewSet, ProductComandaViewSet
from categories.api_views import CategoriesViewSet
from typePay.api_views import TypePayViewSet
from payments.api_views import PaymentsViewSet
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from login.api_views import MyTokenObtainPairView

router = DefaultRouter()
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'clients', ClientViewSet, basename='client')
router.register(r'mesas', MesaViewSet, basename='mesa')
router.register(r'comandas', ComandaViewSet, basename='comanda')
router.register(r'items-comanda', ProductComandaViewSet, basename='items-comanda')
router.register(r'categories', CategoriesViewSet, basename='category')
router.register(r'payment-types', TypePayViewSet, basename='payment-type')
router.register(r'payments', PaymentsViewSet, basename='payment')

urlpatterns = [
    path('', include(router.urls)),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
