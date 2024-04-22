import json



def merge_books(titles, file_path):
    file_path = '/home/longcule/Videos/rag-chatbot/output.json'
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    book = {}

    for item in data:
        if item['title'] in titles:
            print(type(item['book']))
            print("abc",type(book))
            book.update(item['book'])
        
    return book

# Danh sách các tiêu đề
titles = [
    "INT1050_Toán_học_rời_rạc_2023.08.18_v1_3",
    "2023.12.01_CTDT_nganh_KHMT_23",
    "CTDT_nganh_CNTT_CLC_20230928_23",
    "CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20",
    "2023.12.01_CTDT_nganh_MMT_TTDL_23",

    # Thêm các tiêu đề khác tại đây (nếu có)
]

# Đường dẫn tới tệp JSON
file_path = 'output.json'

# Đọc dữ liệu từ tệp JSON
with open(file_path, 'r', encoding='utf-8') as file:
    json_data = json.load(file)

# Hợp nhất sách và đánh lại chỉ mục
merged_data = merge_books(titles, json_data)

# Lưu kết quả vào tệp JSON mới
output_file_path = 'merged_data.json'  # Đường dẫn tới tệp JSON mới
with open(output_file_path, 'w', encoding='utf-8') as file:
    json.dump(merged_data, file, indent=4, ensure_ascii=False)

print(f"Kết quả đã được lưu vào tệp {output_file_path}.")