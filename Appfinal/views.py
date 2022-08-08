from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cliente(request):

    return render(request, 'Appfinal/cliente.html')

def empleado(request):

    return render(request, 'Appfinal/empleado.html')

def local(request):

    return render(request, 'Appfinal/local.html')

def transaccion(request):

    return render(request, 'Appfinal/transaccion.html')