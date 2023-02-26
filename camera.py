import cv2
 
# Create a VideoCapture object
cap = cv2.VideoCapture(0)
 
# Check if camera opened successfully
if (cap.isOpened() == False): 
  print("Unable to read camera feed")
 
# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
 
# Captures a single image from the camera and returns it in PIL format
ret, frame = cap.read()
 
# Saves the image
cv2.imwrite("image.png", frame)
 
# When everything done, release the video capture object
cap.release()
