"""
ASGI config for Social_Project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from django.urls import path
from channels.auth import AuthMiddlewareStack
from User.consumers import *

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Social_Project.settings')

django_asgi_app = get_asgi_application()

ws_patterns= [
    path('ws/test/',TestConsumer.as_asgi())
]

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(ws_patterns)
    ),
})