from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import json


def merge_books(titles):
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

def count_blank(example_text):
    count = 0
    for char in example_text[1:]: 
        if char == ' ':
            count += 1
        else:
            break
    return count


def calculate_cosine_similarity(text, dictionary):
    # Tạo danh sách các item và liên kết tương ứng
    items = []
    item_links = []
    item_contents = []
    for key, value in dictionary.items():
        if key.endswith("_link"):
            continue
        items.append(value)
        item_links.append(dictionary[key + "_link"])
    
    lines = text.split("\n")  # Tách văn bản thành các dòng riêng biệt
    line_list = []  # Danh sách để lưu trữ các dòng

    for line in lines:
        line_list.append(line)
    
    # print(line_list)
    # Tính toán ma trận TF-IDF của các item trong từ điển và dòng văn bản
    vectorizer = TfidfVectorizer()
    item_vectors = vectorizer.fit_transform(items)
    text_vectors = vectorizer.transform(text.split('\n'))

    # Tính toán cosine similarity giữa mỗi dòng văn bản và các item trong từ điển
    similarities = cosine_similarity(item_vectors, text_vectors)

    # Lấy ra index của item có cosine similarity cao nhất cho mỗi dòng văn bản
    max_indices = np.argmax(similarities, axis=0)

    # Lấy ra item, liên kết, nội dung và điểm số tương ứng cho mỗi dòng văn bản
    max_items = [items[index] for index in max_indices]
    max_item_links = [item_links[index] for index in max_indices]
    # max_item_contents = [item_contents[index] for index in max_indices]
    max_scores = [similarities[index, i] for i, index in enumerate(max_indices)]


    for i, line in enumerate(lines):
        if max_scores[i] > 0.6:
            # print(line)
            modified_line = f"[{line}]({max_item_links[i]})"
            # line = modified_line
            num_spaces = count_blank(modified_line)
            modified_line = modified_line[1:num_spaces+2]+" "+modified_line[0]+modified_line[num_spaces+3:]
            lines[i] = modified_line
        
        lines[i] = lines[i] + "  "
    
    text_modified = "\n".join(line for line in lines)

    return text_modified


def modified_response(list_docs, response):
    data = merge_books(list_docs)
    result = calculate_cosine_similarity(response, data)
    return result

# text = """
# **Tài liệu bắt buộc**

# * Keneth Rosen, dịch giả: Phạm Văn Thiều, Đặng Hữu Thịnh, Toán rời rạc và ứng dụng trong tin học.
# * Bài tập toán rời rạc của Đỗ Đức Giáo

# **Tài liệu tham khảo thêm**

# * Miguel A. Lerma. Notes on Discrete Mathematics. 2005.
# * John A. Dossey, Albert D. Otto, Lawrence E. Spence: Discrete Mathematics, Pearson, Education, 2006.
# * L. Lovasz and K. Vesztergombi: Discrete Mathematics, Lecture Notes, Yale University, Spring 1999.
# """

# dictionary = {
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_3": "William Stallings, Computer Organization and Architecture. Prentice Hall; 11th Edition, Prentice Hall, 2019.",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_3_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_4": "Nguyễn Đình Việt, Kiến trúc máy tính, NXB ĐHQGHN, 2009.",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_4_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_6": "John L. Hennessy & David A. Patterson, Computer Architecture, A quantitative approach, Morgan Kaufmann, 6th edition 2019.",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_6_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_7": "Pranabananda Chakraborty, Computer Organisation and Architecture Evolutionary Concepts, Principles, and Designs Published October 29, 2020 by Chapman and Hall/CRC.",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_7_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_10": "Toán rời rạc và ứng dụng trong tin học, Keneth Rosen, dịch giả: Phạm Văn Thiều, Đặng Hữu Thịnh.",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_10_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_11": "Bài tập toán rời rạc của Đỗ Đức Giáo",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_11_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_13": "Miguel A. Lerma. Notes on Discrete Mathematics. 2005.",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_13_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_14": "John A. Dossey, Albert D. Otto, Lawrence E. Spence: Discrete Mathematics, Pearson, Education, 2006",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_14_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_15": "L. Lovasz and K. Vesztergombi: Discrete Mathematics, Lecture Notes, Yale University, Spring 1999",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_15_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_16": "Andrew S. Tanenbaum, Albert S Woodhull, Operating Systems: Design and Implementation, 3rd edition, Prentice-Hall. 2006.",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_16_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_17": "Robert Love, Linux Kernel Development, Sams Publishing, 2003.",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_17_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_18": "Daniel P. Bovet, Marco Cesati, Understanding Linux Kernel, 2nd edition, O'Reilly & Associates, 2002.",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_18_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_19": "W. Richard Stevens, Advanced Programming in the UNIX Environment, Addison-Wesley, 1992.",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_19_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_22": "Abraham Silberschatz, Peter Baer Galvin, Greg GagneOperating System Concepts,10th edition, John Wiley & Sons, Inc., 2018",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_22_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_24": "Andrew S. Tanenbaum, Modern Operating Systems, 4th edition, Pearson, 2016.",
#     "item_CTDT_nganh_CNTT_CLC_20230928_23.md_24_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_3": "William Stallings, Computer Organization and Architecture. Prentice Hall; 11th Edition, Prentice Hall, 2019.",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_3_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_4": "Nguyễn Đình Việt, Kiến trúc máy tính, NXB ĐHQGHN, 2009.",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_4_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_6": "John L. Hennessy & David A. Patterson, Computer Architecture, A quantitative approach, Morgan Kaufmann, 6th edition 2019.",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_6_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_7": "Pranabananda Chakraborty, Computer Organisation and Architecture Evolutionary Concepts, Principles, and Designs Published October 29, 2020 by Chapman and Hall/CRC.",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_7_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_10": "Keneth Rosen, dịch giả: Phạm Văn Thiều, Đặng Hữu Thịnh, Toán rời rạc và ứng dụng trong tin học.",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_10_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_11": "Bài tập toán rời rạc của Đỗ Đức Giáo",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_11_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_13": "Miguel A. Lerma. Notes on Discrete Mathematics. 2005.",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_13_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_14": "John A. Dossey, Albert D. Otto, Lawrence E. Spence: Discrete Mathematics, Pearson, Education, 2006.",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_14_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_15": "L. Lovasz and K. Vesztergombi: Discrete Mathematics, Lecture Notes, Yale University, Spring 1999.",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_15_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_18": "Abraham Silberschatz, Peter Baer Galvin, Greg GagneOperating System Concepts,10th edition, John Wiley & Sons, Inc., 2018.",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_18_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_20": "Andrew S. Tanenbaum, Modern Operating Systems, 4th edition, Pearson, 2016.",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_20_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_23": "Hồ Đắc Phương, Mạng máy tính. NXB ĐHQGHN, 2009.",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_23_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_24": "Kurose & Ross, Networking a top down approach, Pearson Publisher, 7th Edition",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_24_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_26": "Các bài báo của IEEE do giảng viên cung cấp.",
#     "item_2023.12.01_CTDT_nganh_KHMT_23.md_26_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_3": "William Stallings, Computer Organization and Architecture. Prentice Hall; 11th Edition, Prentice Hall, 2019.",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_3_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_4": "Nguyễn Đình Việt, Kiến trúc máy tính, NXB ĐHQGHN, 2009.",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_4_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_6": "John L. Hennessy & David A. Patterson, Computer Architecture, A quantitative approach, Morgan Kaufmann, 6th edition 2019.",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_6_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_7": "Pranabananda Chakraborty, Computer Organisation and Architecture Evolutionary Concepts, Principles, and Designs Published October 29, 2020 by Chapman and Hall/CRC.",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_7_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_10": "Keneth Rosen, dịch giả: Phạm Văn Thiều, Đặng Hữu Thịnh, Toán rời rạc và ứng dụng trong tin học.",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_10_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_11": "Bài tập toán rời rạc của Đỗ Đức Giáo",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_11_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_13": "Miguel A. Lerma. Notes on Discrete Mathematics. 2005.",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_13_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_14": "John A. Dossey, Albert D. Otto, Lawrence E. Spence: Discrete Mathematics, Pearson, Education, 2006.",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_14_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_15": "L. Lovasz and K. Vesztergombi: Discrete Mathematics, Lecture Notes, Yale University, Spring 1999.",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_15_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_18": "Abraham Silberschatz, Peter Baer Galvin, Greg GagneOperating System Concepts,10th edition, John Wiley & Sons, Inc., 2018.",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_18_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_20": "Andrew S. Tanenbaum, Modern Operating Systems, 4th edition, Pearson, 2016.",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_20_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_23": "Hồ Đắc Phương, Mạng máy tính. NXB ĐHQGHN, 2009.",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_23_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_24": "Kurose & Ross, Networking a top down approach, Pearson Publisher, 7th Edition",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_24_link": "https://example.com",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_26": "Các bài báo của IEEE do giảng viên cung cấp.",
#     "item_2023.12.01_CTDT_nganh_MMT_TTDL_23.md_26_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_3": "William Stallings, Computer Organization and Architecture. Prentice Hall; 11th Edition, Prentice Hall, 2019.",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_3_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_4": "Nguyễn Đình Việt, Kiến trúc máy tính, NXB ĐHQGHN, 2009.",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_4_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_6": "John L. Hennessy & David A. Patterson, Computer Architecture, A quantitative approach, Morgan Kaufmann, 6th edition 2019.",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_6_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_7": "Pranabananda Chakraborty, Computer Organisation and Architecture Evolutionary Concepts, Principles, and Designs Published October 29, 2020 by Chapman and Hall/CRC.",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_7_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_10": "Toán rời rạc và ứng dụng trong tin học, Keneth Rosen, dịch giả: Phạm Văn Thiều, Đặng Hữu Thịnh.",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_10_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_11": "Bài tập toán rời rạc của Đỗ Đức Giáo",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_11_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_13": "Miguel A. Lerma. Notes on Discrete Mathematics. 2005.",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_13_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_14": "John A. Dossey, Albert D. Otto, Lawrence E. Spence: Discrete Mathematics, Pearson, Education, 2006",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_14_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_15": "L. Lovasz and K. Vesztergombi: Discrete Mathematics, Lecture Notes, Yale University, Spring 1999",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_15_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_16": "Andrew S. Tanenbaum, Albert S Woodhull, Operating Systems: Design and Implementation, 3rd edition, Prentice-Hall. 2006.",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_16_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_17": "Robert Love, Linux Kernel Development, Sams Publishing, 2003.",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_17_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_18": "Daniel P. Bovet, Marco Cesati, Understanding Linux Kernel, 2nd edition, O'Reilly & Associates, 2002.",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_18_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_19": "W. Richard Stevens, Advanced Programming in the UNIX Environment, Addison-Wesley, 1992.",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_19_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_22": "Abraham Silberschatz, Peter Baer Galvin, Greg GagneOperating System Concepts,10th edition, John Wiley & Sons, Inc., 2018",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_22_link": "https://example.com",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_24": "Andrew S. Tanenbaum, Modern Operating Systems, 4th edition, Pearson, 2016.",
#     "item_CTDT_nganh_CNTT_dinh_huong_thi_truong_Nhat_Ban_20230928_20.md_24_link": "https://example.com"
# }

# text_md = calculate_cosine_similarity(text, dictionary)
# print(text_md)

