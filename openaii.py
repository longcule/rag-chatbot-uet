# insert an openai key below parameter
import os
os.environ["OPENAI_API_KEY"] = "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"

from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI



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
Bạn là một Giáo sư Đại học đang thực hiện một bài kiểm tra dành cho sinh viên giỏi. Đối với mỗi ngữ cảnh, hãy tạo một câu hỏi dành riêng cho ngữ cảnh đó. Tránh tạo ra các câu hỏi chung chung hoặc chung chung.

Câu hỏi: câu hỏi về ngữ cảnh

Format output là JSON theo hướng dẫn sau đây:
question

context: {question}
"""

prompt = PromptTemplate.from_template(qa_template)

llm = OpenAI()
# llm = OpenAI(openai_api_key="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")

question = 'a. chuẩn đầu ra ngành hệ thống thông tin 4. vị trí việc làm mà học viên có thể đảm nhiệm sau khi tốt nghiệp ngành hệ thống thông tin -   Tại cơ quan nhà nước, công nghiệp: Chuyên viên/chuyên gia khoa học dữ liệu/phân tích kinh doanh/quản lý dữ liệu lớn/thiết kế, xây dựng giải pháp và phát triển HTTT; Giám đốc thông tin (CIO); Kiến trúc sư HTTT (system architect); Chuyên gia an ninh/an toàn HTTT; Kỹ sư dữ liệu (data engineer); Lập trình viên, quản trị viên HTTT, CSDL; Lập trình viên, chuyên gia phát triển hệ thống thông minh, giải pháp full-stack; Chuyên viên/chuyên gia phát triển ứng dụng thương mại điện tử (e-commerce), chính quyền điện tử (e-government), xã hội điện tử (e-society) ... -   Tại cơ quan nghiên cứu học thuật: Nghiên cứu viên /giảng viên về Khoa học dữ liệu, HTTT và CNTT tại các Trường-Viện và các Phòng--Trung tâm nghiên cứu phát triển (R&D) tại các Tập đoàn công nghệ. -   Khởi nghiệp: hình thành công ty, tổ chức khởi nghiệp dựa trên sáng tạo giải pháp công nghệ tiên tiến về khoa học dữ liệu, nghiệp vụ, ứng dụng học máy, an toàn thông tin, ... a. chuẩn đầu ra ngành hệ thống thông tin 5. khả năng học tập, nâng cao trình độ sau khi tốt nghiệp ngành hệ thống thông tin Cử nhân tốt nghiệp ngành HTTT có đủ năng lực để tham mưu tư vấn giải pháp xây dựng, phát triển HTTT; đáp ứng tốt các yêu cầu về nghiên cứu và ứng dụng Công nghệ thông tin của xã hội. Cử nhân HTTT hoàn toàn có thể tích lũy kinh nghiệm để trở thành chuyên gia kiến trúc sư hệ thống (system architect), tư vấn giải pháp, giám đốc thông tin (CIO), ... Ngoài ra, cử nhân tốt nghiệp CTĐT HTTT chất lượng cao cũng có đủ năng lực để học tiếp lên trình độ thạc sĩ, tiến sĩ tại các trường đại học tiên tiến trong nước và trên thế giới. [PHẦN III. NỘI DUNG CHƯƠNG TRÌNH ĐÀO TẠO]'
llm_chain = LLMChain(prompt=prompt, llm=llm)

print(llm_chain.invoke(question))



