import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import asyncio
import google.generativeai as genai
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)

# prompt = """
# Với câu hỏi và ngữ cảnh sau đây, hãy trả về *CÓ* nếu bất kỳ phần nào của ngữ cảnh có liên quan để trả lời câu hỏi. 
# Nếu không có ngữ cảnh nào phù hợp, hãy trả về  *KHÔNG*.

# > Câu hỏi: {question}
# > Bối cảnh:
# >>>
# {topic}
# >>>
# Câu trả lời:
# """

# prompt_check_context_relevance = PromptTemplate.from_template(
# """
# Với câu hỏi và ngữ cảnh sau đây, hãy trả về *CÓ* nếu bất kỳ phần nào của ngữ cảnh có liên quan để trả lời câu hỏi. 
# Nếu không có ngữ cảnh nào phù hợp, hãy trả về  *KHÔNG*.

# > Câu hỏi: trong chương trình học ngành khoa học máy tính, Khối kiến thức ngành có bao nhiêu tín chỉ?
# > Bối cảnh:
# >>>
# {topic}
# >>>
# Câu trả lời:""")

# tweet_prompt = PromptTemplate.from_template(
# """
# Nhiệm vụ của bạn là đặt câu hỏi từ ngữ cảnh cho sẵn thỏa mãn các quy tắc dưới đây:
# 1. Câu hỏi cần được trả lời đầy đủ trong bối cảnh nhất định.
# 2. Câu hỏi nên được đóng khung từ một phần có chứa thông tin không tầm thường.
# 3. Câu trả lời không được chứa bất kỳ liên kết nào.
# 4. Câu hỏi phải có độ khó vừa phải.
# 5. Câu hỏi phải hợp lý, phải được con người hiểu và trả lời.
# 6. Không sử dụng các cụm từ 'cung cấp ngữ cảnh', v.v. trong câu hỏi.

# Ngữ cảnh: {topic}
# """)

# tweet_chain = LLMChain(llm=llm, prompt=prompt_check_context_relevance, verbose=True)

# if __name__=="__main__":
#     topic = """
# 1. tóm tắt yêu cầu chương trình đào tạo ngành khoa học máy tính\nTổng số tín chỉ của chương trình đào tạo (Chưa tính các học phần Giáo dục thể chất, Giáo dục Quốc phòng - An ninh, Kỹ năng bổ trợ): 136 tín chỉ\n-   Khối kiến thức chung (Chưa tính các học phần Giáo dục thể chất, Giáo dục Quốc phòng\n- An ninh, Kỹ năng bổ trợ): 26 tín chỉ\n-   Khối kiến thức chung theo lĩnh vực 19 tín chỉ\n-   Khối kiến thức chung cho khối ngành 10 tín chỉ\n-   Khối kiến thức chung cho nhóm ngành 30 tín chỉ\n-   Khối kiến thức ngành 51 tín chỉ\n-   Khối kiến thức bắt buộc: 18 tín chỉ\n-   Khối kiến thức tự chọn: 21 tín chỉ\n-   Khối kiến thức bổ trợ: 05 tín chỉ\n-   Khối kiến thức thực tập và tốt nghiệp: 07 tín chỉ\n 2. khung chương trình đào tạo ngành khoa học máy tính\n
# """
#     resp = tweet_chain.run(topic=topic)
#     print(resp)

async def async_generate_answer(prompt: str):

    # prompt_check_context_relevance = PromptTemplate.from_template(prompt)
    # tweet_chain = LLMChain(llm=llm, prompt=prompt_check_context_relevance, verbose=False)
    # resp = tweet_chain.run(topic=docs)
    # return resp
    genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
    model = genai.GenerativeModel(model_name = "gemini-pro")
    response = model.generate_content(prompt)
        # tweet_chain = LLMChain(llm=self.llm, prompt=prompt, verbose=True)
        # resp = tweet_chain.run(topic=prompt)
    answer = response.text
    return answer

async def check_context_docs_rel(data, question):
    fmt_prompts = []
    for docs in data:

        prompt = f"""
Với câu hỏi và ngữ cảnh sau đây, hãy trả về *CÓ* nếu bất kỳ phần nào của ngữ cảnh có liên quan để trả lời câu hỏi. 
Nếu không có ngữ cảnh nào phù hợp, hãy trả về  *KHÔNG*. 
> Câu hỏi: {question}
> Bối cảnh:
>>>
{docs['passage']}
>>>
Câu trả lời:
"""
        fmt_prompts.append(prompt)

    tasks = [async_generate_answer(p) for p in fmt_prompts]
    node_responses = await asyncio.gather(*tasks)
    # prompt_check_context_relevance = PromptTemplate.from_template(prompt)
    # tweet_chain = LLMChain(llm=llm, prompt=prompt_check_context_relevance, verbose=False)
    # resp = tweet_chain.run(topic=docs)
    new_texts = [str(r) for r in node_responses]
    return new_texts


def check_context_docs(data, question):
    # Các dòng mã khác ở đây
    
    new_texts = asyncio.run(check_context_docs_rel(data, question))
    return new_texts
# docs = """
# Danh mục tài liệu tham khảo học phần Nhập môn lập trình - Introduction to Programming là:\nTài liệu bắt buộc\nLựa chọn 1. Lập trình căn bản với C\n1. Bài giảng của giáo viên\n2. Brian W. Kernighan and Dennis M. Ritchie, The C programming language, Prentice Hall 1988.\nLựa chọn 2. Lập trình căn bản với C++\n1. Bài giảng của giáo viên\n2. Hồ Sĩ Đàm (chủ biên), Trần Thị Minh Châu, Lê Sỹ Vinh, Giáo trình: Lập trình căn bản C++, NXB ĐHQGHN 2011\nLựa chọn 3. Lập trình căn bản với Java\nTài liệu tham khảo thêm\n1. Robert Sedgewick (Author), Kevin Wayne, Introduction to Programming in Java: An Interdisciplinary Approach, 2nd Edition. Addison-Wesley Professional 2017\nLựa chọn 1. Lập trình căn bản với C\n1. K. N. King, C Programming: A Modern Approach, 2nd Edition, W. W. Norton & Company 2008\n2. Paul J. Deitel, Harvey Deitel, C How to Program, 8th Edition, Pearson 2015\n3. J. Glenn Brookshear, Computer Science: An Overview, Addision Wesley 2009\nLựa chọn 2. Lập trình căn bản với C++\n1. Andrew Koenig, Accelerated C++: Practical Programming by Example, Addison-Wesley Professional 2000\n2. Stanley B. Lippman, C++ Primer, 5th Edition, Addison-Wesley Professional 2012\n3. J. Glenn Brookshear, Computer Science: An Overview, Addision Wesley 2009\nLựa chọn 3. Lập trình căn bản với Java\n1. Kathy Sierra, Bert Bates, Head First Java: A Brain-Friendly, O'Reilly 2005\n2. Allen B. Downey, Chris Mayfield, Think Java: How to Think Like a Computer Scientist, O'Reilly 2006\n3. J. Glenn Brookshear, Computer Science: An Overview, Addision Wesley 2009\n
# """
# question = 'các tài liệu tham khảo môn nhập môn lập trình'

# print(check_context_docs(docs, question))