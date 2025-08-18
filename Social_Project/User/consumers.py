from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_consumer"
        self.group_name = "test_consumer_group"

        # Add channel into group
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name)
        # Accepting Connection
        self.accept()
        # Send message to clint
        self.send(json.dumps({"status": "Connected"}))


    def receive(self, text_data):
        print(text_data)
        if text_data:
            data = json.loads(text_data)
            self.send(json.dumps({"message": f"Server receive: {data}"}))

    def disconnect(self):
        print("Disconnected." )