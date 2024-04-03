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


prompt = PromptTemplate.from_template(template3)

llm = OpenAI()
llm = OpenAI(openai_api_key="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")

question = 'toán rời rạc thì sao'
llm_chain = LLMChain(prompt=prompt, llm=llm)

print(llm_chain.invoke(question))


