from django.shortcuts import render
from django.views.generic import TemplateView

def index(request):
    return render(request, "chatapp/index.html")

def room(request, room_name):
    return render(request, "chatapp/room.html", {"room_name": room_name})