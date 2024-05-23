import json

# def remove_special_characters(text):
#     # Loại bỏ các kí tự đặc biệt trong văn bản
#     special_characters = ['*', '\n', '"', '-']
#     for char in special_characters:
#         text = text.replace(char, '')
#     return text

# Đường dẫn tới file JSON gốc và file JSON mới
input_file_path = '/home/longcule/Videos/rag-chatbot/output_rag_250_clean.json'
output_file_path_1 = '/home/longcule/Videos/rag-chatbot/output_rag_250_rag.txt'
output_file_path_2 = '/home/longcule/Videos/rag-chatbot/output_rag_250_gpt4.txt'
# Đọc file JSON gốc
with open(input_file_path, 'r', encoding='utf-8') as input_file:
    data = json.load(input_file)

list1 = []
list2 = []
# Loại bỏ kí tự đặc biệt trong các trường answer_rag và answer_gpt4
for item in data:
    if 'answer_rag' in item:
        list1.append(item['answer_rag'])
        # item['answer_rag'] = remove_special_characters(item['answer_rag'])
    if 'answer_gpt4' in item:
        list2.append(item['answer_gpt4'])
        # item['answer_gpt4'] = remove_special_characters(item['answer_gpt4'])

# Ghi dữ liệu đã được xử lý ra file JSON mới
with open(output_file_path_1, 'w', encoding='utf-8') as output_file:
    json.dump(list1, output_file, indent=4, ensure_ascii=False)
with open(output_file_path_2, 'w', encoding='utf-8') as output_file:
    json.dump(list2, output_file, indent=4, ensure_ascii=False)