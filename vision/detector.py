import cv2
import time
from ultralytics import YOLO

model = YOLO("yolov8n.pt")


def detect(duration=5):

    cap = cv2.VideoCapture(0)

    detected = set()

    start = time.time()

    while time.time() - start < duration:

        ret, frame = cap.read()

        if not ret:
            break

        results = model(frame)

        for box in results[0].boxes:

            cls = int(box.cls)

            detected.add(model.names[cls])

        frame = results[0].plot()

        cv2.imshow("JARVIS Vision", frame)

        cv2.waitKey(1)

    cap.release()

    cv2.destroyAllWindows()

    return list(detected)