from django.urls import path
from Appfinal import views
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
 

urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),


    path('cliente/', views.Lista_clientes.as_view(), name="clienteInicio"),
    path('detalle_cliente/<pk>', views.Detalle_cliente.as_view(), name="clienteDetalle"),
    path('crear_cliente/', views.Crear_cliente.as_view(), name="clienteCrear"),
    path('modificar_cliente/<pk>', views.Modificar_cliente.as_view(), name="clienteModificar"),
    path('eliminar_cliente/<pk>', views.Eliminar_cliente.as_view(), name="clienteEliminar"),
    path('busqueda_cliente/', views.buscarCliente, name="busquedaCliente"),
    path('busqueda_cliente_finalizada/', views.buscarClienteResultado, name="busquedaClienteFinalizada"),

    path('empleado/', views.Lista_empleados.as_view(), name="empleadoInicio"),
    path('crear_empleado/', views.Crear_empleado.as_view(), name="empleadoCrear"),
    path('detalle_empleado/<pk>', views.Detalle_empleado.as_view(), name="empleadoDetalle"),
    path('modificar_empleado/<pk>', views.Modificar_empleado.as_view(), name="empleadoModificar"),
    path('eliminar_empleado/<pk>', views.Eliminar_empleado.as_view(), name="empleadoEliminar"),
    path('busqueda_Empleado/', views.buscarEmpleado, name="busquedaEmpleado"),
    path('busqueda_Empleado_finalizada/', views.buscarEmpleadoResultado, name="busquedaEmpleado"),

    path('productoInicio/', views.Lista_producto_no_logueado.as_view(), name="productos_no_logueado"), 
    path('producto/', views.Lista_productos.as_view(), name="productoInicio"),
    path('detalle_producto/<pk>', views.Detalle_producto.as_view(), name="productoDetalle"),
    path('crear_producto/', views.Crear_producto.as_view(), name="productoCrear"),
    path('modificar_producto/<pk>', views.Modificar_producto.as_view(), name="productoModificar"),
    path('eliminar_producto/<pk>', views.Eliminar_producto.as_view(), name="productoEliminar"),
    path('busqueda_producto/', views.buscarProducto, name="busquedaProducto"),
    path('busqueda_producto_finalizada/', views.buscarProductoResultado, name="busquedaProducto"),

    path('local/', views.local),

    

    path('login/', views.login_request, name="login"),
    path('registrarse/', views.registro, name="registro"),
    path('logout/', LogoutView.as_view(template_name='Appfinal/logout.html'), name = 'Logout'),

    path('usuarios/', views.Lista_usuarios.as_view(), name="usuarioInicio"),
    path('detalle_usuario/<pk>', views.Detalle_usuarios.as_view(), name="usuarioDetalle"),
    path('crear_usuario/', views.Crear_usuario.as_view(), name="usuarioCrear"),
    path('modificar_usuario/<pk>', views.Modificar_usuario.as_view(), name="usuarioModificar"),
    path('eliminar_usuario/<pk>', views.Eliminar_usuario.as_view(), name="usuarioEliminar"),
    path('agregaravatar/', views.agregarAvatar, name="agregarAvatar"),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)