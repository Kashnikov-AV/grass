from django.contrib import admin
from chat_app.models import ChatModel, UserChatProfileModel, ChatNotification, Room


# Register your models here.
class RoomAdmin(admin.ModelAdmin):
    model = Room
    list_display = ('pk', 'room_name')


class ChatUserAdmin(admin.ModelAdmin):
    model = UserChatProfileModel
    list_display = ('pk', 'user', 'online_status')


class MessageAdmin(admin.ModelAdmin):
    model = ChatModel
    list_display = ('pk', 'thread_name', 'timestamp', 'message')


admin.site.register(ChatModel, MessageAdmin)
admin.site.register(UserChatProfileModel, ChatUserAdmin)
admin.site.register(ChatNotification)
admin.site.register(Room, RoomAdmin)
