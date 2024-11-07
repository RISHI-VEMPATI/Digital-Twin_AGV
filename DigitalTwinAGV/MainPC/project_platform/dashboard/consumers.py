import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Schedule
from asgiref.sync import sync_to_async

class JobUpdateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("job_updates_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("job_updates_group", self.channel_name)

    async def send_job_update(self, event):
        # Fetch the latest job data
        jobs = await sync_to_async(list)(Schedule.objects.all().values())
        
        # Send data to the WebSocket
        await self.send(text_data=json.dumps({
            "type": "job_update",
            "jobs": jobs
        }))
