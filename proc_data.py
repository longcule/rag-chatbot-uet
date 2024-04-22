import os

def process_files(folder_path):
    # Lấy danh sách các tệp tin trong thư mục
    files = os.listdir(folder_path)
    
    for file_name in files:
        # Kiểm tra đuôi tệp tin
        if file_name.endswith('.md'):
            file_path = os.path.join(folder_path, file_name)
            
            # Mở tệp tin để đọc
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
            
            # Mở tệp tin để ghi
            with open(file_path, 'w', encoding='utf-8') as file:
                for line in lines:
                    # Kiểm tra dòng bắt đầu bằng ký tự '#'
                    if line.startswith('#'):
                        # Chuyển đổi chữ hoa thành chữ thường
                        line = line.lower()
                    
                    # Loại bỏ các dòng trống và dòng chỉ chứa khoảng trắng
                    if line.strip():
                        # Ghi dòng vào tệp tin
                        file.write(line)

# Đường dẫn tới thư mục chứa các tệp tin Markdown
folder_path = '/home/longcule/Videos/rag-chatbot/abc'

# Gọi hàm xử lý tệp tin
process_files(folder_path)