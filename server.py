from flask import Flask, render_template, Response, jsonify
import cv2
import numpy as np
import requests  
import time
from ultralytics import YOLO

ESP8266_URL = "http://192.168.1.6/control"

model = YOLO("runs/detect/train/weights/best.pt")

app = Flask(__name__)

# Danh sách các quả đã được phân loại để tránh xử lý trùng
processed_objects = set()
history = []

# Map class ID sang tên loại quả
CLASS_NAMES = {0: "Cam", 1: "Chanh", 2: "Nho", 3: "Cà chua"}

def detect_objects():
    cap = cv2.VideoCapture("http://192.168.1.7:81/stream")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Lỗi: Không lấy được frame từ camera!")
            continue
        
        results = model(frame)

        for i, box in enumerate(results[0].boxes):
            x1, y1, x2, y2 = box.xyxy[0]
            confidence = box.conf[0]
            class_id = int(box.cls[0])
            obj_id = f"{class_id}_{int(x1)}_{int(y1)}"  # Xác định duy nhất quả theo vị trí

            if confidence > 0.85 and obj_id not in processed_objects:
                label = f"{CLASS_NAMES[class_id]} ({confidence:.2f})"
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

                # Gửi tín hiệu đến ESP8266 để điều khiển servo
                if class_id == 1:  # Chanh
                    requests.get(f"{ESP8266_URL}?servo=1")
                elif class_id == 3:  # Ca chua
                    requests.get(f"{ESP8266_URL}?servo=2")
                elif class_id == 0:  # Cam
                    print("🍋 Cam! Không gạt, để chạy tiếp.")
                elif class_id == 2:  # Nho
                    print("🟣 Nho! Không gạt, để chạy tiếp.")
                
                # Lưu lịch sử quét
                history.append({"time": time.strftime("%H:%M:%S"), "fruit": CLASS_NAMES[class_id]})

                # Đánh dấu đã xử lý quả này
                processed_objects.add(obj_id)

        yield frame

def generate_frames():
    for frame in detect_objects():
        _, buffer = cv2.imencode(".jpg", frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

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
