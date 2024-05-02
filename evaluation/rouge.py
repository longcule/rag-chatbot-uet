from rouge_score import rouge_scorer
import json
scorer = rouge_scorer.RougeScorer(['rouge1', 'rouge2', 'rougeL'], use_stemmer=True)
candidate_summary = ""
reference_summaries = []
scores = {key: [] for key in ['rouge1', 'rouge2', 'rougeL']}
txt_file = '/home/longcule/Videos/rag-chatbot/output_rouge.txt'
input_file = '/home/longcule/Videos/rag-chatbot/testset_final.json'
with open(input_file, "r", encoding='utf-8') as file:
    input_data = json.load(file)
k = 0
for items in input_data:
    # if items['year'] >= 2023:
        k += 1
        candidate_summary = ""
        reference_summaries = []
        candidate_summary = items["ground_truth"]
        reference_summaries.append(items["answer"])
        for ref in reference_summaries:
            temp_scores = scorer.score(ref, candidate_summary)
            for key in temp_scores:
                scores[key].append(temp_scores[key])

with open(txt_file, 'w', encoding='utf-8') as f:
            for key in scores:
                f.write(str(scores[key]) + '\n')
avg_1 = 0
avg_2 = 0
for key in scores:
    if key == 'rouge1':
        for i in range(len(scores[key])):
            avg_1 += scores[key][i][2]
            # print(f'{key}:\n{scores[key][i][2]}')
    if key == 'rouge2':
        for i in range(len(scores[key])):
            avg_2 += scores[key][i][2]
            # print(f'{key}:\n{scores[key][i][2]}')


print(k)
print(avg_1/k, avg_2/k)