from django.utils.decorators import method_decorator
from django.http import HttpResponseForbidden, HttpResponseRedirect


def group_required(groupName):
    def decorator(view_function):
        def wrapper(request, *args, **kwargs):
            if request.user.is_authenticated:
                if request.user.groups.filter(name=groupName).exists():
                    return view_function(request, *args, **kwargs)
                else:
                    return HttpResponseForbidden('tu nao tem acesso rapa')
            else:
                return HttpResponseForbidden('Direcionar para tela de login aqui')
        return wrapper
    return decorator
   
