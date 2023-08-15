import cv2

object_cascade = cv2.CascadeClassifier("C:\\Users\\marvi\\PycharmProjects\\pythonProject1\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()
    if not ret:
        print("Failed to read the frame from camera")
        break

    #Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect object in the grayscale frame
    objects = object_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    # Draw rectangles around the object that was detected
    for (x, y, w, h) in objects:
        cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame with the detected objects
    cv2.imshow("Detect Objects", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()