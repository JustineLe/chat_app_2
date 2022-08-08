from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room, Message


# Create your views here.
@login_required(login_url='login/')
def room(request):
    chat_room = Room.objects.all()

    return render(request, 'room/rooms.html', {
        'rooms': chat_room,
    })


@login_required(login_url='login/')
def room_detail(request, slug):
    detail_room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=detail_room)

    return render(request, 'room/detail_room.html', {
        'detail_room': detail_room,
        'messages': messages,
    })
