from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/job_updates/', consumers.JobUpdateConsumer.as_asgi()),
]
