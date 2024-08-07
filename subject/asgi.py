import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from account.routing import websocket_urlpatterns 
import universitie.routing 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'subject.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            universitie.routing.websocket_urlpatterns
        )
    ),
})