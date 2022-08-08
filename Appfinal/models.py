from django.db import models

# Create your models here.
class cliente(models.Model):
    nombre = models.CharField(max_length=40)
    cant_transacciones = models.IntegerField() 

class empleado(models.Model):
    nombre = models.CharField(max_length=40)
    salario = models.IntegerField() 
    email = models.EmailField()

class local(models.Model):
    calle = models.CharField(max_length=40)
    encargado = models.CharField(max_length=40)
    abierto = models.BooleanField()
    
class transaccion(models.Model):
    N_de_transaccion = models.IntegerField() 
    fecha_transaccion = models.DateField()
    valor = models.IntegerField() 