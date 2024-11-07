from pyrplidar import PyRPlidar
import time

# Define the parameters for obstacle detection
TARGET_ANGLE = 90  # Target angle in degrees (adjust as needed)
ANGLE_THRESHOLD = 2  # Allowable deviation from target angle in degrees
DISTANCE_THRESHOLD = 500  # Distance threshold in mm (500 mm = 50 cm)

def detect_obstacle_at_angle():
    lidar = PyRPlidar()
    lidar.connect(port="/dev/ttyUSB0", baudrate=115200, timeout=3)
    # Linux   : "/dev/ttyUSB0"
    # MacOS   : "/dev/cu.SLAB_USBtoUART"
    # Windows : "COM5"

    lidar.set_motor_pwm(500)
    time.sleep(2)  # Allow time for the motor to stabilize

    scan_generator = lidar.force_scan()  # Start scanning

    try:
        print("Scanning for obstacles... Press Ctrl+C to stop.")
        
        for count, scan in enumerate(scan_generator):
            for (quality, angle, distance) in scan:
                # Check if the angle is within the target range
                if TARGET_ANGLE - ANGLE_THRESHOLD <= angle <= TARGET_ANGLE + ANGLE_THRESHOLD:
                    if distance < DISTANCE_THRESHOLD:
                        print(f"Obstacle detected! Distance: {distance}mm, Angle: {angle} degrees")
                    else:
                        print(f"No obstacle at target angle. Distance: {distance}mm, Angle: {angle} degrees")
            
            time.sleep(0.1)  # Adjust delay between scans if necessary
            if count == 20:  # Limit the scan to 20 iterations for demonstration
                break

    except KeyboardInterrupt:
        print("Scan interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Stop motor and disconnect lidar
        lidar.stop()
        lidar.set_motor_pwm(0)
        lidar.disconnect()

if __name__ == "__main__":
    detect_obstacle_at_angle()
