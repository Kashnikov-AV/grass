from django.contrib import admin
from chat_app.models import ChatModel, UserChatProfileModel, ChatNotification

# Register your models here.

admin.site.register(ChatModel)
admin.site.register(UserChatProfileModel)
admin.site.register(ChatNotification)