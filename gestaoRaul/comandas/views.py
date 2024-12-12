from django.shortcuts import render, redirect

from comandas.models import Comanda

# Create your views here.

def comandas(request):
    comandas = Comanda.objects.all()
    return render(request, 'comandas.html', {'comandas': comandas})




def viewComanda(request):
    id = request.GET.get('parametro')
    comanda_id = int(id)
    comanda = Comanda.objects.get(id=comanda_id)
  
    return render(request, 'viewcomanda.html', {'comanda': comanda})