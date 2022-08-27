from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=40)
    email = models.EmailField()
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Nombre: {self.nombre_cliente} - Email de contacto: {self.email}"

class empleado(models.Model):

    nombre_empleado = models.CharField(max_length=40)
    email = models.EmailField()
    puesto = models.CharField(max_length=40)
    fecha_de_contratacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Nombre del empleado: {self.nombre_empleado} - email: ${self.email} - puesto: {self.puesto}"

class producto(models.Model):
    nombre_producto = models.CharField(max_length=40)
    precio = models.IntegerField() 
    stock = models.IntegerField() 
    fecha_de_creacion = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Nombre del producto: {self.nombre_producto} - Precio: ${self.precio} - Stock disponible: {self.stock}"

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)