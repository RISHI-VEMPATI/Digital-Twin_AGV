from ultralytics import YOLO
import cv2
import pyrealsense2 as rs
import numpy as np
import math 

# Initialize RealSense pipeline
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 15)  # Increased frame rate for depth
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 15)  # Increased frame rate for color

# Align the depth frame to the color frame
align_to = rs.stream.color
align = rs.align(align_to)

# Start the RealSense pipeline
pipeline.start(config)

# YOLO model
model = YOLO("yolo-Weights/yolov8m.pt")

# Object classes
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"]

# Index of 'bottle' in the classNames list
bottle_class_index = 39

try:
    while True:
        print("Waiting for frames...")
        # Get frames from the RealSense camera
        frames = pipeline.wait_for_frames(1000)  # Add a timeout of 1000 ms
        if not frames:
            print("Frame timeout, no frames received.")
            continue

        # Align the frames
        aligned_frames = align.process(frames)

        # Extract color and depth frames
        color_frame = aligned_frames.get_color_frame()
        depth_frame = aligned_frames.get_depth_frame()

        if not color_frame or not depth_frame:
            print("Color or depth frame not received.")
            continue

        # Convert frames to numpy arrays
        color_image = np.asanyarray(color_frame.get_data())
        depth_image = np.asanyarray(depth_frame.get_data())

        # Run YOLO model on the color image
        results = model(color_image, stream=True)

        # Coordinates and processing results
        for r in results:
            boxes = r.boxes

            for box in boxes:
                # Class name
                cls = int(box.cls[0])

                # Only process if it's a 'bottle' (class index 39)
                if cls == bottle_class_index:
                    # Bounding box
                    x1, y1, x2, y2 = box.xyxy[0]
                    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert to int values
                    x = (x1 + x2) // 2
                    y = (y1 + y2) // 2

                    # Draw bounding box
                    cv2.rectangle(color_image, (x1, y1), (x2, y2), (255, 0, 255), 3)

                    # Confidence
                    confidence = math.ceil((box.conf[0] * 100)) / 100
                    print(f"Confidence ---> {confidence}")

                    # Add label to the image
                    org = (x1, y1 - 10)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    fontScale = 0.7
                    color = (255, 0, 0)
                    thickness = 2
                    radius = 1
                    cv2.putText(color_image, f'Bottle {confidence}', org, font, fontScale, color, thickness)
                    cv2.putText(color_image, f'x: {int(x)}, y: {int(y)}', (int(x), int(y)), font, fontScale, color, thickness)
                    cv2.putText(color_image, f'x1: {x1}, y1: {y1}', (x1, y1 - 30), font, fontScale, color, thickness)
                    cv2.putText(color_image, f'x2: {x2}, y2: {y2}', (x2, y2 + 30), font, fontScale, color, thickness)
                    cv2.circle(color_image, (int(x), int(y)), radius, color, thickness)

                    # Get depth information (at the center of the bounding box)
                    depth = depth_frame.get_distance(int(x), int(y))
                    if depth >= 0:  # Check if depth is valid
                        depth_cm = int(depth * 100)  # Convert meters to centimeters
                        cv2.putText(color_image, f'z: {depth_cm}', (int(x - 100), int(y)), font, fontScale, color, thickness)
                        print(f"Depth at center of bottle: {depth_cm} cm")
                    else:
                        cv2.putText(color_image, "Invalid depth", (int(x - 100), int(y)), font, fontScale, color, thickness)
                        print("Invalid depth at center of bottle.")

        # Show color image with detections
        cv2.imshow('RealSense Color Image - Bottles Only', color_image)

        # Display the depth image for debugging
        # depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)
        # cv2.imshow('Depth Image', depth_colormap)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break

finally:
    # Stop the pipeline
    pipeline.stop()
    cv2.destroyAllWindows()
