import json
import matplotlib.pyplot as plt
# Đọc file JSON
with open('/home/longcule/Videos/rag-chatbot/json_file/retrieve_topk/retrieve_docs_1.json', encoding='utf-8') as file:
    data = json.load(file)

# Tính tỷ lệ trúng top k
def calculate_topk_accuracy(k):
    count = 0
    for item in data:
        topk_files = item['file_path_retrieve'][:k]
        # print(topk_files)
        if item['file_path_target'] in topk_files:
            count = count + 1
    
    accuracy = (count / len(data)) * 100
    return accuracy



# Tính và in ra tỷ lệ trúng top k cho k = 1, 3, 5, 10
topk_values = [1, 3, 4, 5, 10]
# for k in topk_values:
#     accuracy = calculate_topk_accuracy(k)
#     print(f'Tỷ lệ trúng top {k}: {accuracy}%')
accuracies = [calculate_topk_accuracy(k) for k in topk_values]

# Vẽ biểu đồ
plt.plot(topk_values, accuracies, marker='o')
plt.xlabel('Top k')
plt.ylabel('Tỷ lệ trúng (%)')
plt.title('Biểu đồ tỷ lệ trúng top k')
plt.xticks(topk_values)
plt.grid(True)

# Chỉnh cột y từ 0 đến 100%
plt.ylim(0, 100)

# Hiển thị giá trị phần trăm trên biểu đồ
for i, accuracy in enumerate(accuracies):
    rounded_accuracy = round(accuracy, 2)
    plt.annotate(f'{rounded_accuracy}%', (topk_values[i], accuracy), textcoords="offset points", xytext=(0,10), ha='center')

# Lưu biểu đồ thành file PNG
plt.savefig('accuracy_plot_2.png')