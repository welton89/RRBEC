from django.shortcuts import render

# Create your views here.

def mesas(request):
    return render(request, 'mesas.html')