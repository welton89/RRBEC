from rest_framework import viewsets, permissions
from .models import TypePay
from .serializers import TypePaySerializer

class TypePayViewSet(viewsets.ModelViewSet):
    queryset = TypePay.objects.all()
    serializer_class = TypePaySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
