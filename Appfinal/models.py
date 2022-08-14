from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre_cliente = models.CharField(max_length=40)
    email = models.EmailField()
    def __str__(self):
        return f"Nombre: {self.nombre_cliente} - Email de contacto: {self.email}"

class empleado(models.Model):
    nombre_empleado = models.CharField(max_length=40)
    email = models.EmailField()
    puesto = models.CharField(max_length=40)

class producto(models.Model):
    nombre_producto = models.CharField(max_length=40)
    precio = models.IntegerField() 
    stock = models.IntegerField() 
    def __str__(self):
        return f"Nombre del producto: {self.nombre_producto} - Precio: ${self.precio} - Stock disponible: {self.stock}"
    
    def lista_productos(request):
        lista = producto.objects.all()
        contexto = {"lista":lista}
        return render(request, 'Appfinal/productos.html', contexto)

class local(models.Model):
    calle = models.CharField(max_length=40)
    encargado = models.CharField(max_length=40)
    abierto = models.BooleanField()
    
class transaccion(models.Model):
    N_de_transaccion = models.IntegerField() 
    fecha_transaccion = models.DateField()
    valor = models.IntegerField() 