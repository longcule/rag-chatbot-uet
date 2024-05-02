
import json
import evaluate
bleu = evaluate.load('bleu')
# Đường dẫn đến file CSV
input_file = '/home/longcule/Videos/rag-chatbot/testset_final.json'

# Đường dẫn đến file .txt để lưu kết quả
txt_file = '/home/longcule/Videos/rag-chatbot/output_bleu.txt'

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

            # Tính toán kết quả
            result = bleu.compute(predictions=predictions, references=references, max_order=2)
            results.append(result)
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