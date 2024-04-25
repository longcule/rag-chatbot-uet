import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

prompt = """
Hãy trích xuất các câu có liên quan từ bối cảnh được cung cấp có thể có khả năng giúp trả lời câu hỏi sau. 
Nếu không câu có liên quan được tìm thấy, hoặc nếu bạn tin rằng câu hỏi không thể được trả lời từ ngữ cảnh đã cho, trả về cụm từ "Thông tin chưa đầy đủ". 
Trong khi trích xuất các câu ứng cử viên, bạn không được phép thực hiện bất kỳ thay đổi nào đối với câu từ bối cảnh nhất định.
> Câu hỏi: {question}
> Bối cảnh:
>>>
{topic}
>>>
Câu trả lời:
"""

prompt_check_context_relevance = PromptTemplate.from_template(
"""
Với câu hỏi và ngữ cảnh sau đây, hãy trả về *CÓ* nếu bất kỳ phần nào của ngữ cảnh có liên quan để trả lời câu hỏi. 
Nếu không có ngữ cảnh nào phù hợp, hãy trả về  *KHÔNG*.

> Câu hỏi: trong chương trình học ngành khoa học máy tính, Khối kiến thức ngành có bao nhiêu tín chỉ?
> Bối cảnh:
>>>
{topic}
>>>
Câu trả lời:""")

tweet_prompt = PromptTemplate.from_template(
"""
Nhiệm vụ của bạn là hình thành chính xác 1 câu hỏi từ ngữ cảnh nhất định và đưa ra câu trả lời cho từng câu hỏi.

Kết thúc câu hỏi bằng dấu '?' ký tự và sau đó trong dòng mới viết câu trả lời cho câu hỏi đó chỉ bằng cách sử dụng bối cảnh được cung cấp.
Câu hỏi phải bắt đầu bằng "câu hỏi:".
Câu trả lời phải bắt đầu bằng "trả lời:".

Câu hỏi phải đáp ứng các quy tắc được đưa ra dưới đây:
1. Câu hỏi phải có ý nghĩa đối với con người ngay cả khi đọc mà không có ngữ cảnh nhất định.
2. Câu hỏi phải được trả lời đầy đủ trong bối cảnh nhất định.
3. Câu hỏi nên được đóng khung từ một phần bối cảnh có chứa thông tin quan trọng. Nó cũng có thể từ bảng, mã, v.v.
4. Câu trả lời cho câu hỏi không được chứa bất kỳ liên kết nào.
5. Câu hỏi phải có độ khó vừa phải.
6. Câu hỏi phải hợp lý và phải được con người hiểu và trả lời.
7. Không sử dụng các cụm từ như 'ngữ cảnh được cung cấp', v.v. trong câu hỏi
8. Tránh đặt câu hỏi bằng cách sử dụng từ "và" có thể được chia thành nhiều câu hỏi.
    
bối cảnh: {topic}
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

tweet_chain = LLMChain(llm=llm, prompt=tweet_prompt_md, verbose=True)

if __name__=="__main__":
    topic = """
**Tài liệu bắt buộc**

* Keneth Rosen, dịch giả: Phạm Văn Thiều, Đặng Hữu Thịnh, Toán rời rạc và ứng dụng trong tin học.
* Bài tập toán rời rạc của Đỗ Đức Giáo

**Tài liệu tham khảo thêm**

* Miguel A. Lerma. Notes on Discrete Mathematics. 2005.
* John A. Dossey, Albert D. Otto, Lawrence E. Spence: Discrete Mathematics, Pearson, Education, 2006.
* L. Lovasz and K. Vesztergombi: Discrete Mathematics, Lecture Notes, Yale University, Spring 1999.
"""
    resp = tweet_chain.run(topic=topic)
    print(resp)


def check_context_docs(docs, link_book):
    prompt = f"""
Tôi đã có câu trả lời ban đầu theo dạng Markdown: 
>>>
{topic}
>>>
Tôi cung cấp link đường dẫn của các cuốn sách trên như sau:
>>>
{link_book}
>>>
Nhiệm vụ của bạn là viết lại câu trả lời dưới dạng Markdown và gắn kèm link của mỗi cuốn sách, link được chèn trực tiếp vào tên cuốn sách luôn, trong quá trình tạo lại câu trả lời, không thay đổi bất kì điều gì trong câu trả lời ban đầu.
"""

# Note that each chunk may contain more than one "token"
    prompt_check_context_relevance = PromptTemplate.from_template(prompt)
    tweet_chain = LLMChain(llm=llm, prompt=prompt_check_context_relevance, verbose=True)
    resp = tweet_chain.run(topic=docs)
    print(resp)

docs = """
**Tài liệu bắt buộc**

* Keneth Rosen, dịch giả: Phạm Văn Thiều, Đặng Hữu Thịnh, Toán rời rạc và ứng dụng trong tin học.
* Bài tập toán rời rạc của Đỗ Đức Giáo

**Tài liệu tham khảo thêm**

* Miguel A. Lerma. Notes on Discrete Mathematics. 2005.
* John A. Dossey, Albert D. Otto, Lawrence E. Spence: Discrete Mathematics, Pearson, Education, 2006.
* L. Lovasz and K. Vesztergombi: Discrete Mathematics, Lecture Notes, Yale University, Spring 1999.
"""
link_book = """
"* Keneth Rosen, dịch giả: Phạm Văn Thiều, Đặng Hữu Thịnh, Toán rời rạc và ứng dụng trong tin học.": https://example.com
"* Bài tập toán rời rạc của Đỗ Đức Giáo": https://example.com
"* Miguel A. Lerma. Notes on Discrete Mathematics. 2005.": https://example.com
"* John A. Dossey, Albert D. Otto, Lawrence E. Spence: Discrete Mathematics, Pearson, Education, 2006.": https://example.com
"* L. Lovasz and K. Vesztergombi: Discrete Mathematics, Lecture Notes, Yale University, Spring 1999.": https://example.com
"""

check_context_docs(docs, link_book)