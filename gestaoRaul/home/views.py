from django.shortcuts import render
from django.db.models import Sum
from django.db.models import Count, F

from comandas.models import ProductComanda
from products.models import Product
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
