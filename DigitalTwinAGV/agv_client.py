import socket

def start_client(ip_address, port):
    """Starts the socket client to receive jobs from the server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((ip_address, port))
        while True:
            # Receive job data from the server
            job_data = client.recv(1024)
            if not job_data:
                break
            print(f"Client received Job: {job_data.decode('utf-8')}")

# Start the client
start_client("10.14.1.147", 3083)  # Replace with the server's IP address and port
