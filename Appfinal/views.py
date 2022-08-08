from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cliente(request):

    return render(request, 'Appfinal/cliente.html', {"mensaje":"BOKITA"})
