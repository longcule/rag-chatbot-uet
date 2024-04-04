# import os

# def split_md_files(input_folder, output_folder):
#     # Tạo thư mục output nếu chưa tồn tại
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)

#     # Lấy danh sách các file trong thư mục input
#     files = os.listdir(input_folder)

#     for file_name in files:
#         # Kiểm tra nếu là file Markdown
#         if file_name.endswith(".md"):
#             # Đường dẫn đầy đủ đến file gốc
#             input_file_path = os.path.join(input_folder, file_name)

#             # Đọc nội dung file Markdown
#             with open(input_file_path, 'r', encoding='utf-8') as file:
#                 content = file.readlines()

#             # Tách nội dung thành các phần tử
#             sections = []
#             current_section = []
#             for line in content:
#                 if line.startswith(("1. Thông tin", "2. Thông tin", "3. Mục tiêu", "4. Chuẩn đầu ra", "5. Tóm tắt", "6. Nội dung", "7. Học liệu", "8. Hình thức", "9. Chính sách", "10. Phương pháp")):
#                     if current_section:
#                         sections.append(current_section)
#                     current_section = [line]
#                 elif current_section:
#                     current_section.append(line)

#             # Lưu phần tử cuối cùng
#             if current_section:
#                 sections.append(current_section)
#             file_name2 = file_name.split(".")[0]
#             # Lưu các phần tử đã tách vào các file mới
#             for i, section in enumerate(sections, start=1):
#                 output_file_name = f"{file_name2}_{i}.md"
#                 output_file_path = os.path.join(output_folder, output_file_name)
#                 with open(output_file_path, 'w', encoding='utf-8') as file:
#                     file.writelines(section)

#     print("Tách file thành công!")

# # Thay đổi đường dẫn thư mục input và thư mục output tại đây
# input_folder_path = "/home/longcule/Videos/rag-chatbot/docs"
# output_folder_path = "/home/longcule/Videos/rag-chatbot/docs42"

# split_md_files(input_folder_path, output_folder_path)

# import os

# def add_header_lines(input_folder, extension):
#     # Lấy danh sách các file trong thư mục input
#     files = os.listdir(input_folder)

#     for file_name in files:
#         # Kiểm tra nếu là file Markdown
#         if file_name.endswith(extension):
#             # Đường dẫn đầy đủ đến file gốc
#             input_file_path = os.path.join(input_folder, file_name)

#             # Đọc nội dung file Markdown
#             with open(input_file_path, 'r', encoding='utf-8') as file:
#                 content = file.readlines()

#             # Thêm "#" vào đầu của các dòng bắt đầu bằng chuỗi
#             for i, line in enumerate(content):
#                 if line.startswith(("1. Thông tin", "2. Thông tin", "3. Mục tiêu", "4. Chuẩn đầu ra", "5. Tóm tắt", "6. Nội dung", "7. Học liệu", "8. Hình thức", "9. Chính sách", "10. Phương pháp")):
#                     content[i] = "# " + line

#             # Ghi nội dung đã sửa vào file
#             with open(input_file_path, 'w', encoding='utf-8') as file:
#                 file.writelines(content)

#     print("Thêm header thành công!")

# # Thay đổi đường dẫn thư mục input và phần mở rộng của file tại đây
# input_folder_path = "/home/longcule/Videos/rag-chatbot/docs"
# file_extension = ".md"

# add_header_lines(input_folder_path, file_extension)


import csv
import os

# Đường dẫn thư mục chứa các file CSV
csv_folder = "/path/to/source/folder"  # Đường dẫn đến thư mục chứa các file CSV

# Đường dẫn thư mục đích để lưu các file txt
txt_folder = "/path/to/target/folder"  # Đường dẫn đến thư mục đích

# Lặp qua các file CSV trong thư mục nguồn
for csv_file in os.listdir(csv_folder):
    if csv_file.endswith(".csv"):
        csv_file_path = os.path.join(csv_folder, csv_file)
        
        # Tạo tên file txt từ tên file CSV
        txt_file = os.path.splitext(csv_file)[0] + ".md"
        txt_file_path = os.path.join(txt_folder, txt_file)

        # Mở file CSV và đọc nội dung
        with open(csv_file_path, 'r') as file:
            # Tạo đối tượng reader để đọc file CSV
            reader = csv.reader(file)

            # Bỏ qua hàng đầu tiên
            next(reader)

            # Mở file txt để ghi kết quả
            with open(txt_file_path, 'w') as txt_file:
                # Lặp qua các dòng và ghi vào file txt
                for row in reader:
                    processed_row = [column.replace('\n', ' - ') for column in row]
                    processed_row = f"Mã học phần: {processed_row[0]}, Tên học phần(Ghi bằng tiếng Việt và tiếng Anh): {processed_row[1]}, Số tín chỉ: {processed_row[2]}, Danh mục tài liệu tham khảo học phần {processed_row[1]} là:\n {row[3]}"
                    # Ghi kết quả vào file txt
                    txt_file.write(f"{processed_row}\n")