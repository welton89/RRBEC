from django.shortcuts import render
from django.contrib.auth.models import User

from gestaoRaul.decorators import group_required


def clients(request):
    return render(request, 'clients.html')