from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:room_name>/", views.room, name="room"),
    path("delete/<int:room_id>/", views.delete_room, name="room-delete"),
]