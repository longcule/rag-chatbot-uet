import os, json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

prompt = PromptTemplate.from_template(
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
prompt1 = """
Bạn là một trợ lý hữu ích, tôn trọng và trung thực.
Thông tin bối cảnh dưới đây về các học phần hoặc chương trình đào tạo trong trường đại học Công Nghệ.
---------------------
{context}
---------------------
Dựa vào thông tin ngữ cảnh chứ không phải kiến ​​thức có sẵn, hãy tận dụng tất cả thông tin có được và trả lời câu hỏi dưới đây, hãy trả lời một cách lịch sự và lễ phép:
Câu hỏi như sau: {question}
"""
prompt_check_context_relevance = PromptTemplate.from_template(
"""
Nhiệm vụ của bạn là viết một câu hỏi thực tế và một câu trả lời dựa trên ngữ cảnh.
Câu hỏi thực tế của bạn phải được trả lời bằng một đoạn thông tin thực tế cụ thể, ngắn gọn từ ngữ cảnh.
Câu hỏi thực tế của bạn phải được xây dựng theo phong cách giống như những câu hỏi mà người dùng có thể hỏi trong công cụ tìm kiếm.
Điều này có nghĩa là câu hỏi thực tế của bạn "KHÔNG PHẢI" đề cập đến những thứ như "theo đoạn văn" hoặc "ngữ cảnh".

Cung cấp câu trả lời của bạn như sau:

Đầu ra:::
Câu hỏi thực tế: (câu hỏi thực tế của bạn)
Trả lời: (câu trả lời của bạn cho câu hỏi thực tế)

Bây giờ đây là bối cảnh.

Bối cảnh: {topic}\n
Đầu ra:::""")

tweet_prompt = PromptTemplate.from_template(
"""
Nhiệm vụ của bạn là hình thành chính xác 1 câu hỏi từ ngữ cảnh nhất định và đưa ra câu trả lời cho câu hỏi đó.

Kết thúc câu hỏi bằng dấu '?' ký tự và sau đó trong dòng mới viết câu trả lời cho câu hỏi đó chỉ bằng cách sử dụng bối cảnh được cung cấp.

Câu hỏi phải đáp ứng các quy tắc được đưa ra dưới đây:
1. Câu hỏi thực tế của bạn phải được xây dựng theo phong cách giống như những câu hỏi mà người dùng có thể hỏi trong công cụ tìm kiếm.
2. Câu hỏi phải có ý nghĩa đối với con người ngay cả khi đọc mà không có ngữ cảnh nhất định.
3. Câu hỏi phải được trả lời đầy đủ trong bối cảnh nhất định.
4. Câu hỏi nên được đóng khung từ một phần bối cảnh có chứa thông tin quan trọng. Nó cũng có thể từ bảng, mã, v.v.
5. Câu trả lời cho câu hỏi không được chứa bất kỳ liên kết nào.
6. Câu hỏi phải có độ khó vừa phải.
7. Câu hỏi phải hợp lý và phải được con người hiểu và trả lời.
8. Không sử dụng các cụm từ như 'ngữ cảnh được cung cấp', v.v. trong câu hỏi
9. Tránh đặt câu hỏi bằng cách sử dụng từ "và" có thể được chia thành nhiều câu hỏi.
10. Câu hỏi của bạn "KHÔNG PHẢI" đề cập đến những thứ như "theo đoạn văn" hoặc "ngữ cảnh".

Cung cấp câu trả lời của bạn như sau:

Đầu ra:::
Câu hỏi thực tế: (câu hỏi thực tế của bạn)
Trả lời: (câu trả lời của bạn cho câu hỏi thực tế)

Bây giờ đây là bối cảnh.

Bối cảnh: {topic}\n
Đầu ra:::
""")

tweet_prompt_md = PromptTemplate.from_template(
"""
Tôi đã có câu trả lời ban đầu theo dạng Markdown: 
>>>
{topic}
>>>
Tôi cung cấp link đường dẫn của các cuốn sách trên như sau:
>>>

>>>
Nhiệm vụ của bạn là viết lại câu trả lời dưới dạng Markdown và gắn kèm link của mỗi cuốn sách, link được chèn trực tiếp vào tên cuốn sách luôn, trong quá trình tạo lại câu trả lời, không thay đổi bất kì điều gì trong câu trả lời ban đầu.
"""
)

tweet_chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

if __name__=="__main__":
    topic = """
5. tóm tắt nội dung học phần: phân tích kinh doanh\nHọc phần trước tiên đề cập đến vai trò quan trọng của phân tích kinh doanh ở các doanh nghiệp trong thời kỳ chuyển đổi số. Tiếp theo là các phần nội dung cụ thể như hiểu dữ liệu kinh doanh; tiền xử lý và biến đổi dữ liệu; các kỹ thuật và phương pháp phân tích mô tả; các kỹ thuật và phương pháp phân tích dự báo; các kỹ thuật và phương pháp phân tích khuyến nghị; trực quan hoá dữ liệu ... Các nội dung trong học phần này có nhiều kiến thức giao thoa với lĩnh vực như thống kê (statistics) khai phá dữ liệu (data mining) học máy (machine learning) cũng như vận trù học (operations research). Bên cạnh các vấn đề kỹ thuật học phần cũng chú trọng định hướng cho sinh viên việc tiếp cận hiểu và giải quyết các vấn đề thực tiễn trong thương mại và kinh doanh. Học phần sẽ định hướng sinh viên thực hành trên một số công cụ tiện dụng quen thuộc nhưng được trang bị nhiều tính năng phân tích dữ liệu như Microsoft Excel cũng như lập trình phân tích dữ liệu với ngôn ngữ lập trình Python hay R.
"""
    resp = tweet_chain.run(topic=topic)
    print(resp)


# def create_qa_dataset(docs):
#     tweet_chain = LLMChain(llm=llm, prompt=prompt_check_context_relevance, verbose=True)
#     resp = tweet_chain.run(topic=docs)

# def create_qa_dataset_from_folder(folder_path, num_iterations=3):
#     qa_pairs = []

#     # Lặp qua các tệp tin trong thư mục
#     for file_name in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, file_name)
#         if os.path.isfile(file_path) and file_name.endswith(".md"):
#             with open(file_path, "r", encoding="utf-8") as file:
#                 content = file.read()
#                 print(content)
#                 # Chạy vòng lặp để gọi llm và lấy response
#                 for i in range(num_iterations):
#                     tweet_chain = LLMChain(llm=llm, prompt=tweet_prompt, verbose=True)
#                     resp = tweet_chain.run(topic=content)
#                     lines = resp.split("\n")
#                     question = lines[0].split(":")[1].strip()
#                     answer = lines[1].split(":")[1].strip()
#                     # Chuyển đổi câu hỏi và trả lời thành danh sách các cặp câu hỏi và trả lời

#                     # for question, answer in resp:
#                     qa_pairs.append({"question": question, "answer": answer, "file_path": file_path})

#                 # Lưu câu hỏi và trả lời vào tệp JSON
#                 with open("qa_dataset_gemini.json", "w", encoding='utf-8') as json_file:
#                     json.dump(qa_pairs, json_file, ensure_ascii=False)

#     print("Tập dữ liệu câu hỏi và trả lời đã được lưu vào qa_dataset.json")


# # Nhập vào đường dẫn thư mục chứa các tệp tin txt
# folder_path = "docs"
# # Thay thế "đường_dẫn_thư_mục" bằng đường dẫn thư mục thực tế của bạn

# # Gọi hàm create_qa_dataset_from_folder với thư mục đã cho và số lần lặp
# create_qa_dataset_from_folder(folder_path, num_iterations=5)


# def check_context_docs(context, question):
#     prompt = f"""
# Bạn là một trợ lý hữu ích, tôn trọng và trung thực.
# Thông tin bối cảnh dưới đây về các học phần hoặc chương trình đào tạo trong trường đại học Công Nghệ.
# ---------------------
# {context}
# ---------------------
# Dựa vào thông tin ngữ cảnh chứ không phải kiến ​​thức có sẵn, hãy tận dụng tất cả thông tin có được và trả lời câu hỏi dưới đây, hãy trả lời một cách lịch sự và lễ phép:
# Câu hỏi như sau: {question}
# """
#     print(context, question)
# # Note that each chunk may contain more than one "token"
#     prompt_check_context_relevance = PromptTemplate.from_template(prompt)
#     tweet_chain = LLMChain(llm=llm, prompt=prompt_check_context_relevance, verbose=True)
#     resp = tweet_chain.run(topic=question)
#     # print(resp)
#     return resp

# # Đọc file JSON
# with open('/home/longcule/Videos/rag-chatbot/chatbot/output_rag_1.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)

# ans_1 = []
# for item in data:
#     question = item['question']
#     file_path = item['file_path']
    
#     # Đọc nội dung từ file
#     with open(file_path, 'r', encoding='utf-8') as file:
#         context = file.read()
    
#     # print("context: ", context, "question: ", question)
#     # Kiểm tra và lưu câu trả lời
#     # resp = check_context_docs(context, question)
#     # ans_1.append(resp)
#     ans_1.append({"question": question, "file_path_target": file_path})


#     # Lưu kết quả vào file mới
#     with open('retrieve_testset.json', 'w', encoding='utf-8') as file:
#         json.dump(ans_1, file, ensure_ascii=False)


# docs = """
# # 5. hướng dẫn thực hiện chương trình đào tạo ngành công nghệ thông tin chuẩn
# ## các môn học sẽ học trong học kỳ 5 chương trình đào tạo ngành công nghệ thông tin chuẩn
# STT,Mã học phần,Học phần,Số tín chỉ
# 1,PEC1008,"Kinh tế chính trị Mác – Lênin - Marx-Lenin Political Economy",2
# 2,INT3201,"Cơ sở các hệ thống thông tin  - Foundation of Information Systems",4
# 3,HIS1001,"Lịch sử Đảng Cộng sản Việt Nam - Revolutionary Guidelines of Vietnam Communist Party",2
# 4,INT3209E,"Khai phá dữ liệu  - Data Mining",3
# 5-6,,02 học phần khối V.2,6-8
# 7,INT3228E,"Thiết kế và phân tích thực nghiệm - Design and Analysis of Experiments",4
# INT3230E,"Mật mã và An toàn thông tin - Cryptography and Information security",4
# INT3506E,"Các hệ thống thương mại điện tử - E-commerce Systems",3
# INT3501E,"Khoa học dịch vụ - Service Science",3
# INT3505,"Kiến trúc hướng dịch vụ - Service-Oriented Architectures",3
# INT3401,"Trí tuệ nhân tạo  - Artificial Intelligence",3
# INT3306,"Phát triển ứng dụng Web - Web application development",3
# Tổng: 17-19 tín chỉ
# ## các môn học sẽ học trong học kỳ 6 chương trình đào tạo ngành công nghệ thông tin chuẩn
# STT,Mã học phần,Học phần,Số tín chỉ
# 1,POL1001,"Tư tưởng Hồ Chí Minh - Ho Chi Minh's Ideology",2
# 2,INT2214,"Nguyên lý hệ điều hành- Principles of operating systems",4
# 3,INT2020E,"Phân tích thiết kế các hệ thống thông tin - Information System Analysis and Design",3
# 4-5,,02 học phần khối V.2,6-8
# 6,INT3229E,"Kỹ thuật và công nghệ dữ liệu lớn- BigData Techniques and Technologies",4
# INT3231E,"Công nghệ Blockchain - Blockchain and Distributed Ledger Technologies",4
# INT3235E,"Phân tích mạng phương tiện xã hội trong kinh doanh - Social Media Network Analysis for Business",4
# INT2045E,"Quản lý dự án HTTT - Information System Project Management",4
# INT3224E,"Trí tuệ kinh doanh - Business Intelligence",4
# Tổng: 15-17 tín chỉ
# """
# question = """
# Trong chương trình đào tạo ngành công nghệ thông tin chuẩn, môn học nào được giảng dạy trong học kỳ 5?
# """

# check_context_docs(docs, question)