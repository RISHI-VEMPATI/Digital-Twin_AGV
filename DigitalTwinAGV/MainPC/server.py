import json
import socket
import threading
import time
import os
import sys

# Get the parent directory
parent_dir = os.getcwd()
# Add the Server directory to the path
sys.path.append(os.path.join(parent_dir, 'Server'))
from BaseLibraries.messaging import flatten, unflatten
from BaseLibraries.messaging import dummyFIPA
# Get the current directory path
parent_dir = os.getcwd()

# Use os.path.join() for cross-platform compatibility
with open(os.path.join(parent_dir, 'server_ip.txt')) as f:
    lines = f.readlines()
    port = int(lines[0].strip())  # Get port from the first line
    host = lines[1].strip()  # Get host from the second line

# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()  # Start listening for connections

clients = []  # List to store connected clients
agent_ids = []  # List to store agent IDs

# Function to broadcast message to all clients
def broadcast(message):
    for client in clients:
        client.sendall(message)

# Function to forward messages to specific receivers
def forward_to_receivers(message):
    msg = unflatten(message)
    print(f"sending {msg.performative} from {msg.sender} to {int(msg.receiver)}")
    if msg.protocol != "DUMMY_FIPA":
        try:
            # For multiple receivers
            for n_name in eval(int(msg.receiver)):
                agentid_index = agent_ids.index(n_name)
                clients[agentid_index].sendall(message)
                time.sleep(0.5)
        except:
            # For a single receiver
            agentid_index = agent_ids.index(int(msg.receiver))
            clients[agentid_index].sendall(message)
            time.sleep(0.5)

# Function to handle each client connection
def handle(client):
    print("initial tasks done")
    while True:
        try:
            message = client.recv(1024)
            if len(message) > 0:
                msg = bytes(message)
                while len(message) > 1023:
                    message = client.recv(1024)
                    msg += message

                msg = unflatten(msg)
                print(msg)

                if msg.content == "platform_disconnection":
                    print('hel')
                    try:
                        index = clients.index(client)
                        agent_id = agent_ids[index]
                        broadcast(flatten(dummyFIPA("client_disconnected", agent_id)))
                        print(f"{agent_id} got disconnected")
                        while True:
                            index = agent_ids.index(agent_id)
                            client = clients[index]
                            agent_ids.remove(agent_id)
                            clients.remove(client)
                            client.close()
                            print(clients)
                    except:
                        break
                else:
                    msg = flatten(msg)
                    forward_to_receivers(msg)

        except:
            # Handle client disconnection
            index = clients.index(client)
            agent_id = agent_ids[index]
            print(f"{agent_id} got disconnected")
            agent_ids.remove(agent_id)
            clients.remove(client)
            client.close()
            break

# Function to receive new client connections
def recieve():
    print("server is listening...")
    while True:
        client, address = server.accept()
        print(f"connected with {str(address)}")

        # Ask the client for its agent ID
        client.sendall(flatten(dummyFIPA("server_topics", 'NICK')))
        agent_id = unflatten(client.recv(1024)).content
        print(agent_id)

        # Store the agent ID and client
        agent_ids.append(agent_id)
        clients.append(client)
        client.sendall(flatten(dummyFIPA("active_agents", agent_ids)))

        # Notify other clients of the new connection
        print(f"name of the client is {agent_id}")
        broadcast(flatten(dummyFIPA("client_connected", agent_id)))

        # Start a new thread to handle the client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

# Uncomment the line below to start the server
# recieve()
