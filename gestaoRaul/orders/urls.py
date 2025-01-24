
from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewsOrders, name='pedidos'),
    path('preparing/<int:order_id>/', views.preparing, name='preparing'),
    path('finished/<int:order_id>/', views.finished, name='finished'),
    path('delivered/<int:order_id>/', views.delivered, name='delivered'),
    path('notificacao/', views.notificacao, name='notificacao'),


]