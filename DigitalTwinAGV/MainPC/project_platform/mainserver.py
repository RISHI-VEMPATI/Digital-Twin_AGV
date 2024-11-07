import socket
import os
import threading
import json
import django
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

# Set up Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_platform.settings")
django.setup()

from dashboard.models import Schedule

def send_job_to_websocket(job_data):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'job_updates_group',
        {
            'type': 'send_job_update',
            'job_id': job_data['job_id'],
            'location': job_data['location']
        }
    )

def save_job_to_db(virtual_job):
    """Save the job data into the Django database."""
    try:
        job = Schedule(job_name=virtual_job['job_id'], pick_at=virtual_job['location'], place_at='P')
        job.save()
        print(f"Job saved to DB: {job.job_name} at {job.pick_at}")
    except Exception as e:
        print(f"Error saving job to DB: {e}")

def handle_client(client_socket):
    """Handles communication with a connected client."""
    try:
        while True:
            job_data = client_socket.recv(4096)
            if not job_data:
                print("Connection closed by client.")
                break

            job = job_data.decode('utf-8')
            try:
                virtual_job = json.loads(job)
                save_job_to_db(virtual_job)
                send_job_to_websocket(virtual_job)
                print(f"Received Job ID: {virtual_job['job_id']}, Location: {virtual_job['location']}")
            except json.JSONDecodeError:
                print("Received invalid JSON data.")
        
    except Exception as e:
        print(f"Error occurred while handling client: {e}")
    
    finally:
        client_socket.close()
        print("Client connection closed.")

def start_server(ip_address, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip_address, port))
    server.listen(5)
    print(f"Server listening on {ip_address}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.daemon = True
        client_handler.start()

if __name__ == "__main__":
    start_server("10.14.2.227", 3083)
