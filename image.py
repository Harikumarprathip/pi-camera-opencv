import cv2

# Open the camera
cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Capture a single frame
ret, frame = cap.read()

# Check if the frame was captured successfully
if not ret:
    print("Error: Could not read frame.")
    cap.release()
    exit()

# Save the captured frame to a file
cv2.imwrite('example_image.jpg', frame)

# Release the camera
cap.release()
