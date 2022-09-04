from django.shortcuts import render
from django.http import HttpResponse
from Appfinal.forms import *
from Appfinal.models import *
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin  
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
clientes_lista = dir(Cliente)

#VISTAS SIMPLES

def inicio(request):
    if request.user.is_authenticated:
        try:
            avatar = Avatar.objects.filter(user=request.user.id).last()
            return render(request, 'Appfinal/inicio.html', {"url":avatar.imagen.url})
        except:
            return render(request, 'Appfinal/inicio.html')
    else:
        return render(request, 'Appfinal/inicio.html')

def local(request):
    
    
    return render(request, 'Appfinal/local.html')

def paginas(request):

    return render(request, 'Appfinal/paginas.html')

def about(request):
    return render(request, 'Appfinal/Acerca.html')


#MOTORES BUSQUEDA

def buscarCliente(request):

    return render(request, 'Appfinal/busqueda_cliente.html')

def buscarClienteResultado(request):


    respuesta = request.GET.get("nombre")

    respuesta_lista = Cliente.objects.filter(nombre_cliente__icontains = respuesta)

    return render(request, 'Appfinal/busqueda_cliente_finalizada.html', {"nombre": respuesta_lista})

def buscarProducto(request):

    return render(request, 'Appfinal/busqueda_producto.html')

def buscarProductoResultado(request):


    respuesta = request.GET.get("nombre")

    respuesta_lista = producto.objects.filter(nombre_producto__icontains = respuesta)

    return render(request, 'Appfinal/busqueda_producto_finalizada.html', {"nombre": respuesta_lista})

def buscarEmpleado(request):

    return render(request, 'Appfinal/busqueda_empleado.html')

def buscarEmpleadoResultado(request):


    respuesta = request.GET.get("nombre")

    respuesta_lista = empleado.objects.filter(nombre_empleado__icontains = respuesta)

    return render(request, 'Appfinal/busqueda_empleado_finalizada.html', {"nombre": respuesta_lista})

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
    success_url = '/Appfinal/empleado/'
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
    success_url = '/Appfinal/cliente/'
    fields = ['nombre_cliente', 'email']

class Modificar_cliente(LoginRequiredMixin, UpdateView):
    model = Cliente
    success_url = '/Appfinal/cliente/'
    fields = ['nombre_cliente', 'email']

class Eliminar_cliente(LoginRequiredMixin,  DeleteView):
    model = Cliente
    success_url = '/Appfinal/cliente/'

#CRUD PRODUCTO

class Lista_productos(ListView):
    model = producto
    template_name = 'Appfinal/producto_lista.html'

class Detalle_producto(DetailView):
    model = producto
    template_name = 'Appfinal/producto_detalle.html'

class Crear_producto(LoginRequiredMixin, CreateView):
    model = producto
    success_url = '/Appfinal/producto'
    fields = ['nombre_producto', 'precio', 'stock']

class Modificar_producto(LoginRequiredMixin, UpdateView):
    model = producto
    success_url = '/Appfinal/producto'
    fields = ['nombre_producto', 'precio', 'stock']

class Eliminar_producto(LoginRequiredMixin, DeleteView):
    model = producto
    success_url = '/Appfinal/producto'


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

                return render(request, "Appfinal/inicio.html", {"mensaje":f"Bienvenido {usuario}"})

            else:

                return render(request, "Appfinal/inicio.html", {"mensaje":"Datos incorrectos"})

        else:

            return render(request, "Appfinal/inicio.html", {"mensaje":"Error de formulario"})

    form = AuthenticationForm()
    
    return render(request, 'Appfinal/login.html', {'form':form})

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "Appfinal/inicio.html", {"mensaje":"Usuario creado!"})
    else:
        form = UserRegisterForm()
    return render(request, 'Appfinal/registro.html', {'form':form})

#CRUD USUARIOS

class Lista_usuarios(LoginRequiredMixin, ListView):
    model = User
    template_name = 'Appfinal/usuario_lista.html'

class Detalle_usuarios(LoginRequiredMixin, DetailView):
    model = User
    def get_context_data(self, **kwargs):
        try:
            avatar = Avatar.objects.filter(user=self.object.id).last()
            context = super(Detalle_usuarios, self).get_context_data(**kwargs)
            context = {"url":avatar.imagen.url}
            return context
        except:
            pass
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

@login_required
def agregarAvatar(request):

    if request.method == "POST":
        
        mi_formulario = Avatarformulario(request.POST, request.FILES)
        
        if mi_formulario.is_valid():
            #data = mi_formulario.cleaned_data

            u = User.objects.get(username=request.user)
            
            avatar = Avatar(user=u, imagen=mi_formulario.cleaned_data['imagen'])

            avatar.save()
            
            return render(request, 'Appfinal/inicio.html')
    
    else:
        mi_formulario = Avatarformulario()
    return render(request, 'Appfinal/AgregarAvatar.html', {"mi_formulario":mi_formulario})