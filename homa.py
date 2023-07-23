import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture('video.mp4')

# Check if camera opened successfully or the video file is opened
if not cap.isOpened():
    print("Error opening video file")

# Read video file frame by frame
pause = False
while cap.isOpened():
    if not pause:
        ret, frame = cap.read()

    if ret:
        # Display the read frame
        cv2.imshow('frame', frame)

        # Press 'q' to exit
        key = cv2.waitKey(25)
        if key & 0xFF == ord('q'):
            break
        elif key & 0xFF == ord(' '):
            pause = not pause
        elif key & 0xFF == ord('s'):
            cv2.imwrite('screenshot.png', frame)
    else:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
 