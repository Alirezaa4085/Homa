import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture('video.mp4')

# Check if camera opened successfully or the video file is opened
if not cap.isOpened():
    print("Error opening video file")

# Read video file frame by frame
pause = False
wait_time = 25
while cap.isOpened():
    if not pause:
        ret, frame = cap.read()

    if ret:
        # Display the read frame
        cv2.imshow('frame', frame)

        # Press 'q' to exit
        key = cv2.waitKey(wait_time)
        if key & 0xFF == ord('q'):
            break
        elif key & 0xFF == ord(' '):
            pause = not pause
        elif key & 0xFF == ord('s'):
            cv2.imwrite('screenshot.png', frame)
        elif key & 0xFF == ord('+'):
            wait_time = max(1, wait_time - 5)
        elif key & 0xFF == ord('-'):
            wait_time += 5
    else:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
