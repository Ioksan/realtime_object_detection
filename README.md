# 🎯 Realtime Object Detection

Real-time object detection using YOLOv8 and OpenCV.

## 📋 Requirements

- Python 3.8+
- Webcam

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/loksan/realtime_object_detection.git
cd realtime_object_detection

# Create virtual environment
python -m venv realtimenv
realtimenv\Scripts\activate

# Install dependencies
pip install opencv-python ultralytics
```

## 🚀 Usage

```bash
python main.py
```

- The model (`yolov8n.pt`) downloads automatically on first run
- Press **Q** to quit

## 🛠️ How it works

- Captures video from webcam using OpenCV
- Runs YOLOv8 nano model for object detection
- Displays bounding boxes and labels in real-time