from django.shortcuts import render
from django.http import HttpResponse
from Appfinal.forms import *
from Appfinal.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin  

# Create your views here.
clientes_lista = dir(Cliente)

def inicio(request):
    return render(request, 'Appfinal/inicio_logueado.html')

def local(request):
    a = dir(User)
    
    return render(request, 'Appfinal/local.html', {"a": a})

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

class Lista_empleados(LoginRequiredMixin, ListView):
    model = empleado
    template_name = 'Appfinal/empleado_lista.html'

class Detalle_empleado(LoginRequiredMixin, DetailView):
    model = empleado
    template_name = 'Appfinal/empleado_detalle.html'

class Crear_empleado(LoginRequiredMixin, CreateView):
    model = empleado
    success_url = '/Appfinal/empleado'
    fields = ['nombre_empleado', 'email', 'puesto']

class Modificar_empleado(LoginRequiredMixin, UpdateView):
    model = empleado
    success_url = '/Appfinal/empleado_lista'
    fields = ['nombre_empleado', 'email', 'puesto']

class Eliminar_empleado(LoginRequiredMixin, DeleteView):
    model = empleado
    success_url = '/Appfinal/empleado'

#CRUD CLIENTE
    
class Lista_clientes(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'Appfinal/cliente_lista.html'

class Detalle_cliente(LoginRequiredMixin, DetailView):
    model = Cliente
    template_name = 'Appfinal/cliente_detalle.html'

class Crear_cliente(LoginRequiredMixin, CreateView):
    model = Cliente
    success_url = '/Appfinal/cliente_prueba'
    fields = ['nombre_cliente', 'email']

class Modificar_cliente(LoginRequiredMixin, UpdateView):
    model = Cliente
    success_url = '/Appfinal/cliente_prueba'
    fields = ['nombre_cliente', 'email']

class Eliminar_cliente(LoginRequiredMixin,  DeleteView):
    model = Cliente
    success_url = '/Appfinal/cliente_prueba'

#CRUD PRODUCTO

class Lista_producto_no_logueado(ListView):
    model = producto
    template_name = 'Appfinal/producto_lista_no_logueado.html'

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

#LOGIN

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get("username")

            contraseña = form.cleaned_data.get("password")

            user = authenticate(username=usuario, password=contraseña)

            if user is not None:

                login(request, user)

                return render(request, "Appfinal/inicio_logueado.html", {"mensaje":f"Bienvenido {usuario}"})

            else:

                return render(request, "Appfinal/inicio_logueado.html", {"mensaje":"Datos incorrectos"})

        else:

            return render(request, "Appfinal/inicio_logueado.html", {"mensaje":"Error de formulario"})

    form = AuthenticationForm()
    
    return render(request, 'Appfinal/login.html', {'form':form})

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "Appfinal/producto_lista.html", {"mensaje":"Usuario creado!"})
    else:
        form = UserRegisterForm()
    return render(request, 'Appfinal/registro.html', {'form':form})

#CRUD USUARIOS

class Lista_usuarios(LoginRequiredMixin, ListView):
    model = User
    template_name = 'Appfinal/usuario_lista.html'

class Detalle_usuarios(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'Appfinal/usuario_detalle.html'

class Crear_usuario(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'Appfinal/user_form.html'
    success_url = '/Appfinal/usuarios/'
    fields = ['username', 'email', 'password', 'first_name', 'last_name']

class Modificar_usuario(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'Appfinal/user_form.html'
    success_url = '/Appfinal/usuarios/'
    fields = ['username', 'email', 'first_name', 'last_name']

class Eliminar_usuario(LoginRequiredMixin,  DeleteView):
     model = User
     template_name = 'Appfinal/user_confirm_delete.html'
     success_url = '/Appfinal/usuarios/'
