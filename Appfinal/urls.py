from django.urls import path
from Appfinal import views

urlpatterns = [

    path('cliente/', views.cliente),
    path('empleado/', views.empleado),
    path('local/', views.local),
    path('transaccion/', views.transaccion),
    path('formulario_cliente/', views.formulario_cliente),
    path('formulario_producto/', views.formulario_producto),
    path('busqueda/', views.buscarcliente),
    path('buscar/', views.buscar),
    path('productos/', views.lista_productos),
    path('borrar_productos/<id_producto>', views.eliminarProductos, name="eliminarProducto")
    

]