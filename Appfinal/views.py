from django.shortcuts import render
from django.http import HttpResponse
from Appfinal.forms import *
from Appfinal.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
clientes_lista = dir(Cliente)

def local(request):

    return render(request, 'Appfinal/local.html')

def transaccion(request):

    return render(request, 'Appfinal/transaccion.html')

#MOTOR BUSQUEDA CLIENTE

def buscarcliente(request):

    return render(request, 'Appfinal/busqueda_cliente.html')

def buscar(request):


    respuesta = request.GET.get("nombre")

    respuesta_lista = Cliente.objects.filter(nombre_cliente__icontains = respuesta)

    return render(request, 'Appfinal/busqueda_finalizada.html', {"nombre": respuesta_lista})

#HAY QUE UNIR MOTOR Y CRUD DE CLIENTE

#CRUD EMPLEADO            

class Lista_empleados(ListView):
    model = empleado
    template_name = 'Appfinal/empleado_lista.html'

class Detalle_empleado(DetailView):
    model = empleado
    template_name = 'Appfinal/empleado_detalle.html'

class Crear_empleado(CreateView):
    model = empleado
    success_url = '/Appfinal/empleado'
    fields = ['nombre_empleado', 'email', 'puesto']

class Modificar_empleado(UpdateView):
    model = empleado
    success_url = '/Appfinal/empleado_lista'
    fields = ['nombre_empleado', 'email', 'puesto']

class Eliminar_empleado(DeleteView):
    model = empleado
    success_url = '/Appfinal/empleado'

#CRUD CLIENTE
    
class Lista_clientes(ListView):
    model = Cliente
    template_name = 'Appfinal/cliente_lista.html'

class Detalle_cliente(DetailView):
    model = Cliente
    template_name = 'Appfinal/cliente_detalle.html'

class Crear_cliente(CreateView):
    model = Cliente
    success_url = '/Appfinal/cliente_prueba'
    fields = ['nombre_cliente', 'email']

class Modificar_cliente(UpdateView):
    model = Cliente
    success_url = '/Appfinal/cliente_prueba'
    fields = ['nombre_cliente', 'email']

class Eliminar_cliente(DeleteView):
    model = Cliente
    success_url = '/Appfinal/cliente_prueba'

#CRUD PRODUCTO

class Lista_productos(ListView):
    model = producto
    template_name = 'Appfinal/producto_lista.html'

class Detalle_producto(DetailView):
    model = producto
    template_name = 'Appfinal/producto_detalle.html'

class Crear_producto(CreateView):
    model = producto
    success_url = '/Appfinal/producto'
    fields = ['nombre_producto', 'precio', 'stock']

class Modificar_producto(UpdateView):
    model = producto
    success_url = '/Appfinal/producto'
    fields = ['nombre_producto', 'precio', 'stock']

class Eliminar_producto(DeleteView):
    model = producto
    success_url = '/Appfinal/producto'

#CRUD TRANSACCION

#CRUD LOCAL