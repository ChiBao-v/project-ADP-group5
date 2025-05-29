# SCORE INPUT - HỆ THỐNG QUẢN LÝ ĐIỂM SINH VIÊN

## Mục lục

1. Thông tin nhóm
2. Giới thiệu
3. Tính năng nổi bật
4. Thiết kế hệ thống
5. Công nghệ sử dụng
6. Cấu trúc thư mục
7. Hướng dẫn cài đặt

---

## 1. THÔNG TIN NHÓM

| Họ và tên              | Email                        | Vai trò                |
|------------------------|------------------------------|------------------------|
| Mai Thị Diệu My        | [maithidieumy18122004@gmail.com]        | Firebase Cloud Messaging (FCM) -  Hiển thị thông báo   |
| Nguyễn Phạm Chí Bảo         | [nguyenphamchibao757@gmail.com]        | Google Cloud Run và Registry - Triển khai dịch vụ             |
| Võ Tấn Bình  | [binhvotan907@gmail.com]       | Gmail API - Gửi email thông báo |
| Vũ Hải Ninh          | [vuninhghjk@gmail.com]       | Docker Based Deployment                 |

---

## 2. GIỚI THIỆU

**Hệ thống quản lý điểm học sinh** là một ứng dụng web phát triển bằng **Django Framework**, giúp các trường học dễ dàng quản lý thông tin học sinh, giáo viên và điểm số. Hệ thống cung cấp giao diện đơn giản, thân thiện với người dùng và hỗ trợ phân quyền rõ ràng.

### Các chức năng chính:
- Quản lý học sinh, giáo viên, lớp học, môn học
- Phân công giảng dạy cho giáo viên
- Nhập và tra cứu điểm học sinh theo học kỳ, môn học
- Phân quyền người dùng: Quản trị viên, Giáo viên, Học sinh
- Gửi thông báo qua email hoặc Firebase (tùy cấu hình)

---

## 3. TÍNH NĂNG NỔI BẬT

-  Đăng nhập theo vai trò: Admin, Giáo viên, Học sinh
-  Quản lý lớp học, học sinh, môn học
-  Nhập và xem điểm theo học kỳ
-  Xuất bảng điểm ra file Excel (tùy chọn)
-  Gửi thông báo đến người dùng qua email hoặc Firebase
-  Giao diện dễ sử dụng, phù hợp với mọi đối tượng

---

## 4. THIẾT KẾ HỆ THỐNG

- **Thiết kế CSDL:**
  <div align="center">
    <img src="https://github.com/user-attachments/assets/394a6b19-9a2d-4cff-be8a-341a2b32cd56" alt="Sơ đồ CSDL" width="500"/><br>
    <i>Hình 1: Sơ đồ quan hệ các bảng trong cơ sở dữ liệu. Các bảng liên kết với nhau qua các khóa ngoại để đảm bảo tính toàn vẹn dữ liệu.</i>
  </div>

- **Thiết kế giao diện:**  
  Giao diện được thiết kế hiện đại, thân thiện với người dùng. Dưới đây là một số hình ảnh minh họa các màn hình chính của hệ thống:

  <div align="center">
  
    <h4>Landing Page</h4>
    <img src="https://github.com/user-attachments/assets/bc612e5f-9496-4ae5-9e07-c335fda192f8" width="500"/><br>
    <i>Hình 2: Trang giới thiệu hệ thống, đăng nhập và các thông tin tổng quan về hệ thống.</i>
  
    <h4>Login Page</h4>
    <img src="https://github.com/user-attachments/assets/ef2c6ceb-b2db-4801-ac19-1e0d26012bc8" alt="Login Page" width="500"/><br>
    <i>Hình 3: Login Page – Trang đăng nhập vào hệ thống.</i>
  
    <h4>Admin Dashboard</h4>
    <img src="https://github.com/user-attachments/assets/5ba48f25-cbed-4a3e-8f7e-c6c57981d1e8" alt="Admin Dashboard" width="500"/><br>
    <i>Hình 4: Dashboard dành cho Admin.</i>
  
    <h4>Teacher Dashboard</h4>
    <img src="https://github.com/user-attachments/assets/9e273c06-8e0d-4e22-8251-b9842ed74b51" alt="Sale Dashboard" width="500"/><br>
    <i>Hình 5: Dashboard dành cho Teacher.</i>
  
    <h4>Student Dashboard</h4>
    <img src="https://github.com/user-attachments/assets/b3d3af13-fbc0-4140-ba77-610df81988ad" alt="Product Manager Dashboard" width="500"/><br>
    <i>Hình 6: Dashboard dành cho Student.</i>
  
    </div>

---

## 5. CÔNG NGHỆ SỬ DỤNG

- **Framework**: Django 4.x
- **Cơ sở dữ liệu**: SQLite (có thể nâng cấp lên PostgreSQL, MySQL)
- **Giao diện**: Django Template
- **Gửi email**: Gmail API / SMTP
- **Thông báo đẩy**: Firebase Cloud Messaging
- **Triển khai**: Google Cloud Run

---

## 6. CẤU TRÚC THƯ MỤC
```bash
project-ADP-group5/  
│  
├── core/                     # Ứng dụng con: Xử lý logic chính (models, views, urls, v.v.)  
├── grade_management/         # Thư mục cấu hình Django (settings.py, urls.py, wsgi.py, v.v.)    
├── images/                   # Thư mục chứa hình ảnh tĩnh (nếu có)  
├── static/                   # Thư mục chứa các file tĩnh (CSS, JS, ảnh,...)  
├── templates/                # Thư mục chứa các template HTML  
│  
├── .dockerignore            # File cấu hình Docker để loại trừ file/thư mục không cần thiết  
├── credentials.json         # Thông tin xác thực Gmail API (nên bảo mật)  
├── db.sqlite3               # Cơ sở dữ liệu SQLite  
├── Dockerfile               # File cấu hình Docker  
├── manage.py                # File quản lý Django (chạy server, migrate, v.v.)  
├── proposal.md              # Tài liệu đề xuất dự án    
├── README.md                # File mô tả dự án (hiển thị trên GitHub)  
├── requirements.txt         # Danh sách các thư viện cần cài  
└── token.json               # Token xác thực Gmail API (sinh ra khi xác thực)  
```
---
- Vì lý do bảo mật, các tệp sau đã được ẩn khỏi GitHub và được lưu trữ riêng trong thư mục key/ trên Google Drive:
  ```bash
    core/firebase/ — Cấu hình Firebase cho thông báo đẩy  
    credentials.json — Thông tin xác thực Gmail API  
    token.json — Token xác thực cho dịch vụ Gmail
  ```
- Lưu ý: Khi triển khai hoặc chạy hệ thống, bạn cần tải các tệp này từ Drive và đặt đúng vị trí như cấu trúc ở trên.  
---

## 7. HƯỚNG DẪN CÀI ĐẶT

### 7.1. Clone dự án

```bash
git clone https://github.com/ChiBao-v/project-ADP-group5
cd project-ADP-group5
```
### 7.2. Cài đặt các thư viện phụ thuộc
```bash
pip install -r requirements.txt
```
### 7.3. Chạy server
```bash
python manage.py runserver
```
**Link deploy:**  
Truy cập website tại: [Score-Input Website](https://score-input-service-747091567428.us-central1.run.app/)
