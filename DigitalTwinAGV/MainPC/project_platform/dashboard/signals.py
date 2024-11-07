from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Schedule
from channels.layers import get_channel_layer

@receiver(post_save, sender=Schedule)
def job_saved(sender, instance, created, **kwargs):
    if created:
        # Notify all WebSocket clients about the new job
        channel_layer = get_channel_layer()
        channel_layer.group_send(
            "job_updates",  # The group name for WebSocket clients
            {
                "type": "send_job_data",  # This triggers the send_job_data method in JobConsumer
            }
        )
