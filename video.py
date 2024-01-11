import cv2
import time

# Open the camera
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Set the video capture properties (adjust as needed)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('example_video.avi', fourcc, 20.0, (640, 480))

# Record video for 5 seconds (adjust as needed)
start_time = time.time()
while time.time() - start_time < 5:
    # Capture a frame
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Could not read frame.")
        break

    # Write the frame to the output video file
    out.write(frame)

# Release resources
cap.release()
out.release()

# Destroy all OpenCV windows
cv2.destroyAllWindows()
