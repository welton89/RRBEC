from django.shortcuts import render

# Create your views here.

def mesas(request):
    return render(request, 'mesas.html', {'mesas': ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']})