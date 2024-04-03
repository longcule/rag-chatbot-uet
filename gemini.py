
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

tweet_prompt = PromptTemplate.from_template(
"""
cho danh sách các đầu mục dưới đây: 
"
Thông tin về các giảng viên học phần:
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
Khi tôi có câu hỏi, bạn hãy nêu ra những đầu mục liên quan tới câu hỏi cho tôi, câu trả lời có dạng như sau: "đầu mục liên quan là: danh sách đầu mục liên quan tới câu hỏi", không trả lời thừa so với những gì tôi đưa ra, chỉ nêu đề mục liên quan trong list trên.
Câu hỏi là: 
""")

tweet_chain = LLMChain(llm=llm, prompt=tweet_prompt, verbose=True)

if __name__=="__main__":
    topic = "Hãy cho tôi biết về giảng viên môn nhập môn lập trình?"
    resp = tweet_chain.run(topic=topic)
    print(resp)