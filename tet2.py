import os

def split_md_files(input_folder, output_folder):
    # Tạo thư mục output nếu chưa tồn tại
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Lấy danh sách các file trong thư mục input
    files = os.listdir(input_folder)

    for file_name in files:
        # Kiểm tra nếu là file Markdown
        if file_name.endswith(".md"):
            # Đường dẫn đầy đủ đến file gốc
            input_file_path = os.path.join(input_folder, file_name)

            # Đọc nội dung file Markdown
            with open(input_file_path, 'r', encoding='utf-8') as file:
                content = file.readlines()

            # Tách nội dung thành các phần tử
            sections = []
            current_section = []
            for line in content:
                if line.startswith(("1. Thông tin", "2. Thông tin", "3. Mục tiêu", "4. Chuẩn đầu ra", "5. Tóm tắt", "6. Nội dung", "7. Học liệu", "8. Hình thức", "9. Chính sách", "10. Phương pháp")):
                    if current_section:
                        sections.append(current_section)
                    current_section = [line]
                elif current_section:
                    current_section.append(line)

            # Lưu phần tử cuối cùng
            if current_section:
                sections.append(current_section)
            file_name2 = file_name.split(".")[0]
            # Lưu các phần tử đã tách vào các file mới
            for i, section in enumerate(sections, start=1):
                output_file_name = f"{file_name2}_{i}.md"
                output_file_path = os.path.join(output_folder, output_file_name)
                with open(output_file_path, 'w', encoding='utf-8') as file:
                    file.writelines(section)

    print("Tách file thành công!")

# Thay đổi đường dẫn thư mục input và thư mục output tại đây
input_folder_path = "/home/longcule/Videos/rag-chatbot/docs"
output_folder_path = "/home/longcule/Videos/rag-chatbot/docs42"

split_md_files(input_folder_path, output_folder_path)