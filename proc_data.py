# import csv
# import os

# # Đường dẫn đến file CSV
# csv_file = "/home/longcule/Videos/rag-chatbot/Table_CTDT - HTTT_CTDT.csv"

# # Tạo tên file txt từ tên file CSV
# txt_file = os.path.splitext(csv_file)[0] + ".md"

# # Mở file CSV và đọc nội dung
# with open(csv_file, 'r') as file:
#     # Tạo đối tượng reader để đọc file CSV
#     reader = csv.reader(file)

#     # Bỏ qua hàng đầu tiên
#     next(reader)

#     # Mở file txt để ghi kết quả
#     with open(txt_file, 'w') as txt_file:
#         # Lặp qua các dòng và ghi vào file txt
#         for row in reader:
#             if row[0]:  # Kiểm tra giá trị của cột đầu tiên
#                 processed_row = [column.replace('\n', ' - ') for column in row]
#                 processed_row = [
#                     f"### {row[0]}. {row[1]} chương trình đào tạo ngành Hệ Thống Thông Tin(HTTT), Tổng số tín chỉ: {row[3]}"
#                 ]
#             else:
#                 processed_row = [column.replace('\n', ' - ') for column in row]
#                 processed_row = [
#                     f"Mã số học phần: {row[1]}, Tên học phần(Ghi bằng tiếng Việt và tiếng Anh): {row[2]}, số tín chỉ: {row[3]}, Lý thuyết: {row[4]}, Thực hành: {row[5]}, Tự học: {row[6]}, mã số học phần tiên quyết: {row[7]}"
#                 ]
            
#             # Ghi kết quả vào file txt
#             txt_file.write(f"{processed_row}\n")


# import csv
# import os

# # Đường dẫn đến file CSV
# csv_file = "/home/longcule/Videos/rag-chatbot/Table_CTDT - CNTT_NB_TAILIEU.csv"

# # Tạo tên file txt từ tên file CSV
# txt_file = os.path.splitext(csv_file)[0] + ".md"

# # Mở file CSV và đọc nội dung
# with open(csv_file, 'r') as file:
#     # Tạo đối tượng reader để đọc file CSV
#     reader = csv.reader(file)

#     # Bỏ qua hàng đầu tiên
#     next(reader)

#     # Mở file txt để ghi kết quả
#     with open(txt_file, 'w') as txt_file:
#         # Lặp qua các dòng và ghi vào file txt
#         for row in reader:
#             processed_row = [column.replace('\n', ' - ') for column in row]
#             # print(processed_row)
#             processed_row = f"Mã học phần: {processed_row[0]}, Tên học phần(Ghi bằng tiếng Việt và tiếng Anh): {processed_row[1]}, Số tín chỉ: {processed_row[2]}, Danh mục tài liệu tham khảo học phần {processed_row[1]} là:\n {row[3]}"
#             # Ghi kết quả vào file txt
#             txt_file.write(f"{processed_row}\n")


import csv
import os

# Đường dẫn thư mục chứa các file CSV
csv_folder = "/home/longcule/Videos/rag-chatbot/gv"  # Đường dẫn đến thư mục chứa các file CSV

# Đường dẫn thư mục đích để lưu các file txt
txt_folder = "/home/longcule/Videos/rag-chatbot/gv1"  # Đường dẫn đến thư mục đích

# Lặp qua các file CSV trong thư mục nguồn
for csv_file in os.listdir(csv_folder):
    if csv_file.endswith(".csv"):
        csv_file_path = os.path.join(csv_folder, csv_file)
        
        # Tạo tên file txt từ tên file CSV
        txt_file = os.path.splitext(csv_file)[0] + ".md"
        txt_file_path = os.path.join(txt_folder, txt_file)

        # Mở file CSV và đọc nội dung
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            # Tạo đối tượng reader để đọc file CSV
            reader = csv.reader(file)

            # Bỏ qua hàng đầu tiên
            next(reader)

            # Mở file txt để ghi kết quả
            with open(txt_file_path, 'w') as txt_file:
                # Lặp qua các dòng và ghi vào file txt
                for row in reader:
                    processed_row = [column.replace('\n', ' - ') for column in row]
                    if processed_row[1] != '':
                        processed_row = f"### Các giảng viên học phần: {processed_row[1]} là:\nTên giảng viên: {row[3]}, chức danh: {row[4]}, chuyên ngành: {row[5]}, đơn vị: {row[6]}"
                    if processed_row[1] == '':
                        processed_row = f"Tên giảng viên: {row[3]}, chức danh: {row[4]}, chuyên ngành: {row[5]}, đơn vị: {row[6]}"
                    # Ghi kết quả vào file txt
                    txt_file.write(f"{processed_row}\n")