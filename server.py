from flask import Flask, render_template, Response, jsonify
import cv2
import numpy as np
import requests  
import time
from ultralytics import YOLO

ESP8266_URL = "http://172.20.10.14/control"

model = YOLO("runs/detect/train/weights/best.pt")

app = Flask(__name__)

processed_objects = set()
history = []

CLASS_NAMES = {0: "Cam", 1: "Chanh", 2: "Nho", 3: "Ca chua"}

MIN_WIDTH = 30
MIN_HEIGHT = 30
MAX_WIDTH = 500
MAX_HEIGHT = 500

def detect_objects():
    cap = cv2.VideoCapture("http://172.20.10.2:81/stream")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Lỗi: Không lấy được frame từ camera!")
            continue
        
        results = model(frame)

        for box in results[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = float(box.conf[0])
            class_id = int(box.cls[0])
            width, height = x2 - x1, y2 - y1

            if width < MIN_WIDTH or height < MIN_HEIGHT or width > MAX_WIDTH or height > MAX_HEIGHT:
                continue  

            obj_id = f"{class_id}_{x1}_{y1}"

            if confidence > 0.7 and obj_id not in processed_objects:
                label = f"{CLASS_NAMES[class_id]} ({confidence:.2f})"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

                try:
                    if class_id == 3:  # Cà chua -> Servo 1
                        requests.get(f"{ESP8266_URL}?servo=1", timeout=1)
                    elif class_id == 1:  # Chanh -> Servo 2
                        requests.get(f"{ESP8266_URL}?servo=2", timeout=1)
                    # Không gửi lệnh gì cho nho (class_id == 2)
                except requests.exceptions.RequestException:
                    print("❌ Lỗi: Không thể gửi lệnh đến ESP8266!")

                history.append({"time": time.strftime("%H:%M:%S"), "fruit": CLASS_NAMES[class_id]})
                processed_objects.add(obj_id)

        yield frame

def generate_frames():
    for frame in detect_objects():
        _, buffer = cv2.imencode(".jpg", frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/')
def index():
    return render_template("web_dashboard.html")

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/history')
def get_history():
    return jsonify(history)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
