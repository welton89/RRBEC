from rest_framework import viewsets, permissions
from .models import Categories
from .serializers import CategoriesSerializer

class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
