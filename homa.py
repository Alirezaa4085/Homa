import cv2

# Create a VideoCapture object
cap = cv2.VideoCapture('video.mp4')

# Check if camera opened successfully or the video file is opened
if not cap.isOpened():
    print("Error opening video file")

# Read video file frame by frame
pause = False
wait_time = 25
playback_speed = 1.0
message = ""
message_duration = 0
while cap.isOpened():
    if not pause:
        ret, frame = cap.read()

    if ret:
        # Display playback speed on the top left corner of the frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f"Speed: {playback_speed:.1f}x"
        text_size, _ = cv2.getTextSize(text, font, 1, 2)
        text_width, text_height = text_size
        cv2.rectangle(frame, (0, 0), (text_width + 10, text_height + 10), (0, 0, 0), -1)
        cv2.putText(frame, text, (5, text_height + 5), font, 1, (255, 255, 255), 2)

        # Display message on the top right corner of the frame
        if message_duration > 0:
            text_size, _ = cv2.getTextSize(message, font, 1, 2)
            text_width, text_height = text_size
            x = frame.shape[1] - text_width - 15
            y = text_height + 5
            cv2.rectangle(frame, (x - 5, 0), (x + text_width + 5, y + 5), (0, 0, 0), -1)
            cv2.putText(frame, message, (x, y), font, 1, (255, 255, 255), 2)
            message_duration -= wait_time

        # Display the read frame
        cv2.imshow('frame', frame)
        cv2.setWindowTitle('frame', 'Homa')

        # Press 'q' to exit
        key = cv2.waitKey(wait_time)
        if key & 0xFF == ord('q'):
            break
        elif key & 0xFF == ord(' '):
            pause = not pause
            message = "Pause" if pause else "Play"
            message_duration = 1000
        elif key & 0xFF == ord('s'):
            cv2.imwrite('screenshot.png', frame)
            message = "Screenshot saved"
            message_duration = 1000
        elif key & 0xFF == ord('+'):
            wait_time = max(1, wait_time - 5)
            playback_speed = 25.0 / wait_time
            message = f"Speed: {playback_speed:.1f}x"
            message_duration = 1000
        elif key & 0xFF == ord('-'):
            wait_time += 5
            playback_speed = 25.0 / wait_time
            message = f"Speed: {playback_speed:.1f}x"
            message_duration = 1000
    else:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
