from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserChatProfileModel, ChatNotification
import json
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model

user = get_user_model()

@receiver(post_save, sender=user)
def create_chat_profile(sender, instance, created, **kwargs):
    if created:
        p = UserChatProfileModel.objects.create(
            user=instance)
        p.save() # you have correctly passed instance to foreign key and you just need to check condition for the same

@receiver(post_save, sender=ChatNotification)
def send_notification(sender, instance, created, **kwargs):
    if created:
        channel_layer = get_channel_layer()
        notification_obj = ChatNotification.objects.filter(is_seen=False, user=instance.user).count()
        user_id = str(instance.user.id)
        data = {
            'count':notification_obj
        }

        async_to_sync(channel_layer.group_send)(
            user_id, {
                'type':'send_notification',
                'value':json.dumps(data)
            }
        )


@receiver(post_save, sender=UserChatProfileModel)
def send_onlineStatus(sender, instance, created, **kwargs):
    if not created:
        channel_layer = get_channel_layer()
        user = instance.user.username
        user_status = instance.online_status

        data = {
            'username':user,
            'status':user_status
        }
        async_to_sync(channel_layer.group_send)(
            'user', {
                'type':'send_onlineStatus',
                'value':json.dumps(data)
            }
        )