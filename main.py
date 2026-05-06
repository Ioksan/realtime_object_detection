import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # se descarcă automat prima dată

cap = cv2.VideoCapture(0)  # 0 = webcam default

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, verbose=False)
    annotated = results[0].plot()

    cv2.imshow("Real-Time Object Detection", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()