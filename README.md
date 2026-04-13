#  YOLO-Based Robot Vision System

##  Overview

The YOLO-Based Robot Vision System is a real-time computer vision application that captures live video from a camera, detects objects using a YOLO-based detection model, and triggers decision-making logic for robotic actions. The system integrates OpenCV for video processing and a modular architecture for detection and robot control.

---

##  Problem Statement

Robotic systems require real-time perception of their surroundings to make intelligent decisions. Traditional systems lack efficient and fast object detection capabilities needed for dynamic environments.

---

##  Solution

This project uses:

* YOLO-based object detection for real-time accuracy
* OpenCV for live camera feed processing
* Custom robot decision logic based on detected objects

to simulate an intelligent vision system for robotics.

---

##  Key Features

*  Real-time video capture using camera
*  Object detection using YOLO model
*  Automated decision-making logic
*  Camera control (Start / Pause / Quit)
*  Resizable and interactive display window
*  Fast and efficient processing

---

##  Tech Stack

* **Programming Language:** Python
* **Computer Vision:** OpenCV
* **Model:** YOLO (You Only Look Once)
* **Architecture:** Modular Python scripts

---

##  How It Works

1. Camera captures live video frames
2. YOLO model detects objects in each frame
3. Detected objects are passed to decision logic
4. Robot decision function determines action
5. Output is displayed in real-time window

---

##  Project Structure

vision-system/
│
├── main.py                    # Main application file
├── detector.py               # Object detection logic (YOLO)
├── robot_logic.py            # Decision-making module
├── models/                   # YOLO model files (not uploaded if large)
└── README.md

---

##  How to Run the Project

### 1️ Clone the repository

git clone https://github.com/uzi-works/YOLO-Based-Robot-Vision-System
cd vision-system

### 2️ Install dependencies

pip install opencv-python

### 3️ Run the application

python main.py

---

##  Controls

* **P** → Pause camera
* **S** → Start/Resume camera
* **Q** → Quit application

---

##  Output

* Real-time object detection displayed on screen
* Bounding boxes and labels for detected objects
* Console-based robot decisions

---

##  Notes

* Model files (YOLO weights) are not included due to size limitations
* Ensure correct camera index (e.g., 0 or 1) depending on your system

---

##  Future Improvements

* Integrate hardware robot control
* Improve detection accuracy with custom-trained models
* Add object tracking
* Deploy on edge devices (Raspberry Pi, Jetson Nano)
* Add GUI-based control panel

---

##  Screenshots (Add Later)

*Add detection output screenshots here*

---

##  Contributing

Contributions are welcome! Feel free to fork and improve the project.

---

##  License

This project is open-source and available under the MIT License.

---

##  Author

**Uzair Sabir**
B.Tech CSE | AI Enthusiast

---

## ⭐ Acknowledgements

* YOLO Object Detection Framework
* OpenCV Library
