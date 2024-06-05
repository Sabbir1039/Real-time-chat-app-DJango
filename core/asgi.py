import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from chatapp.routing import websocket_urlpatterns

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatapp.settings")

django_asgi_app = get_asgi_application()


application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter(websocket_urlpatterns))
        ),
    }
)

# ProtocolTypeRouter
# The ProtocolTypeRouter is a mechanism provided by Django Channels 
# to route different types of connections to different consumers or handlers.

# AuthMiddlewareStack(...):
# This wraps the URLRouter to handle authentication for WebSocket connections.

# AllowedHostsOriginValidator(...):
# This ensures that WebSocket connections come from allowed hosts.
# It's a security measure to prevent WebSocket connections from untrusted sources.

# Initialization of Django settings:
# It ensures that Django's settings are properly configured
# by setting the DJANGO_SETTINGS_MODULE environment variable if it's not already set.
# This is necessary for Django to know which settings module to use.