from rest_framework import viewsets, permissions
from .models import Payments
from .serializers import PaymentsSerializer

class PaymentsViewSet(viewsets.ModelViewSet):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Opcionalmente filtrar pagamentos recentes
        return Payments.objects.all().order_by('-datetime')
