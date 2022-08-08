from django.http import HttpResponse
from django.template import Template, Context
from datetime import datetime 
from django.template import loader

def dia(request):
    return HttpResponse(f"La fecha de hoy es {datetime.datetime.now()}")

def plantilla(self):

    plantilla = loader.get_template("Plantilla1.html")

    documento = plantilla.render()

    return HttpResponse(documento)

