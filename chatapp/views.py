from django.shortcuts import render, redirect
from django.views.generic import TemplateView

def index(request):
    user = request.user
    if user.is_authenticated:
        return render(request, "chatapp/index.html")
    else:
        return redirect('login')

def room(request, room_name):
    return render(request, "chatapp/room.html", {"room_name": room_name})