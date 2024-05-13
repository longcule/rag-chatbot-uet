from sentence_transformers import SentenceTransformer
import numpy as np
from pyvi.ViTokenizer import tokenize
import string, json

def split_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.lower().split()
    words = [word for word in words if len(word.strip()) > 0]
    return words

def caculate_semantic_sc():
    file_path = '/home/longcule/Videos/rag-chatbot/output_rag_250_clean.json'
    embedder = SentenceTransformer('bkai-foundation-models/vietnamese-bi-encoder')
    print("halo")
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    # print(data)
    ans_1 = []
    semantic = []
    for item in data:
        tokenized_ans_rag = split_text(item['answer_rag'])
        tokenized_ans_gpt4 = split_text(item['answer_gpt4'])
        # print(tokenize)
        segmented_question_rag = tokenize(str(tokenized_ans_rag))
        segmented_question_gpt4 = tokenize(str(tokenized_ans_gpt4))
        question_emb_rag = embedder.encode([segmented_question_rag])
        question_emb_gpt4 = embedder.encode([segmented_question_gpt4])
        question_emb_rag /= np.linalg.norm(question_emb_rag, axis=1)[:, np.newaxis]
        question_emb_gpt4 /= np.linalg.norm(question_emb_gpt4, axis=1)[:, np.newaxis]
        semantic_scores = question_emb_rag @ question_emb_gpt4.T
        # semantic_scores = semantic_scores
        # print(semantic_scores[0][0])
        # print(semantic_scores)
        ans_1.append({"question": item['question'], "answer_rag": item['answer_rag'], "answer_gpt4": item['answer_gpt4'], "contexts": item['contexts'], "semantic_scores": semantic_scores[0][0].astype(float)})
        semantic.append(semantic_scores[0][0])
        # print(ans_1)
        # Lưu kết quả vào file mới
        with open('/home/longcule/Videos/rag-chatbot/evaluation/file/semantic_score.json', 'w', encoding='utf-8') as file:
            json.dump(ans_1, file, ensure_ascii=False)
    return semantic

score = caculate_semantic_sc()
sum = 0
for item in score:
    sum = sum + item

print(sum/(len(score)))

import json
import matplotlib.pyplot as plt

# Đường dẫn đến file JSON
file_path = "/home/longcule/Videos/rag-chatbot/evaluation/file/semantic_score.json"

# Đọc dữ liệu từ file JSON
with open(file_path, "r", encoding='utf-8') as file:
    data = json.load(file)

# Lấy danh sách các semantic_score
semantic_scores = [item["semantic_scores"] for item in data]

# Tạo danh sách các số thứ tự từ 1 đến n
indices = list(range(1, len(semantic_scores) + 1))

# Vẽ biểu đồ đường
plt.plot(indices, semantic_scores)
plt.xlabel("Số thứ tự")
plt.ylabel("Semantic Score")
plt.title("Biểu đồ đường của Semantic Score")
plt.ylim(0, 1)  # Đặt giới hạn trục y từ 0 đến 1
plt.show()
plt.savefig("/home/longcule/Videos/rag-chatbot/evaluation/img/semantic_scores.png")
