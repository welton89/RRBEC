from django.shortcuts import render
from django.http import JsonResponse

from comandas.models import Comanda
from mesas.models import Mesa
from gestaoRaul.decorators import group_required


def mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'mesas.html', {'mesas': mesas, })


@group_required(groupName='Garçom')
def mapMesas(request):
    eixosXY = []
    for i in range(0,27):
        for j in range(0,16):
            item = {'x':j*50, 'y':i*50}
            eixosXY.append(item)

    mesas = Mesa.objects.all()
    comandas = Comanda.objects.filter(status__in=["OPEN", "PAYING"])
    for mesa in mesas:
        for comanda in comandas:
            if mesa.id == comanda.mesa.id:
                mesa.active = True
                break
    for mesa in mesas:
        print(mesa.active)

    return render(request, 'mesas_map.html', {'comandas': comandas,'mesas': mesas, 'eixosXY': eixosXY})

def locationMesa(request, mesaId, location):
    print('inicioul')
    mesa = Mesa.objects.get(id=mesaId)
    mesa.location = location
    mesa.save()
    return JsonResponse({'status': 'ok'})
