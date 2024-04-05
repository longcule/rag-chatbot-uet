def split_md_file(file_path, max_chars_per_chunk):
    chunks = []
    current_chunk = ""
    current_chunk_char_count = 0

    with open(file_path, "r", encoding='utf-8') as file:
        for line in file:
            line = line.strip()

            if line.startswith("#"):
                if current_chunk:
                    chunks.append(current_chunk)
                    current_chunk = ""
                    current_chunk_char_count = 0

            current_chunk += line + "\n"
            current_chunk_char_count += len(line) + 1  # +1 for the newline character

            # Kiểm tra nếu tổng số ký tự vượt quá giới hạn cho mỗi chunk
            if current_chunk_char_count > max_chars_per_chunk:
                last_line_char_count = len(line) + 1  # +1 for the newline character

                # Nếu tổng số ký tự của dòng hiện tại vượt quá giới hạn, tạo một chunk mới
                if last_line_char_count > max_chars_per_chunk:
                    chunks.append(current_chunk)
                    current_chunk = ""
                    current_chunk_char_count = 0
                else:
                    # Di chuyển dòng hiện tại vào chunk mới
                    chunks.append(current_chunk[:-last_line_char_count])
                    current_chunk = line + "\n"
                    current_chunk_char_count = last_line_char_count

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def save_chunks_to_file(chunks, output_file_path):
    with open(output_file_path, "w") as file:
        for i, chunk in enumerate(chunks, start=1):
            file.write(f"Chunk {i}:\n{chunk}\n\n")

# Sử dụng hàm split_md_file để phân chia file
file_path = "/home/longcule/Videos/rag-chatbot/docs/2023.12.01_CTDT_nganh_HTTT.md"
max_chars_per_chunk = 1000  # Số lượng ký tự tối đa cho mỗi chunk
chunks = split_md_file(file_path, max_chars_per_chunk)

# Lưu các chunks vào tệp văn bản
output_file_path = "/home/longcule/Videos/rag-chatbot/chunk.txt"
save_chunks_to_file(chunks, output_file_path)