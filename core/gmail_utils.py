import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import os

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

# Hàm tạo và lấy service
def get_service():
    creds = None
    # Nếu đã có file token.json thì tải thông tin xác thực từ đó
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        # Nếu chưa có token.json, chạy quá trình xác thực OAuth
        flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
        creds = flow.run_local_server(port=5000)  # Mở trình duyệt để đăng nhập
        # Lưu lại thông tin xác thực vào file token.json
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Tạo service Gmail API với thông tin xác thực
    service = build('gmail', 'v1', credentials=creds)
    return service

# Hàm gửi email
def send_email(to, subject, body):
    service = get_service()
    message = MIMEText(body, 'plain')
    message['to'] = to
    message['subject'] = subject
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()

    try:
        message = service.users().messages().send(userId="me", body={'raw': raw}).execute()
        print(f'Gửi thành công. ID: {message["id"]}')
    except Exception as e:
        print(f'Lỗi gửi email: {e}')
