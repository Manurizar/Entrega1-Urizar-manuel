from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    email = models.EmailField()

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