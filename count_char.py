import os
def combine_chunks(chunks, max_chars):
    combined_chunks = []
    current_chunk = ""

    for chunk in chunks:
        if len(current_chunk) + len(chunk) <= max_chars:
            current_chunk += chunk
        else:
            combined_chunks.append(current_chunk)
            current_chunk = chunk

        if not current_chunk.startswith("# "):
            current_chunk_lines = current_chunk.split("\n")
            current_chunk_first_line = current_chunk_lines[0]

            for i in range(len(combined_chunks) - 1, -1, -1):
                combined_chunk_lines = combined_chunks[i].split("\n")

                for line in reversed(combined_chunk_lines):
                    if line.startswith("#") or line.startswith("##") or line.startswith("###"):
                        if line.count("#") < current_chunk_first_line.count("#"):
                            current_chunk = line + "\n" + current_chunk
                            break

                if line.startswith("#"):
                    break

                combined_chunks[i] = "\n".join(combined_chunk_lines[:-1])

    if current_chunk:
        combined_chunks.append(current_chunk)

    return combined_chunks

def count_chars_in_chunks(file_path):
    chunks = []
    current_chunk = ""

    with open(file_path, "r", encoding='utf-8') as file:
        for line in file:
            line = line.strip()

            if line.startswith("#"):
                if current_chunk:
                    chunks.append(current_chunk)
                    current_chunk = ""

            current_chunk += line + "\n"

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

# # # Sử dụng hàm count_chars_in_chunks để đếm số ký tự trong các đoạn
# file_path = "/home/longcule/Videos/rag-chatbot/docs/2023.12.01_CTDT_nganh_HTTT.md"
# chunks = count_chars_in_chunks(file_path)
# # # print(chunks)
# # # Kết hợp các chunk thành các chunk mới không vượt quá giới hạn số ký tự
# num_chars_per_chunk = 2000  # Số ký tự tối đa cho mỗi chunk
# combined_chunks = combine_chunks(chunks, num_chars_per_chunk)

# # # Lưu kết quả vào tệp văn bản
# # output_file_path = "/home/longcule/Videos/rag-chatbot/count.txt"
# # save_chunk_char_counts(combined_chunks, output_file_path)

def save_chunks_to_md_files(chunks, output_folder_path, original_file_name):
    for i, chunk in enumerate(chunks, start=1):
        file_name = f"{original_file_name}_{i}.md"
        file_path = os.path.join(output_folder_path, file_name)
        with open(file_path, "w") as file:
            file.write(chunk)

# output_folder_path = "/home/longcule/Videos/rag-chatbot/chunks"  # Đường dẫn thư mục lưu các file chunk
# original_file_name = os.path.splitext(os.path.basename(file_path))[0]  # Tên file ban đầu (loại bỏ phần mở rộng)

# save_chunks_to_md_files(combined_chunks, output_folder_path, original_file_name)

def process_md_files(input_folder_path, output_folder_path, num_chars_per_chunk):
    os.makedirs(output_folder_path, exist_ok=True)  # Tạo thư mục đầu ra nếu chưa tồn tại

    # Duyệt qua các tệp tin Markdown trong thư mục đầu vào
    for filename in os.listdir(input_folder_path):
        if filename.endswith(".md"):
            file_path = os.path.join(input_folder_path, filename)

            # Đếm số ký tự trong các đoạn và kết hợp các chunk
            chunks = count_chars_in_chunks(file_path)
            combined_chunks = combine_chunks(chunks, num_chars_per_chunk)

            # Lưu các chunk vào các file Markdown mới
            original_file_name = os.path.splitext(filename)[0]
            save_chunks_to_md_files(combined_chunks, output_folder_path, original_file_name)

# Ví dụ sử dụng
input_folder_path = "/home/longcule/Videos/rag-chatbot/docs"  # Đường dẫn thư mục chứa các file Markdown
output_folder_path = "/home/longcule/Videos/rag-chatbot/chunks"  # Đường dẫn thư mục lưu các file chunk
num_chars_per_chunk = 2000  # Số ký tự tối đa cho mỗi chunk

process_md_files(input_folder_path, output_folder_path, num_chars_per_chunk)