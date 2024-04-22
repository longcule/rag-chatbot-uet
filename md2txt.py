import os

def remove_headings(input_folder, output_folder):
    # Tạo thư mục đầu ra nếu nó chưa tồn tại
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Lặp qua tất cả các tệp tin trong thư mục đầu vào
    for filename in os.listdir(input_folder):
        if filename.endswith(".md"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".txt")

            # Đọc nội dung từ tệp tin markdown
            with open(input_path, "r") as file:
                content = file.readlines()

            # Xóa các dòng bắt đầu bằng dấu #
            modified_content = [line.lstrip("#") if line.startswith("#") else line for line in content]

            # Ghi nội dung đã chỉnh sửa vào tệp tin văn bản mới
            with open(output_path, "w") as file:
                file.writelines(modified_content)

            print(f"Đã xử lý tệp tin: {filename}")

# Thư mục đầu vào chứa các tệp tin markdown
input_folder = "/home/longcule/Videos/rag-chatbot/docs"

# Thư mục đầu ra cho các tệp tin văn bản đã chỉnh sửa
output_folder = "/home/longcule/Videos/rag-chatbot/docstxt"

# Gọi hàm để xóa các dấu # và lưu thành các tệp tin văn bản mới
remove_headings(input_folder, output_folder)