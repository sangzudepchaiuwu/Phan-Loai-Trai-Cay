<h1 align="center">PHÂN LOẠI HOA QUẢ</h1>

<div align="center">

<p align="center">
  <img src="images/logoDaiNam.png" alt="DaiNam University Logo" width="200"/>
  <img src="images/LogoAIoTLab.png" alt="AIoTLab Logo" width="170"/>
</p>

[![Made by AIoTLab](https://img.shields.io/badge/Made%20by%20AIoTLab-blue?style=for-the-badge)](https://www.facebook.com/DNUAIoTLab)
[![Fit DNU](https://img.shields.io/badge/Fit%20DNU-green?style=for-the-badge)](https://fitdnu.net/)
[![DaiNam University](https://img.shields.io/badge/DaiNam%20University-red?style=for-the-badge)](https://dainam.edu.vn)

</div>

<h2 align="center">PHÂN LOẠI HOA QUẢ</h2>

<p align="left">
HỆ THỐNG PHÂN LOẠI HOA QUẢ SỬ DỤNG ESP32CAM VÀ BĂNG CHUYỀN
</p>

---

## 🌟 Giới thiệu

- **📌 Tự động nhận diện hoa quả** 
- **💡 Thông báo trực quan:** Arduino sẽ điều khiển cần gạt để đẩy quả về khay quy định
- **🖥️ Giao diện thân thiện:** .

---
## 🏗️ HỆ THỐNG!
<p align="center">
  <img src="images/structure.png" alt="System Architecture" width="800"/>
</p>



---
## 📂 Cấu trúc dự án

📦 Project  
├── 📂 Dataset 
├── 📂 runs   
│   ├── 📂 detect
        ├── 📂 train
            ├── 📂 weights
├── 📂 templates  
│   ├── web_dashboard 
├── server.py  
├── test1.py 
├── tét.py
├── train_model.py
├── yolov8s.py




## 🛠️ CÔNG NGHỆ SỬ DỤNG

<div align="center">

### 📡 Phần cứng
ARDUINO UNO
ESP32CAM
ESP8266
BĂNG CHUYỀN

### 🖥️ Phần mềm
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)]()
[![Flask](https://img.shields.io/badge/Flask-Framework-black?style=for-the-badge&logo=flask)]()
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-blue?style=for-the-badge)]()

</div>

## 🛠️ Yêu cầu hệ thống

### 🔌 Phần cứng
- **Arduino Uno** Điều khiển servo và kết nối với ESP8266
- **ESP32CAM** Tạo luồng stream video
- **ESP8266** Kết nối với flask gửi lệnh qua lại giữa flask arduino uno

### 💻 Phần mềm
- **🐍 Python 3+**
- **⚡ Arduino IDE** 

### 📦 Các thư viện Python cần thiết
Cài đặt các thư viện bằng lệnh:

    pip install ultralytics 
    pip install opencv-python

## 🚀 Hướng dẫn cài đặt và chạy
1️ Chuẩn bị phần cứng
- **Nạp mã Arduino**
- **Nạp mã ESP8266**
- **Nạp mã ESP32CAM**

   

2️ Cài đặt thư viện Python. 

Cài đặt Python 3 nếu chưa có, sau đó cài đặt các thư viện cần thiết bằng pip.

3 Huấn luyện mô hình
Chạy code trong train_model.py để huấn luyện mô hình từ dataset để xuất ra file train

4 Chạy các chương trình
Chạy Server.py đẻ hiển thị màn hình livestream camera để hiển thị phân loại




## 📰 Poster
<p align="center">
  <img src="images/b94cdba5a0ef7d9573080a176875ea36-0.png" alt="System Architecture" width="800"/>
</p>

## 🤝 Đóng góp
Dự án được phát triển bởi 4 thành viên:

| Họ và Tên        | Vai trò                  |
|----------------- |--------------------------|
| Vũ Tài Sang      | Phát triển toàn bộ mã nguồn, thiết kế cơ sở dữ liệu, kiểm thử, triển khai dự án và thực hiện video giới thiệu.|
| Trần Lê Bảo Long | Biên soạn tài liệu Overleaf, Poster, Powerpoint.|
| Phạm Đức Long    | Thiết kế slide PowerPoint, hỗ trợ bài tập lớn.  |
| Bùi Duy Anh      | Hỗ trợ bài tập lớn       |

© 2025 NHÓM 2, CNTT16-02, TRƯỜNG ĐẠI HỌC ĐẠI NAM
