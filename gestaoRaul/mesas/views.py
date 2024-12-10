from django.shortcuts import render

from mesas.models import Mesa

# Create your views here.

def mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'mesas.html', {'mesas': mesas})