#  HỆ THỐNG QUẢN LÝ ĐIỂM HỌC SINH

##  Giới thiệu

**Hệ thống quản lý điểm học sinh** là một ứng dụng web phát triển bằng **Django Framework**, giúp các trường học dễ dàng quản lý thông tin học sinh, giáo viên và điểm số. Hệ thống cung cấp giao diện đơn giản, thân thiện với người dùng và hỗ trợ phân quyền rõ ràng.

### Các chức năng chính:
- Quản lý học sinh, giáo viên, lớp học, môn học
- Phân công giảng dạy cho giáo viên
- Nhập và tra cứu điểm học sinh theo học kỳ, môn học
- Phân quyền người dùng: Quản trị viên, Giáo viên, Học sinh
- Gửi thông báo qua email hoặc Firebase (tùy cấu hình)

---

##  Tính năng nổi bật

-  Đăng nhập theo vai trò: Admin, Giáo viên, Học sinh
-  Quản lý lớp học, học sinh, môn học
-  Nhập và xem điểm theo học kỳ
-  Xuất bảng điểm ra file Excel (tùy chọn)
-  Gửi thông báo đến người dùng qua email hoặc Firebase
-  Giao diện dễ sử dụng, phù hợp với mọi đối tượng

---

##  Công nghệ sử dụng

- **Framework**: Django 4.x
- **Cơ sở dữ liệu**: SQLite (có thể nâng cấp lên PostgreSQL, MySQL)
- **Giao diện**: Django Template
- **Gửi email**: Gmail API / SMTP
- **Thông báo đẩy**: Firebase Cloud Messaging
- **Triển khai**: Google Cloud Run

---

## Cấu trúc thư mục
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
    core/firebase/ — Cấu hình Firebase cho thông báo đẩy  
    credentials.json — Thông tin xác thực Gmail API  
    token.json — Token xác thực cho dịch vụ Gmail  
- Lưu ý: Khi triển khai hoặc chạy hệ thống, bạn cần tải các tệp này từ Drive và đặt đúng vị trí như cấu trúc ở trên.  
---

##  Hướng dẫn cài đặt

### 1. Clone dự án

```bash
git clone https://github.com/ChiBao-v/project-ADP-group5
cd project-ADP-group5
```
### 2. Cài đặt các thư viện phụ thuộc
```bash
pip install -r requirements.txt
```
### 3. Chạy server
```bash
python manage.py runserver
```


python manage.py runserver
```
