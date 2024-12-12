from django.shortcuts import render,redirect

from mesas.models import Mesa

# Create your views here.

def mesas(request):
    mesas = Mesa.objects.all()
    return render(request, 'mesas.html', {'mesas': mesas})



def onOffmesa(request):
    id = request.POST.get('id-mesa')
    mesa_id = int(id)
    mesa = Mesa.objects.get(id=mesa_id)
    mesa.active = not mesa.active
    mesa.save()
    return redirect('mesas')