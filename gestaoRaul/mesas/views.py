from django.shortcuts import render,redirect, HttpResponse
from django.http import JsonResponse


from mesas.models import Mesa

# Create your views here.

def mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'mesas.html', {'mesas': mesas})


def mapMesas(request):
    eixosXY = []
    for i in range(0,25):
        for j in range(0,15):
            item = {'x':j*50, 'y':i*50}
            eixosXY.append(item)

    mesas = Mesa.objects.all()
    return render(request, 'mesas_map.html', {'mesas': mesas, 'eixosXY': eixosXY})

def locationMesa(request, mesaId, location):
    mesa = Mesa.objects.get(id=mesaId)
    mesa.location = location
    mesa.save()
    return JsonResponse({'status': 'ok'})
# def onOffmesa(request):
#     id = request.POST.get('id-mesa')
#     mesa_id = int(id)
#     mesa = Mesa.objects.get(id=mesa_id)
#     mesa.active = not mesa.active
#     mesa.save()
#     return redirect('mesas')