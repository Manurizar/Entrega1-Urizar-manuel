from django.shortcuts import render
from django.http import HttpResponse
from Appfinal.forms import Formulario_clientes
from Appfinal.models import *

# Create your views here.
def cliente(request):

    return render(request, 'Appfinal/cliente.html')

def empleado(request):

    return render(request, 'Appfinal/empleado.html')

def local(request):

    return render(request, 'Appfinal/local.html')

def transaccion(request):

    return render(request, 'Appfinal/transaccion.html')

def formulario(request):

    return render(request, 'Appfinal/formulario.html')

def info_formulario(request):

    if request.method == "POST":

        mi_formulario = Formulario_clientes(request.POST)
        
        print(mi_formulario)
        
        if mi_formulario.is_valid:
            
            informacion = mi_formulario.cleaned_data
            
            cliente_3 = Cliente(nombre=informacion["nombre"], email=informacion["email"])
            
            cliente_3.save()
            
            return render(request, 'Appfinal/formulario_cargado.html')
    
    else:
        pass

def buscarcliente(request):

    return render(request, 'Appfinal/busqueda_cliente.html')

def buscar(request):

    respuesta = request.GET.get("nombre")
    return HttpResponse(respuesta)