import cv2
import numpy as np

# Initialize the webcam
cap = cv2.VideoCapture(2)  # Use 0 for the default camera or adjust as needed

try:
    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Apply Gaussian blur to reduce noise
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # Threshold the image to detect the black line
        _, threshold = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY_INV)

        # Find contours in the thresholded image
        contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        if contours:
            # Find the largest contour, which should be the line
            largest_contour = max(contours, key=cv2.contourArea)
            M = cv2.moments(largest_contour)
            
            if M["m00"] > 0:
                # Calculate the center of the line
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                # Draw the largest contour and the center point
                cv2.drawContours(frame, [largest_contour], -1, (0, 255, 0), 3)
                cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)

        # Display the frames
        cv2.imshow("Frame", frame)
        cv2.imshow("gray",gray)
        cv2.imshow("Threshold", threshold)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Release the capture and close windows
    cap.release()
    cv2.destroyAllWindows()
