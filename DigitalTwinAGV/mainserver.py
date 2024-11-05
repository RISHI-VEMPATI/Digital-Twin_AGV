import socket
import threading
import json

def handle_client(client_socket):
    """Handles communication with a connected client."""
    while True:
        try:
            # Receive job data from the socket
            job_data = client_socket.recv(1024)
            if not job_data:
                print("Connection closed by client.")
                break  # Connection closed by client
            
            job = job_data.decode('utf-8')
            virtual_job = json.loads(job)  # Attempt to decode the JSON
            
            # Print the received job information
            print(f"Received Job ID: {virtual_job['job_id']}, Location: {virtual_job['location']}")
        
        except json.JSONDecodeError:
            print("Received invalid JSON data.")
        except Exception as e:
            print(f"Error occurred: {e}")
            break
    
    client_socket.close()
    print("Client connection closed.")

def start_server(ip_address, port):
    """Starts the socket server to listen for clients."""
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip_address, port))
    server.listen(5)
    print(f"Server listening on {ip_address}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.daemon = True  # Allows the program to exit even if threads are running
        client_handler.start()

# Start the server
if __name__ == "__main__":
    start_server("10.14.1.147", 3083)  # Listen on all interfaces
