from django.shortcuts import render

# Create your views here.

def typePay(request):
    return render(request, 'typePay.html')