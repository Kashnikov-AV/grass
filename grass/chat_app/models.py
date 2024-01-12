from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.

class UserChatProfileModel(models.Model):
    user_model = get_user_model()

    user = models.OneToOneField(to=user_model, on_delete=models.CASCADE)
    name = models.CharField(blank=True, null=True, max_length=100)
    online_status = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.email


class ChatModel(models.Model):
    sender = models.CharField(max_length=100, default=None)
    message = models.TextField(null=True, blank=True)
    thread_name = models.CharField(null=True, blank=True, max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.message


class ChatNotification(models.Model):
    user_model = get_user_model()

    chat = models.ForeignKey(to=ChatModel, on_delete=models.CASCADE)
    user = models.ForeignKey(to=user_model, on_delete=models.CASCADE)
    is_seen = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.email