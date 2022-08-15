from django.urls import path
from Appfinal import views

urlpatterns = [

    path('cliente/', views.cliente),
    path('formulario_cliente/', views.formulario_cliente),
    path('busqueda/', views.buscarcliente),
    path('buscar/', views.buscar),

    path('cliente_prueba/', views.Lista_clientes.as_view(), name="clienteInicio"),
    path('detalle_cliente/<pk>', views.Detalle_cliente.as_view(), name="clienteDetalle"),
    path('crear_cliente/', views.Crear_cliente.as_view(), name="clienteCrear"),
    path('modificar_cliente/<pk>', views.Modificar_cliente.as_view(), name="clienteModificar"),
    path('eliminar_cliente/<pk>', views.Eliminar_cliente.as_view(), name="clienteEliminar"),

    path('empleado/', views.Lista_empleados.as_view()),
    path('crear_empleado', views.Crear_empleado.as_view()),
    path('detalle_empleado/<pk>', views.Detalle_empleado.as_view()),
    path('modificar_empleado/<pk>', views.Modificar_empleado.as_view()),
    path('eliminar_empleado/<pk>', views.Eliminar_empleado.as_view()),

    path('local/', views.local),

    path('transaccion/', views.transaccion),

    
    path('formulario_producto/', views.formulario_producto),
    path('productos/', views.lista_productos),
    path('borrar_productos/<id_producto>', views.eliminarProductos, name="eliminarProducto"),
    path('actualizar_producto/<id_producto>', views.modificarProducto, name="modificarProducto")
    

]