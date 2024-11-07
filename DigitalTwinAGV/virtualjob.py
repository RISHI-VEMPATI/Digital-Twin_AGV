import numpy as np
import time
import socket
import json

ip_address = "10.14.2.227"
port = 3083

# Parameters for the job generation process
average_interval = 10  # Average time between job arrivals in seconds
locations = ['A', 'B', 'C', 'D', 'E']
a = 0
lambda_value = 3

class VirtualJob:
    def __init__(self, job_id, location):
        self.job_id = job_id
        self.location = location

def generate_job(i):
    """Generates a job with a unique ID and location."""
    job_id = f"JOB {i}"
    location_index = np.random.poisson(lambda_value) % len(locations)
    location = locations[location_index]
    return job_id, location

def send_job_to_server(s, job):
    """Sends the generated job to the socket server."""
    job_data = json.dumps(job.__dict__)  # Convert job to JSON format
    s.sendall(job_data.encode('utf-8'))  # Send the job data

def simulate_job_generation(total_time=10000):  # Adjust total_time as needed
    """Simulates job generation over a given time period."""
    global a
    current_time = 0
    
    # Establish a single socket connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip_address, port))
        print("Connected to server.")
        
        while current_time < total_time:
            # Time interval between job arrivals follows an exponential distribution
            time_interval = np.random.exponential(average_interval)
            current_time += time_interval
            a += 1
            if current_time < total_time:
                job_id, location = generate_job(a)
                job = VirtualJob(job_id, location)
                print(f"Time: {current_time:.2f} seconds, Generated Job ID: {job.job_id}, Location: {job.location}")
                send_job_to_server(s, job)  # Send the job to the server
                time.sleep(time_interval)

# Run the simulation for a specified duration
simulate_job_generation(total_time=10000)  # Change 'total_time' as needed
