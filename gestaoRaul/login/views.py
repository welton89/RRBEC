from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import AuthenticationForm


def logout_view(request):
    logout(request)
    return redirect('login')


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if  request.user.groups.filter(name='Admin').exists() or  request.user.groups.filter(name='Gerente').exists() :
                    return redirect('home')
                else:
                    return redirect('comandas')
            else:
                pass
                # Mensagem de erro: Credenciais inválidas
        else:
            pass
            # Mensagem de erro: Formulário inválido
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})