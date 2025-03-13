
import os
from ultralytics import YOLO

# Đường dẫn đến ảnh bạn vừa tải lên
image_path = "Dataset/test/images/image.png"

# Load mô hình YOLOv8 đã huấn luyện
model = YOLO("runs/detect/train/weights/best.pt")

# Dự đoán trên ảnh
results = model(image_path, save=True)

# Hiển thị kết quả dự đoán
results[0].show()

print(f"Đã nhận diện trên ảnh: {image_path}")
