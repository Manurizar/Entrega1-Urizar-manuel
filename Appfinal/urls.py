from django.urls import path
from Appfinal import views

urlpatterns = [

    path('cliente/', views.cliente),
    path('empleado/', views.empleado),
    path('local/', views.local),
    path('transaccion/', views.transaccion),
    path('formulario/', views.info_formulario),
    path('busqueda/', views.buscarcliente),
    path('buscar/', views.buscar)
    

]