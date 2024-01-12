from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
from chat_app.models import ChatModel

# Create your views here.
User = get_user_model()

@login_required
def chat(request):
    users = User.objects.exclude(email=request.user.email)[0:5]
    return render(request, "chat_app/chat.html", context={'users': users})


def chatPage(request, email):
    user_obj = User.objects.get(email=email)
    users = User.objects.exclude(email=request.user.email)[0:5]

    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'
    message_objs = ChatModel.objects.filter(thread_name=thread_name)
    return render(request, 'chat_app/chat-page.html', context={'user': user_obj, 'users': users, 'messages': message_objs})
