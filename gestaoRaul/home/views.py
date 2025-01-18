from django.shortcuts import render
from django.db.models import Sum
from django.db.models import Count, F
from django.http import JsonResponse, HttpResponse
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.utils.dateparse import parse_datetime

import datetime
import json



from comandas.models import ProductComanda
from orders.models import Order
from payments.models import Payments
from gestaoRaul.decorators import group_required

@group_required(groupName='Gerente')
def home(request):

        return render(request, 'home.html')


@group_required(groupName='Gerente')
def chartCuisine(request,dateStart,dateEnd):
    try:
        dateStart = parse_datetime(dateStart+' 07:00:00')
        dateEnd = parse_datetime(dateEnd+' 07:00:00')+ datetime.timedelta(days=1)
    except:
        dateStart = parse_datetime('2025-01-01 07:00:00')
        dateEnd = datetime.datetime.now()

    tFila = []
    tPreparando = []
    tFinalizado = []

    total_pagamentos =  Payments.objects.filter(datetime__range=(dateStart, dateEnd)).aggregate(total=Sum('value'))['total']
    total_pagamentos = 0 if total_pagamentos is None else total_pagamentos
    qdt_pagamentos = Payments.objects.filter(datetime__range=(dateStart, dateEnd)).aggregate(total=Count('value'))['total']
    qdt_pagamentos = 0 if qdt_pagamentos is None else qdt_pagamentos
    try:
        ticket_medio = total_pagamentos / qdt_pagamentos
    except:
        ticket_medio = 0

    try:
        produtos_mais_vendidos = ProductComanda.objects.filter(
                                    data_time__range=(dateStart, dateEnd)
                                ).values('product').annotate(
                                    quantidade=Count('product'),
                                    nome=F('product__name')
                                ).order_by('-quantidade')[:5]
        maisVendidos = {}
        for produto in produtos_mais_vendidos:
            maisVendidos[produto['nome']] = produto['quantidade']
        produtos_mais_vendidos = maisVendidos
  
    except:
        produtos_mais_vendidos = {
                                    'petra': 25,
                                    'petra2': 26,
                                    'petra3': 27,
                                    'petra4': 28,
                                    'petra5': 29,
                                  }
      
    orders = Order.objects.filter(delivered__isnull=False, queue__gt=dateStart, queue__lt=dateEnd)
    try:
        for order in orders:
            tFila.append((order.preparing - order.queue).total_seconds())
            tPreparando.append((order.finished - order.preparing).total_seconds())
            tFinalizado.append((order.delivered - order.finished).total_seconds())

        mediaFila = int((sum(tFila) / len(tFila))/60)
        mediaPreparando = int((sum(tPreparando) / len(tPreparando))/60)
        mediaFinalizado = int((sum(tFinalizado) / len(tFinalizado))/60)

        return JsonResponse({
            'mediaFila': mediaFila,
            'mediaPreparando': mediaPreparando,
            'mediaFinalizado': mediaFinalizado,
            'total_pagamentos': round(total_pagamentos, 2),
            'qtd_pagamentos': qdt_pagamentos,
            'ticket_medio': round(ticket_medio, 2),
            'produtos_mais_vendidos': produtos_mais_vendidos,
            })
    except:
        return JsonResponse({
            'mediaFila': 0,
            'mediaPreparando': 0,
            'mediaFinalizado': 0,
            'total_pagamentos': round(total_pagamentos, 2),
            'qtd_pagamentos': qdt_pagamentos,
            'ticket_medio': round(ticket_medio, 2),
            'produtos_mais_vendidos': produtos_mais_vendidos,
            })
