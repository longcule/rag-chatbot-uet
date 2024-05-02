
import json
from evaluate import load
bertscore = load("bertscore")
# Đường dẫn đến file CSV
input_file = '/home/longcule/Videos/rag-chatbot/testset_final.json'

# Đường dẫn đến file .txt để lưu kết quả
txt_file = '/home/longcule/Videos/rag-chatbot/output_bert.txt'

# Lưu kết quả vào list
predictions = []
references = []
results = []
# Đọc dữ liệu từ file CSV với encoding là UTF-8
with open(input_file, "r", encoding='utf-8') as file:
    input_data = json.load(file)
    predictions = []
    references = []
    k = 0
    for row in input_data:
        # if row['year'] >= 2023:
            k += 1
            data_test_value = row['ground_truth']  # Giá trị cột "data_test"
            predictions.append(data_test_value)

            reference_values = row['answer']  # Các giá trị cột "references"
            references.append(reference_values)
            predictions = ["hello world", "general kenobi"]
            references = ["hello world", "general kenobi"]
            results = bertscore.compute(predictions=predictions, references=references, model_type="distilbert-base-uncased")
            # BERTScore calculation
            scorer = BERTScorer(model_type='bert-base-uncased')
            P, R, F1 = scorer.score([candidate], [reference])
            print(f"BERTScore Precision: {P.mean():.4f}, Recall: {R.mean():.4f}, F1: {F1.mean():.4f}")
            
            # Tính toán kết quả
            # result = bleu.compute(predictions=predictions, references=references, max_order=2)
            # results.append(result)
            # print(result['bleu'])
            # Lưu kết quả vào file .txt theo từng hàng
    
with open(txt_file, 'w', encoding='utf-8') as f:
            for res in results:
                f.write(str(res) + '\n')
summm = 0
for res in results:
    summm += float(res['bleu'])

print(summm/k)
print("Kết quả đã được lưu vào file .txt.")