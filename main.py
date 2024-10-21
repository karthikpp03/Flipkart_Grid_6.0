import cv2
from ultralytics import YOLO
import numpy as np

# Load a YOLOv8 model
model = YOLO("/home/sridhar/myData/college projects/flipkart-6.0/main/dataSet/models/objectDetectionModels/model-fr-24/weights/best.pt")  # Replace 'yolov8n.pt' with another YOLOv8 model if needed

# Open a video capture (0 for default webcam)
cap1 = cv2.VideoCapture(0)
cap2 = cv2.VideoCapture(1)
cap3 = cv2.VideoCapture(2)

# Main loop
while True:
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()
    ret3, frame3 = cap3.read()
    # frame = cv2.imread("/home/sridhar/myData/college projects/flipkart-6.0/main/camera/image4.jpeg")
    frame = cv2.resize(frame, (640, 640))
    if not ret1 and not ret2 and not ret3:
        break

    # Perform object detection
    results = model([frame1, frame2, frame3], conf=0.7)

    # Process the results
    for i, result in enumerate(results):
        image = [frame1, frame2, frame3][i]
        boxes = result.boxes  # Access detected bounding boxes
        for box in boxes:
            # Extract bounding box coordinates, confidence, and class
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Convert to integer
            conf = box.conf[0].item()  # Confidence score
            cls = int(box.cls[0].item())  # Class ID

            # Draw bounding box and label
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, f'{model.names[cls]} {conf:.2f}', (x1, y1 - 10), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('YOLOv8 Object Detection', frame1)
    cv2.imshow('YOLOv8 Object Detection', frame2)
    cv2.imshow('YOLOv8 Object Detection', frame3)

    # Exit loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

cap1.release()
cap2.release()
cap3.release()
cv2.destroyAllWindows()
