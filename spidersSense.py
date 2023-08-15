import cv2
import numpy as np
import pyttsx3

net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt', 'MobileNetSSD_deploy.caffemodel')

person_count = 0

# Opens the webcam
video_capture = cv2.VideoCapture(0)

# Variable for the motion
previous_frame = None

engine = pyttsx3.init()

# Main loop
while True:
    ret, frame = video_capture.read()

    # noise reduction
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Motion detection
    if previous_frame is not None:
        # The difference between the current and the previous frame
        frame_delta = cv2.absdiff(previous_frame, gray)

        # Apply threshold to the image to fill the holes
        thresh = cv2.threshold(frame_delta, 30, 255, cv2.THRESH_BINARY)[1]

        thresh = cv2.dilate(thresh, None, iterations=2)

        # Find contours of threshold image
        contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Iterate over contours and detect motion
        for contour in contours:
            if cv2.contourArea(contour) < 500:
                continue

    previous_frame = gray.copy()

    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (200, 200)), 0.007843, (300, 300), 127.5)
    net.setInput(blob)
    detections = net.forward()

    person_counter = 0  # Counter variable for the number of people detected

    # ...

    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 1]

        # Check if the object is a person and the confidence is above a certain threshold
        if detections[0, 0, i, 1] == 15 and confidence > 0.5:
            person_counter += 1  # Increment the counter for each person detected

            # Get the coordinates of the bounding box
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            # Draw the bounding box and label on the frame
            cv2.rectangle(frame, (startX, startY), (endX, endY), (0, 255, 0), 2)
            cv2.putText(frame, "Person", (startX, startY - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    if person_counter == 2:
        engine.say("Danger is behind you!")
        engine.runAndWait()

        # Display the resulting frame with your face and object detection
    cv2.imshow("Spider Sense Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()