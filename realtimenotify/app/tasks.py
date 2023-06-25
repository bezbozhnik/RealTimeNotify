from celery import shared_task
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from models import Notification
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@shared_task
def send_notification(notification_id):
    try:
        notification = Notification.objects.get(id=notification_id)
        # Здесь можно выполнить необходимую логику отправки уведомления, например, отправить его через WebSocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"notifications_{notification.user.id}",  # Имя группы WebSocket, соответствующей пользователю
            {"type": "notification.message", "message": notification.message}  # Отправка сообщения через WebSocket
        )
        notification.sent_at = timezone.now()
        notification.save()
    except ObjectDoesNotExist:
        pass
