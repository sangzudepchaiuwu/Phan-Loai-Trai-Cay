import cv2
import numpy as np
from ultralytics import YOLO

# Địa chỉ luồng video của ESP32-CAM
url = "http://172.20.10.2:81/stream"
# Tải mô hình YOLOv8
model = YOLO("runs/detect/train/weights/best.pt")

# Kết nối đến camera
cap = cv2.VideoCapture(url)

if not cap.isOpened():
    print("Không thể kết nối đến ESP32-CAM!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Lỗi khi nhận dữ liệu từ camera!")
        break

    results = model(frame)

    for box in results[0].boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        confidence = box.conf[0]
        class_id = int(box.cls[0])

        if confidence > 0.75:  # Giảm ngưỡng để nhận diện tốt hơn quả nhỏ
            label = f"Class {class_id} {confidence:.2f}"
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, label, (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Hiển thị video
    cv2.imshow("ESP32-CAM Live Stream", frame)

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()