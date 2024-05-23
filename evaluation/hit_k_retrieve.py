import json
import matplotlib.pyplot as plt
# Đọc file JSON
# with open('/home/longcule/Videos/rag-chatbot/json_file/retrieve_topk/retrieve_docs_semantic.json', encoding='utf-8') as file:
#     data = json.load(file)

# Tính tỷ lệ trúng top k
def calculate_topk_accuracy(k, type):
    with open(f'/home/longcule/Videos/rag-chatbot/json_file/retrieve_topk/retrieve_docs_{type}.json', encoding='utf-8') as file:
        data = json.load(file)

    count = 0
    for item in data:
        topk_files = item[f'file_path_{type}_retrieve'][:k]
        # print(topk_files)
        if item['file_path_target'] in topk_files:
            count = count + 1
    
    accuracy = (count / len(data)) * 100
    return accuracy


# Giả sử bạn đã tính toán được accuracies từ ba file khác nhau
topk_values = [1, 3, 4, 5, 10]
type1='hybrid'
type2='bm25'
type3='semantic'
accuracies_file1 = [calculate_topk_accuracy(k, type1) for k in topk_values]
accuracies_file2 = [calculate_topk_accuracy(k, type2) for k in topk_values]
accuracies_file3 = [calculate_topk_accuracy(k, type3) for k in topk_values]

# Vẽ biểu đồ cho từng file
plt.plot(topk_values, accuracies_file1, marker='o', color='blue', label='Hybrid Search')
plt.plot(topk_values, accuracies_file2, marker='o', color='red', label='Keyword Search')
plt.plot(topk_values, accuracies_file3, marker='o', color='green', label='Semantic Search')

# Cài đặt các nhãn và tiêu đề
plt.xlabel('Top k Chunks')
plt.ylabel('Hit-Rate (%)')
plt.title('The ratio chart hits the top k')
plt.xticks(topk_values)
plt.grid(True)
plt.ylim(0, 100)

# Hiển thị chú thích
plt.legend()

# Hiển thị giá trị phần trăm trên biểu đồ
for i, (acc1, acc2, acc3) in enumerate(zip(accuracies_file1, accuracies_file2, accuracies_file3)):
    plt.annotate(f'{round(acc1, 2)}%', (topk_values[i], acc1), textcoords="offset points", xytext=(0,10), ha='center')
    plt.annotate(f'{round(acc2, 2)}%', (topk_values[i], acc2), textcoords="offset points", xytext=(0,-15), ha='center')
    plt.annotate(f'{round(acc3, 2)}%', (topk_values[i], acc3), textcoords="offset points", xytext=(0,25), ha='center')

# Lưu biểu đồ thành file PNG
plt.savefig('/home/longcule/Videos/rag-chatbot/evaluation/img/accuracy_plot_comparison.png')


# Tính và in ra tỷ lệ trúng top k cho k = 1, 3, 5, 10
# topk_values = [1, 3, 4, 5, 10]
# # for k in topk_values:
# #     accuracy = calculate_topk_accuracy(k)
# #     print(f'Tỷ lệ trúng top {k}: {accuracy}%')
# accuracies = [calculate_topk_accuracy(k) for k in topk_values]

# # Vẽ biểu đồ
# plt.plot(topk_values, accuracies, marker='o')
# plt.xlabel('Top k')
# plt.ylabel('Tỷ lệ trúng (%)')
# plt.title('Biểu đồ tỷ lệ trúng top k')
# plt.xticks(topk_values)
# plt.grid(True)

# # Chỉnh cột y từ 0 đến 100%
# plt.ylim(0, 100)

# # Hiển thị giá trị phần trăm trên biểu đồ
# for i, accuracy in enumerate(accuracies):
#     rounded_accuracy = round(accuracy, 2)
#     plt.annotate(f'{rounded_accuracy}%', (topk_values[i], accuracy), textcoords="offset points", xytext=(0,10), ha='center')

# # Lưu biểu đồ thành file PNG
# plt.savefig('/home/longcule/Videos/rag-chatbot/evaluation/img/accuracy_plot_semantic.png')