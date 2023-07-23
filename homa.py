import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture('video.mp4')

# Check if camera opened successfully or the video file is opened
if not cap.isOpened():
    print("Error opening video file")

# Read video file frame by frame
while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        # Display the read frame
        cv2.imshow('frame', frame)

        # Press 'q' to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
