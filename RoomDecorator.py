import cv2

# Load the image
import numpy as np

img = cv2.imread('C:\\Users\\marvi\\Downloads\\Bedroom.jpg')

# Load the pre-trained object detection model
net = cv2.dnn.readNet("C:\\Users\\marvi\\Downloads\\yolov3.weights", "C:\\Users\\marvi\\Downloads\\darknet-master\\darknet-master\\cfg\\yolov3.cfg")
# Define the object class
classes = []
with open('C:\\Users\\marvi\\Downloads\\darknet-master\\darknet-master\\data\\coco.names', 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# Set the input image  dimensions
input_size = 416

# Prepare the  image for object detection
blob = cv2.dnn.blobFromImage(img, 1/255.0, (input_size, input_size), swapRB=True, crop=False)

# Set the input layer for the network
net.setInput(blob)

# Run object detection on image
outputs = net.forward(net.getUnconnectedOutLayersNames())

# Extract the bounding boxes, confidences,and class IDs of the detected objects
boxes = []
confidences = []
class_ids = []
for output in outputs:
    for detection in output:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]
        if confidence > 0.5:
            center_x = int(detection[0] * img.shape[1])
            center_y = int(detection[1] * img.shape[0])
            w = int(detection[2] * img.shape[1])
            h = int(detection[3] * img.shape[0])
            x = int(center_x - w/2)
            y = int(center_y - h/2)
            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

# Apply non-maximum suppression to remove overlapping boxes
nms_threshold = 0.4
indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, nms_threshold)

# Draw the bounding boxes and class lables on the image
front_scale = 1
thickness = 2
for i in indices:
    for i in indices.flatten():
        x, y, w, h = boxes[1]
        label = classes[class_ids[i]]
        confidence = confidences[i]
        color = (0, 255, 0)
        cv2.rectangle(img, (x,y), (x + w, y + h), color, thickness)
        text = f"{label}: {confidence: .2f}"
        cv2.putText(img, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, front_scale, color, thickness)

# Show the resulting image
cv2.imshow('Object Detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()