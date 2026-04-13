import cv2
from detector import ObjectDetector
from robot_logic import robot_decision

def main():

    detector = ObjectDetector()

    cap = cv2.VideoCapture(1)

    camera_running = True

    cv2.namedWindow("YOLO Robot Vision", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("YOLO Robot Vision", 500, 350)
    cv2.moveWindow("YOLO Robot Vision", 100, 100)

    print("YOLO Robot Vision System Running...")
    print("Press 'p' to pause, 's' to start, 'q' to quit")

    while True:

        if camera_running:
            ret, frame = cap.read()

            if not ret:
                break

            frame, objects = detector.detect(frame)

            robot_decision(objects)

            cv2.imshow("YOLO Robot Vision", frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('p'):
            camera_running = False
            print("Camera paused")

        elif key == ord('s'):
            camera_running = True
            print("Camera resumed")

        elif key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()