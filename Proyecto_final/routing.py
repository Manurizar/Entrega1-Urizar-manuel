from django.core.asgi import get_asgi_application
import os
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
import sendemail.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Proyecto_final.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack((
            URLRouter(
                sendemail.routing.websocket_urlpatterns
            )
        ))
    )
})