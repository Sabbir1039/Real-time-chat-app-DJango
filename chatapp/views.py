from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib import messages
from .models import Room, Message

def custom_404(request, *args, **kwargs):
    return render(request, "chatapp/404.html", status=404)

def home(request):
    user = request.user
    if user.is_authenticated:
        rooms = Room.objects.all().order_by('-created_at')
        context = {
            "rooms": rooms
        }
        return render(request, "chatapp/home.html", context)
    else:
        return redirect('login')

def room(request, room_name):
    user = request.user
    if user.is_authenticated:
        room = Room.objects.filter(name=room_name).first()
        if not room:
            messages = None   
        else:
            messages = Message.objects.filter(room=room).order_by('timestamp')
        
        return render(request, "chatapp/room.html", {
            "room_name": room_name,
            "messages": messages
        })
    else:
        return redirect('login')
    
def delete_room(request, room_id):
    room = Room.objects.get(id=room_id)
    if room:
        room.delete()
        return redirect('home')
    else:
        messages.error(request,'Error! Can not delete room. Try agin!')
        return redirect('home')