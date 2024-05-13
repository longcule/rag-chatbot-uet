# insert an openai key below parameter
import os
OPENAI_API_KEY = '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'
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI
llm = OpenAI(model="gpt-4-turbo", openai_api_key=OPENAI_API_KEY)



template = """
cho danh sách các đầu mục dưới đây: 
"
Thông tin về các giảng viên học phần
Thông tin chung về học phần
Mục tiêu học phần
Chuẩn đầu ra
Tóm tắt nội dung học phần
Nội dung chi tiết học phần
Học liệu 
Hình thức tổ chức dạy học
Chính sách đối với học phần và các yêu cầu khác của giảng viên
Phương pháp, hình thức kiểm tra, đánh giá kết quả học tập học phần
"
Khi tôi có câu hỏi, bạn hãy nêu ra những đầu mục liên quan tới câu hỏi cho tôi, 
câu trả lời có dạng như sau: "đầu mục liên quan là: danh sách đầu mục liên quan tới câu hỏi", 
không trả lời thừa so với những gì tôi đưa ra, chỉ nêu đề mục liên quan trong list trên, nhiều nhất là 3 đề mục, nếu câu hỏi không có liên quan đến các đề mục thì hãy trả lời là không tìm thấy.
Câu hỏi là: {question}
"""

template2 = """
Hãy thực hiện theo yêu cầu dưới đây của tôi:
Khi tôi có câu hỏi, chỉ ra môn học nói đến trong câu hỏi đó, 
câu trả lời chỉ gồm tên môn học, không có thông tin vào khác, câu trả lời sẽ có dạng: "Tên môn học liên quan(chỉ là tên thôi)"
không trả lời thừa so với những gì tôi đưa ra, chỉ trả lời tên môn học bằng tiếng việt, không nói tiếng anh, chỉ nêu tên môn học liên quan.
Câu hỏi là: {question}
"""
template3 = """
cho danh sách các câu hỏi trong cuộc trò chuyện trước đây từ người dùng: 
"
Nhập môn lập trình sẽ học những gì

"
Câu hỏi là: {question}
Với cuộc trò chuyện trên và một câu hỏi tiếp theo, hãy diễn đạt lại câu hỏi tiếp theo thành một câu hỏi độc lập
"""

qa_template = """\
Hãy trích xuất các câu có liên quan từ bối cảnh được cung cấp có thể có khả năng giúp trả lời câu hỏi sau. 
Nếu không câu có liên quan được tìm thấy, hoặc nếu bạn tin rằng câu hỏi không thể được trả lời từ ngữ cảnh đã cho, trả về cụm từ "Thông tin chưa đầy đủ". 
Trong khi trích xuất các câu ứng cử viên, bạn không được phép thực hiện bất kỳ thay đổi nào đối với câu từ bối cảnh nhất định.
> Câu hỏi: {question}
> Bối cảnh:
>>>
# 6. nội dung chi tiết học phần phân tích và thiết kế hướng đối tượng
Học phần bao gồm các nội dung chính như sau: Chương 1. Bộ kinh nghiệm về phát triển phần mềm 1.1. Phát triển tăng dần 1.2. Quản lý yêu cầu 1.3. Kiến trúc hướng thành phần 1.4. Mô hình hóa trực quan 1.5. Kiểm chứng chất lượng 1.6. Quản lý thay đổi 1.7. Giới thiệu quy trình phát triển RUP Chương 2. Mô hình hóa hướng đối tượng 2.1. Lược đồ hướng đối tượng 2.2. Biểu diễn lược đồ bằng ngôn ngữ mô hình UML Chương 3. Tổng quan về yêu cầu phần mềm 3.1. Giới thiệu 3.2. Các khái niệm chính 3.3. Mô hình ca sử dụng 3.4. Đặc tả các yêu cầu chức năng và phi chức năng khác 3.5. Từ điển thuật ngữ Chương 4. Tổng quan về phân tích và thiết kế 4.1. Các khái niệm chính 4.2. Luồng công việc phân tích và thiết kế Chương 5. Phân tích kiến trúc 5.1. Tổng quan về phân tích kiến trúc 5.2. Các khái niệm chính 5.3. Tổ chức mức cao của các hệ thống con 5.4. Xác định các cơ chế phân tích 5.5. Xác định các trừu tượng hóa chính 5.6. Tạo các hiện thực hóa ca sử dụng Chương 6. Phân tích ca sử dụng 6.1. Tổng quan về phân tích ca sử dụng 6.2. Chính xác hóa các mô tả ca sử dụng 6.3. Tìm các lớp từ hành vi ca sử dụng 6.4. Phân bổ hành vi ca sử dụng cho các lớp 6.5. Mô tả các trách nhiệm 6.6. Mô tả các thuộc tính và liên kết 6.7. Các bước phân tích ca sử dụng 6.8. Thống nhất các lớp phân tích Chương 7. Xác định các phần tử thiết kế 7.1. Tổng quan về xác định các phần tử thiết kế 7.2. Xác định các lớp và các hệ thống con 7.3. Xác định các giao diện hệ thống con 7.4. Xác định các cơ hội sử dụng lại 7.5. Cập nhật lại mô hình thiết kế Chương 8. Xác định các cơ chế thiết kế 8.1. Tổng quan về xác định các cơ chế thiết kế 8.2. Phân loại các nhóm sử dụng cơ chế phân tích 8.3. Làm tài liệu cơ chế kiến trúc Chương 9. Mô tả kiến trúc thực thi và phân tán 9.1. Tổng quan về thiết kế kiến trúc 9.2. Mô tả kiến trúc thực thi 9.3. Mô tả kiến trúc phân tán Chương 10. Thiết kế ca sử dụng 10.1. Tổng quan về thiết kế ca sử dụng 10.2. Mô tả tương tác giữa các đối tượng thiết kế 10.3. Đơn giản hóa biểu đồ tuần tự sử dụng các hệ thống con 10.4. Mô tả hành vi liên quan đến lưu trữ lâu bền 10.5. Làm mịn mô tả luồng sự kiện 10.6. Thống nhất các lớp và các hệ thống con Chương 11. Thiết kế hệ thống con 11.1. Tổng quan về thiết kế hệ thống con 11.2. Phân bố hành vi của hệ thống con cho các phần tử của nó 11.3. Làm tài liệu các phần tử của hệ thống con 11.4. Mô tả các phụ thuộc giữa các hệ thống con Chương 12. Thiết kế lớp 12.1. Tổng quan về thiết kế lớp 12.2. Hình thành các lớp thiết kế 12.3. Xác định biểu đồ lớp thiết kế 12.4. Xác định các biểu đồ trạng thái 12.5. Dung hòa các xung đột giữa các ca sử dụng 12.6. Điều khiển các yêu cầu phi chức năng 12.7. Ánh xạ lớp lưu trữ lâu bền vào cơ sở dữ liệu
>>>
Câu trả lời:
"""

tweet_prompt = PromptTemplate.from_template(
"""
Hãy trích xuất các câu có liên quan từ bối cảnh được cung cấp có thể có khả năng giúp trả lời câu hỏi sau. 
Nếu không câu có liên quan được tìm thấy, hoặc nếu bạn tin rằng câu hỏi không thể được trả lời từ ngữ cảnh đã cho, trả về cụm từ "Thông tin chưa đầy đủ". 
Trong khi trích xuất các câu ứng cử viên, bạn không được phép thực hiện bất kỳ thay đổi nào đối với câu từ bối cảnh nhất định.
> Câu hỏi: Học phần phân tích kinh doanh tập trung vào những lĩnh vực nào ngoài các vấn đề kỹ thuật?
> Bối cảnh:
>>>
{topic}
>>>
Câu trả lời:
"""
)
def create_qa_dataset_from_folder(folder_path, num_iterations=3):
    qa_pairs = []

    # Lặp qua các tệp tin trong thư mục
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name.endswith(".md"):
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                print(content)
                # Chạy vòng lặp để gọi llm và lấy response
                for i in range(num_iterations):
                    tweet_chain = LLMChain(llm=llm, prompt=tweet_prompt, verbose=True)
                    resp = tweet_chain.run(topic=content)
                    lines = resp.split("\n")
                    question = lines[0].split(":")[1].strip()
                    answer = lines[1].split(":")[1].strip()
                    # Chuyển đổi câu hỏi và trả lời thành danh sách các cặp câu hỏi và trả lời

                    # for question, answer in resp:
                    qa_pairs.append({"question": question, "answer": answer, "file_path": file_path})

                # Lưu câu hỏi và trả lời vào tệp JSON
                with open("qa_dataset_gemini.json", "w", encoding='utf-8') as json_file:
                    json.dump(qa_pairs, json_file, ensure_ascii=False)

    print("Tập dữ liệu câu hỏi và trả lời đã được lưu vào qa_dataset.json")

# prompt = PromptTemplate.from_template(qa_template)

# llm = OpenAI()
# # llm = OpenAI(openai_api_key="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")

# question = 'Học phần phân tích thiết kế hướng đối tượng bao gồm các nội dung chính nào?'
# llm_chain = LLMChain(prompt=prompt, llm=llm)

# print(llm_chain.invoke(question))


