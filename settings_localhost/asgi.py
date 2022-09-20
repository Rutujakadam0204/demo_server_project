"""
ASGI config for bms project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import apps.widget.routing
import apps.project_mgmt_basic.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings_localhost.settings_prod')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(
        apps.widget.routing.websocket_urlpatterns+apps.project_mgmt_basic.routing.websocket_urlpatterns
    ))
    # "websocket": AuthMiddlewareStack(URLRouter(apps.widget.routing.websocket_urlpatterns)),
    # "websocket": AuthMiddlewareStack(URLRouter(apps.project_mgmt_basic.routing.websocket_urlpatterns))
})
