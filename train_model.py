from ultralytics import YOLO

# Load model YOLOv8 có sẵn hoặc tạo model mới
model = YOLO("yolov8s.pt")  

# Huấn luyện mô hình
model.train(data=r"C:\Users\Admin\OneDrive\Desktop\PHANLOAIHOAQUA\Dataset\data.yaml", epochs=50, imgsz=640, batch=16)
