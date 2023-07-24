import cv2
import time

# Create a VideoCapture object
cap = cv2.VideoCapture('video.mp4')

# Check if camera opened successfully or the video file is opened
if not cap.isOpened():
    print("Error opening video file")
    
# Determine the number of frames to skip for a 5-second jump
fps = cap.get(cv2.CAP_PROP_FPS)
skip_frames = int(fps * 5)


# Variables to calculate FPS
frame_counter = 0
start_time = time.time()
fps = 0


# Read video file frame by frame
pause = False
wait_time = 25
playback_speed = 1.0
message = ""
message_duration = 0
current_frame = 0
while cap.isOpened():
    if not pause:
        ret, frame = cap.read()
        if ret:
            current_frame += 1

    if ret:

        frame_counter += 1
        # Calculate FPS every second
        if frame_counter % 60 == 0:
            end_time = time.time()
            fps = frame_counter / (end_time - start_time)
            # Reset the variables
            frame_counter = 0
            start_time = time.time()
        # Write FPS onto the frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        text = f"FPS: {fps:.0f}"
        text_size, _ = cv2.getTextSize(text, font, 1, 2)
        text_width, text_height = text_size
        cv2.rectangle(frame, (0, 30), (text_width + 20, text_height + 40), (0, 0, 0), -1)
        cv2.putText(frame, text, (5, text_height + 35), font, 1, (255, 255, 255), 2)


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
        elif key & 0xFF == ord('-'):
            wait_time += 5
            playback_speed = 25.0 / wait_time
        elif key & 0xFF == ord('a'):
            # Go back one frame
            current_frame = max(0, current_frame - 2)
            cap.set(cv2.CAP_PROP_POS_FRAMES, current_frame)
            ret, frame = cap.read()
            if ret:
                message = "Previous frame"
                message_duration = 1000
                current_frame += 1
            if not ret:
                print("Error reading frame")
        elif key & 0xFF == ord('d'):
            # Go forward one frame
            ret, frame = cap.read()
            current_frame += 1
            message = "Next frame"
            message_duration = 1000
            if not ret:
                print("Error reading frame")
        elif key & 0xff == ord("z"):  
            # Go back 5 seconds
            current_time = cap.get(cv2.CAP_PROP_POS_MSEC)
            new_time = max(0, current_time - 5000)
            cap.set(cv2.CAP_PROP_POS_MSEC, new_time)
            current_frame = int(new_time / 1000 * fps)
            message = "5 Sec. Forward"
            message_duration = 1000
        elif key & 0xff == ord("x"):  
            # Go forward 5 seconds
            current_time = cap.get(cv2.CAP_PROP_POS_MSEC)
            new_time = current_time + 5000
            cap.set(cv2.CAP_PROP_POS_MSEC, new_time)
            current_frame = int(new_time / 1000 * fps)
            message = "5 Sec. Backward"
            message_duration = 1000
    else:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
