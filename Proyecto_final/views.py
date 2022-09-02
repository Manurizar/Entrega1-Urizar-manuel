from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime 
from django.template import loader

def dia(request):
    return HttpResponse(f"La fecha de hoy es {datetime.datetime.now()}")


def inicio(request):
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(user=request.user).first()
        return render(request, 'Appfinal/inicio_logueado.html', {"url":avatar.imagen.url})
    else:
        return render(request, 'Appfinal/inicio_logueado.html')
