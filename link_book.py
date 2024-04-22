import os
import json
import re

def process_md_files(folder_path):
    data = []
    
    for filename in os.listdir(folder_path):
        if filename.endswith('.md'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                
                title = os.path.splitext(filename)[0]
                book = {}
                
                for i, line in enumerate(lines):
                    line = line.strip()
                    match = re.match(r'^([1-7]\. |\- )(.*)', line)
                    if match:
                        item = f'item_{filename}_{i}'
                        item_link = 'https://example.com'
                        book[item] = match.group(2)
                        book[f'{item}_link'] = item_link
                
                if book:
                    entry = {
                        'title': title,
                        'book': book
                    }
                    data.append(entry)
    
    with open('output.json', 'w', encoding='utf-8') as output_file:
        json.dump(data, output_file, indent=4, ensure_ascii=False)

# Thay đổi đường dẫn thư mục của bạn tại đây
folder_path = '/home/longcule/Videos/rag-chatbot/docs_book'

process_md_files(folder_path)