from django.shortcuts import render

# Create your views here.

def comandas(request):
    return render(request, 'comandas.html')