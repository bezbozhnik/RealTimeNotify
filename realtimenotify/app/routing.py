from django.urls import re_path
from . import consumer

websocket_urlpatterns = [
    re_path(r'ws/notifications/(?P<user_id>\d+)/$', consumer.NotificationConsumer.as_asgi()),
    # Добавьте другие маршруты WebSocket по мере необходимости
]
