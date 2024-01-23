from django.db import models
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async


# Create your models here.
class Room(models.Model):
    class Meta:
        ordering = ['pk']

    room_name = models.CharField(max_length=150, unique=True, verbose_name='room name')
    users = models.ManyToManyField(get_user_model(), related_name='rooms')

    @classmethod
    @sync_to_async
    def add(cls, room_name, user):
        room, created = cls.objects.get_or_create(room_name=room_name)
        room.users.add(user)
        return created # sockets => join or create

    @classmethod
    @sync_to_async
    def users_count(cls, room_name):
        rooms = cls.objects.filter(room_name=room_name)
        if rooms.exists():
            return rooms.first().users.count()
        return 0

    @classmethod
    @sync_to_async
    def remove_user(cls, user, room_name):
        room = cls.objects.filter(room_name=room_name)
        if room.exists():
            room.users.remove(user)

    def __str__(self) -> str:
        return self.room_name


class UserChatProfileModel(models.Model):
    class Meta:
        ordering = ['pk']

    user_model = get_user_model()
    user = models.OneToOneField(to=user_model, on_delete=models.CASCADE, verbose_name='user')
    online_status = models.BooleanField(default=False, verbose_name='online status')

    def __str__(self) -> str:
        if not self.user.role:
            return str(self.user.pk) + ' ' + self.user.email + ' ' + self.user.profile.surname
        else:
            return str(self.user.pk) + ' ' + self.user.email + ' ' + self.user.company.company_name


class ChatModel(models.Model):
    class Meta:
        ordering = ['pk']

    sender = models.CharField(max_length=100, default=None)
    message = models.TextField(null=True, blank=True)
    thread_name = models.CharField(null=True, blank=True, max_length=50)
    room = models.ForeignKey(to=Room, on_delete=models.CASCADE,  verbose_name='room')
    timestamp = models.DateTimeField(auto_now_add=True)



    def __str__(self) -> str:
        return self.message


class ChatNotification(models.Model):
    class Meta:
        ordering = ['pk']

    user_model = get_user_model()

    chat = models.ForeignKey(to=ChatModel, on_delete=models.CASCADE)
    user = models.ForeignKey(to=user_model, on_delete=models.CASCADE)
    is_seen = models.BooleanField(default=False)



    def __str__(self) -> str:
        return self.user.email