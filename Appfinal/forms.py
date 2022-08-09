from django import forms

class Formulario_clientes(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()