from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth import get_user_model
from chat_app.models import ChatModel, Room

# Create your views here.
User = get_user_model()

@login_required
def chat(request):
    current_user = request.user
    rooms = current_user.rooms.all()
    users_id = set()
    for r in rooms:
        users = r.users.all()
        for u in users:
            print(u.pk)
            users_id.add(u.pk)

    users_list = User.objects.filter(pk__in=list(users_id)).exclude(pk=request.user.pk)
    return render(request, "chat_app/chat.html", context={'users': users_list, 'rooms': rooms})


@login_required
def chatPage(request, email):
    user_obj = User.objects.get(email=email)



    rooms = request.user.rooms.all()
    users_id = set()
    for r in rooms:
        users = r.users.all()
        for u in users:
            print(u.pk)
            users_id.add(u.pk)

    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'

    current_room = Room.objects.get(room_name=thread_name)
    users_list = User.objects.filter(pk__in=list(users_id)).exclude(pk=request.user.pk)

    message_objs = ChatModel.objects.filter(thread_name=thread_name)
    return render(request, 'chat_app/chat-page.html', context={'userobj': user_obj,
                                                               'users': users_list,
                                                               'messages': message_objs,
                                                               'room_obj': current_room
                                                               }
                  )
