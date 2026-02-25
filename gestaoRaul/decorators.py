from django.urls import reverse
from django.http import HttpResponseForbidden, HttpResponseRedirect



def group_required(groupName):
    def decorator(view_function):
        def wrapper(request, *args, **kwargs):
            if request.user != None:
                if request.user.is_authenticated:
                    if request.user.groups.filter(name=groupName).exists():
                        return view_function(request, *args, **kwargs)
                    else:
                        return HttpResponseForbidden('tu nao tem acesso rapa')
                else:
                    return  HttpResponseRedirect(reverse('login'), status=302)
            else:
                print(f"Erro no decorator: usuario none")
                return HttpResponseRedirect(reverse('login'), status=302)
        return wrapper
    return decorator
   
