from django.urls import path

from .client import PracticeConsumer

websocket_urlpatterns = [
    path('practise/', PracticeConsumer.as_asgi()),
]
