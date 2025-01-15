from django.shortcuts import render
from django.http import JsonResponse

from mesas.models import Mesa


def mesas(request):
    
    mesas = Mesa.objects.all()
    return render(request, 'mesas.html', {'mesas': mesas})


def mapMesas(request):
    eixosXY = []
    for i in range(0,27):
        for j in range(0,16):
            item = {'x':j*50, 'y':i*50}
            eixosXY.append(item)

    mesas = Mesa.objects.all()
    return render(request, 'mesas_map.html', {'mesas': mesas, 'eixosXY': eixosXY})

def locationMesa(request, mesaId, location):
    print('inicioul')
    mesa = Mesa.objects.get(id=mesaId)
    mesa.location = location
    mesa.save()
    return JsonResponse({'status': 'ok'})
