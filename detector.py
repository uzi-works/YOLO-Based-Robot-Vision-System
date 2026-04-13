from ultralytics import YOLO

class ObjectDetector:

    def __init__(self):
        self.model = YOLO("yolov8n.pt")  # lightweight model

    def detect(self, frame):

        results = self.model(frame)

        detections = []

        for result in results:
            boxes = result.boxes

            for box in boxes:
                cls = int(box.cls[0])
                label = self.model.names[cls]

                detections.append(label)

        annotated_frame = results[0].plot()

        return annotated_frame, detections