from django.shortcuts import render
from django.db.models import Sum
from django.db.models import Count, F
from django.http import JsonResponse


from comandas.models import ProductComanda
from orders.models import Order
from payments.models import Payments

def home(request):
    total_pagamentos = Payments.objects.aggregate(total=Sum('value'))['total']
    qdt_pagamentos = Payments.objects.aggregate(total=Count('value'))['total']
    pagamentos = Payments.objects.all()
    ticekMedio = total_pagamentos / qdt_pagamentos

    produtos_mais_vendidos = ProductComanda.objects.values('product').annotate(
    quantidade=Count('product'),
    nome=F('product__name') ).order_by('-quantidade')[:5]
    return render(request, 'home.html', {'total_pagamentos': total_pagamentos, 'pagamentos': pagamentos, 'qdt_pagamentos': qdt_pagamentos, 'produtos_mais_vendidos': produtos_mais_vendidos, 'ticekMedio': ticekMedio})


def chartCuisine(request):
    print('entrooooooouuuuu')
    tFila = []
    tPreparando = []
    tFinalizado = []

    orders = Order.objects.filter(delivered__isnull=False)

    for order in orders:
        tFila.append((order.preparing - order.queue).total_seconds())
        tPreparando.append((order.finished - order.preparing).total_seconds())
        tFinalizado.append((order.delivered - order.finished).total_seconds())

    mediaFila = int((sum(tFila) / len(tFila))/60)
    mediaPreparando = int((sum(tPreparando) / len(tPreparando))/60)
    mediaFinalizado = int((sum(tFinalizado) / len(tFinalizado))/60)

    # orders = Order.objects.filter(
    # created_at__gte='a',
    # created_at__lte='b',
    # delivered__isnull=False
    # )

    return JsonResponse({
        'mediaFila': mediaFila,
        'mediaPreparando': mediaPreparando,
        'mediaFinalizado': mediaFinalizado,
        })