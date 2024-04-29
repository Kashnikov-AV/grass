from django.apps import AppConfig


class ChatAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'chat_app'


    def ready(self) -> None:
        from chat_app import signals

