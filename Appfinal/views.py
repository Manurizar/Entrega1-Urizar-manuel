from django.shortcuts import render
from django.http import HttpResponse
from Appfinal.forms import *
from Appfinal.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def cliente(request):

    return render(request, 'Appfinal/cliente.html')

def local(request):

    return render(request, 'Appfinal/local.html')

def transaccion(request):

    return render(request, 'Appfinal/transaccion.html')

def formulario(request):

    return render(request, 'Appfinal/formulario.html')

def formulario_cliente(request):

    if request.method == "POST":

        mi_formulario = Formulario_clientes(request.POST)
        
        print(mi_formulario)
        
        if mi_formulario.is_valid:
            
            informacion = mi_formulario.cleaned_data
            
            cliente_3 = Cliente(nombre_cliente=informacion["nombre"], email=informacion["email"])
            
            cliente_3.save()
            
            return render(request, 'Appfinal/formulario_cliente_cargado.html')
    
    else:
        return render(request, 'Appfinal/formulario_cliente.html')

def formulario_producto(request):

    if request.method == "POST":

        mi_formulario = Formulario_producto(request.POST)
        
        print(mi_formulario)
        
        if mi_formulario.is_valid:
            
            informacion = mi_formulario.cleaned_data
            
            producto_a_crear = producto(nombre_producto=informacion["nombre_producto"], precio=informacion["precio"], stock=informacion["stock"])
            
            producto_a_crear.save()
            
            return render(request, 'Appfinal/formulario_producto_cargado.html')
    
    else:

        formularioProducto = Formulario_producto()

    return render(request, 'Appfinal/formulario_producto.html', {"formularioProducto":formularioProducto})

clientes_lista = dir(Cliente)

def buscarcliente(request):

    return render(request, 'Appfinal/busqueda_cliente.html')

def buscar(request):


    respuesta = request.GET.get("nombre")

    respuesta_lista = Cliente.objects.filter(nombre_cliente__icontains = respuesta)

    return render(request, 'Appfinal/busqueda_finalizada.html', {"nombre": respuesta_lista})

def lista_productos(request):
        lista = producto.objects.all()
        contexto = {"lista":lista}
        return render(request, 'Appfinal/productos.html', contexto)

def eliminarProductos(request, id_producto):

    try:
        producto_a_buscar = producto.objects.get(nombre_producto=id_producto)

        producto_a_buscar.delete()

        lista = producto.objects.all()
        
        contexto = {"lista":lista}
        
        return render(request, 'Appfinal/productos.html', contexto)
    except:
        return HttpResponse("Este producto no existe")

def modificarProducto(request, id_producto):
    
    if request.method == "GET":

        formulario = Formulario_producto()
        
        return render(request, 'Appfinal/actualizar_productos.html', {"formulario":formulario})

    else:

        formulario = Formulario_producto(request.POST)

        if formulario.is_valid():

            data = formulario.cleaned_data

            producto_a_modificar = producto.objects.get(nombre_producto=id_producto)

            producto_a_modificar.nombre_producto = data["nombre_producto"]

            producto_a_modificar.precio = data["precio"]

            producto_a_modificar.stock = data["stock"]

            producto_a_modificar.save()

            return render(request, 'Appfinal/formulario_producto_cargado.html') 
            

class Lista_empleados(ListView):
    model = empleado
    template_name = 'Appfinal/empleado_lista.html'

class Detalle_empleado(DetailView):
    model = empleado
    template_name = 'Appfinal/empleado_detalle.html'

class Crear_empleado(CreateView):
    model = empleado
    success_url = 'empleado_lista'
    fields = ['nombre_empleado', 'email', 'puesto']

class Modificar_empleado(UpdateView):
    model = empleado
    success_url = '/Appfinal/empleado_lista'
    fields = ['nombre_empleado', 'email', 'puesto']

class Eliminar_empleado(DeleteView):
    model = empleado
    success_url = '/Appfinal/empleado'
    
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
