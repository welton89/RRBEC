from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from django.utils import timezone

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_field = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Filtrar pedidos das últimas 15 horas como na view original
        fifteen_hours_ago = timezone.now() - timezone.timedelta(hours=15)
        return Order.objects.filter(queue__gte=fifteen_hours_ago).order_by('-queue')

    def get_serializer_class(self):
        return OrderSerializer

    @action(detail=True, methods=['post'])
    def preparing(self, request, pk=None):
        order = self.get_object()
        order.preparing = timezone.now()
        order.save()
        return Response(OrderSerializer(order).data)

    @action(detail=True, methods=['post'])
    def finish(self, request, pk=None):
        order = self.get_object()
        order.finished = timezone.now()
        order.save()
        return Response(OrderSerializer(order).data)

    @action(detail=True, methods=['post'])
    def deliver(self, request, pk=None):
        order = self.get_object()
        order.delivered = timezone.now()
        order.save()
        return Response(OrderSerializer(order).data)

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        order = self.get_object()
        order.canceled = timezone.now()
        order.save()
        return Response(OrderSerializer(order).data)
