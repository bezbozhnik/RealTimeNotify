from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from .models import Notification

@shared_task
def send_notification(notification_id):
    try:
        notification = Notification.objects.get(id=notification_id)
        # Здесь можно выполнить необходимую логику отправки уведомления, например, отправить его через WebSocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"notifications_123",  # Имя группы WebSocket, соответствующей пользователю
            {"type": "notification_message", "message": notification.message}  # Отправка сообщения через WebSocket
        )
    except ObjectDoesNotExist:
        pass
