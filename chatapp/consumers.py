# chatapp/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth import get_user_model
from asgiref.sync import sync_to_async
from .models import Room, Message

User = get_user_model()

class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        # extracts the room_name from the URL route parameters
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # Creating a unique group name for the room
        self.room_group_name = f'chat_{self.room_name}'
        
        # Check if the room exists, if not create it
        self.room, created = await sync_to_async(Room.objects.get_or_create)(name=self.room_name)
        
        print("*****Connected")
        print(self.scope['user'])
        
        if self.scope['user'].is_authenticated:
            # Add the channel (WebSocket connection) to the group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name # Unique identifier for the WebSocket connection
            )
            # Accept the WebSocket connection
            await self.accept()
        else:
            await self.close()
        

    async def disconnect(self, close_code):
        # Remove the channel from the group on disconnect
        print("*****disconnected")
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        # Receive a message from the WebSocket
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        username = text_data_json["username"]
        
        user = await sync_to_async(User.objects.get)(username=username)
        
        # Save the message to the database
        await sync_to_async(Message.objects.create)(
            room=self.room,
            user=user,
            content=message
        )

        # Send the message to the group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chatroom_message',
                'message': message,
                'username': username,
            }
        )
    
    async def chatroom_message(self, event):
        message = event['message']
        username = event['username']
        
        await self.send(text_data=json.dumps({
            'message': message,
            'username': username,
        }))