from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class Formulario_clientes(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()

class Formulario_producto(forms.Form):
    nombre_producto = forms.CharField(max_length=40)
    precio = forms.IntegerField() 
    stock = forms.IntegerField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k:"" for k in fields}

class Avatarformulario(forms.Form):
    imagen = forms.ImageField(required=True)