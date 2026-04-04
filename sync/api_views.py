from rest_framework import viewsets
from .models import ChangeLog
from .serializers import ChangeLogSerializer

class ChangeLogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ChangeLog.objects.all()
    serializer_class = ChangeLogSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        since_id = self.request.query_params.get('since_id')
        if since_id:
            queryset = queryset.filter(id__gt=since_id)
        return queryset
