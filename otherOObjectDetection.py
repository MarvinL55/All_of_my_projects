import cv2

#load the pre-trained imag
# e
model = cv2.dnn.readNetFromCaffe("models/MobileNetSSD_deploy.prototxt.txt", "models/MobileNetSSD_deploy.caffemodel")

confidence_threshold = 0.5

#open camera
cap = cv2.VideoCpature(0)

while True:
    #read the frame from the camera
    ret, frame = cap.read()
    if not ret:
        print("Failed to find camera")
        break

    #Prepare the input for image
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300,300)), 0.007843, (300,300), 127.5)

    #pass input through the network
    model.setInput(blob)
    detections = model.forward()

    #loops over the detection and draw bounding boxes around the detected object
    for i in range(detections.shape[2]):
        confidence = detections[0,0,i,2]
        if confidence > confidence_threshold:
            class_id = int(detections[0,0,i,1])
            x1,y1,x2,y2 = (detections[0,0,i,3:7] * [frame.shape[1], frame.shape[0], frame.shape[1], frame.shape[0]]).astype("int")
            cv2.rectangle(frame, (x1,y1), (x2, y2), (0, 255, 0),2)
            cv2.putText(frame, f"{class_id}", (x1, y1-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    #show thw output
    cv2.imshow("Frame", frame)

    #check for quit key
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

#to close it all
cap.release()
cv2.destroyAllWindows()