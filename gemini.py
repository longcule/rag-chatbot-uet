
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

tweet_prompt1 = PromptTemplate.from_template(
"""
Hãy trích xuất các câu có liên quan từ ngữ cảnh được cung cấp có thể có khả năng giúp trả lời câu hỏi sau. 
Câu hỏi: Ngoài các tài liệu bắt buộc, các tài liệu tham khảo thêm nào được liệt kê cho học phần Trí tuệ nhân tạo?
Nếu không có các câu liên quan được tìm thấy, hoặc nếu bạn tin rằng câu hỏi không thể được trả lời từ ngữ cảnh đã cho, trả về cụm từ "Thông tin chưa đầy đủ". 
Trong khi trích xuất các câu ứng cử viên, bạn không được phép thực hiện bất kỳ thay đổi nào đối với câu từ bối cảnh nhất định.
Ngữ cảnh: {topic}

""")
tweet_prompt = PromptTemplate.from_template(
"""
Nhiệm vụ của bạn là đặt câu hỏi từ ngữ cảnh cho sẵn thỏa mãn các quy tắc dưới đây:
1. Câu hỏi cần được trả lời đầy đủ trong bối cảnh nhất định.
2. Câu hỏi nên được đóng khung từ một phần có chứa thông tin không tầm thường.
3. Câu trả lời không được chứa bất kỳ liên kết nào.
4. Câu hỏi phải có độ khó vừa phải.
5. Câu hỏi phải hợp lý, phải được con người hiểu và trả lời.
6. Không sử dụng các cụm từ 'cung cấp ngữ cảnh', v.v. trong câu hỏi.

Ngữ cảnh: {topic}
""")

tweet_chain = LLMChain(llm=llm, prompt=tweet_prompt, verbose=True)

if __name__=="__main__":
    topic = "3. danh mục tài liệu tham khảo ngành hệ thống thông tin Danh mục tài liệu tham khảo học phần Trí tuệ kinh doanh - Business Intelligence là: Tài liệu bắt buộc 1. Learn Power BI, A beginner’s guide to developing interactive business intelligence solutions using Microsoft Power BI, Greg Deckler, Packt Publishing, 2019. 2. Business intelligence analytics, and data science: a managerial perspective, Ramesh sharda, Dursun Delen, Efraim Turban, Pearson, 2018 Tài liệu tham khảo thêm 1. Business analytics for managers: Taking business intelligence beyond reporting, 2nd Edition by Gert H. N. Laursen & Jesper Thorlund, Wiley & SAS Business Series, 2017. 2. Learning Tableau 2019, Tools for Business Intelligence, data prep, and visual analytics, Joshua N. Milligan, Third Edition, 2019. Danh mục tài liệu tham khảo học phần Trí tuệ nhân tạo - Artificial Intelligence là: Tài liệu bắt buộc 1. Đinh Mạnh Tường. Trí tuệ nhân tạo. NXB Khoa học & Kỹ thuật, 2002 2. Russel S. and Norvig P. Artificial Intelligence: A modern approach. Prentice Hall 2008. Tài liệu tham khảo thêm 1. Ben Coppin. Artificial Intelligence Illuminated. Jones and Bartlett Publishers, 2004. Danh mục tài liệu tham khảo học phần Khoa học dịch vụ - Service Science là: Tài liệu bắt buộc 1. Hà Quang Thụy, Bài giảng Khoa học dịch vụ. Trường ĐHCN, ĐHQGHN (cập nhật hàng năm). Tài liệu tham khảo thêm 1. Mark S. Daskin. Service Science. Wiley, 2010. 2. Robin G. Qiu. Service Science: The Foundations of Service Engineering and Management. Wiley, 2014. 3. Jorge Cardoso, Rocardo Lopes, Geert Poels. Service Systems: Concepts, Modeling, and Programming. Springer, 2014. 4. Paul P. Maglio, Cheryl A. Kieliszewski, James C. Spohrer, Kelly Lyons, Lia Patricio, Yuriko Sawatani. Handbook of Service Science (Volume II). Springer, 2019. 5. Các bài báo, sách cập nhật về khoa học dịch vụ là tài liệu tiểu luận"
    resp = tweet_chain.run(topic=topic)
    print(resp)