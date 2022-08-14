from django import forms

class Formulario_clientes(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()

class Formulario_producto(forms.Form):
    nombre_producto = forms.CharField(max_length=40)
    precio = forms.IntegerField() 
    stock = forms.IntegerField()