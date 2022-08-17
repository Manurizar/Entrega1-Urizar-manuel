from django.urls import path
from Appfinal import views

urlpatterns = [


    path('cliente/', views.Lista_clientes.as_view(), name="clienteInicio"),
    path('detalle_cliente/<pk>', views.Detalle_cliente.as_view(), name="clienteDetalle"),
    path('crear_cliente/', views.Crear_cliente.as_view(), name="clienteCrear"),
    path('modificar_cliente/<pk>', views.Modificar_cliente.as_view(), name="clienteModificar"),
    path('eliminar_cliente/<pk>', views.Eliminar_cliente.as_view(), name="clienteEliminar"),
    path('busqueda_cliente/', views.buscarcliente),
    path('buscar_cliente/', views.buscar),

    path('empleado/', views.Lista_empleados.as_view(), name="empleadoInicio"),
    path('crear_empleado/', views.Crear_empleado.as_view(), name="empleadoCrear"),
    path('detalle_empleado/<pk>', views.Detalle_empleado.as_view(), name="empleadoDetalle"),
    path('modificar_empleado/<pk>', views.Modificar_empleado.as_view(), name="empleadoModificar"),
    path('eliminar_empleado/<pk>', views.Eliminar_empleado.as_view(), name="empleadoEliminar"),

    path('producto/', views.Lista_productos.as_view(), name="productoInicio"),
    path('detalle_producto/<pk>', views.Detalle_producto.as_view(), name="productoDetalle"),
    path('crear_producto/', views.Crear_producto.as_view(), name="productoCrear"),
    path('modificar_producto/<pk>', views.Modificar_producto.as_view(), name="productoModificar"),
    path('eliminar_producto/<pk>', views.Eliminar_producto.as_view(), name="productoEliminar"),

    path('local/', views.local),

    path('transaccion/', views.transaccion),

    

]