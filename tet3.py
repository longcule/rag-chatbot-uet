import json
file_path = '/home/longcule/Videos/rag-chatbot/json_file/testset_final.json'
qa_pairs = []
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)
for item in data:
    question = item['question']
    context = item['contexts']
    prompt = f"""
Hãy trích xuất các câu có liên quan từ bối cảnh được cung cấp có thể có khả năng giúp trả lời câu hỏi sau. 
Nếu không câu có liên quan được tìm thấy, hoặc nếu bạn tin rằng câu hỏi không thể được trả lời từ ngữ cảnh đã cho, trả về cụm từ "Thông tin chưa đầy đủ". 
Trong khi trích xuất các câu ứng cử viên, bạn không được phép thực hiện bất kỳ thay đổi nào đối với câu từ bối cảnh nhất định.
> Câu hỏi: {question}
> Bối cảnh:
>>>
{context}
>>>
Câu trả lời:
"""
    qa_pairs.append({"question": item['question'],"answer_gpt4":'', "context": item['contexts'], "prompt": prompt})
    with open("qa_dataset_prompt.json", "w", encoding='utf-8') as json_file:
                    json.dump(qa_pairs, json_file, ensure_ascii=False)