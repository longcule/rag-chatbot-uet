from bot.client.llm_client import LlmClientType
from bot.model.model import Model


class MistralSettings(Model):
    url = "https://huggingface.co/TheBloke/Mistral-7B-OpenOrca-GGUF/resolve/main/mistral-7b-openorca.Q4_K_M.gguf"
    file_name = "mistral-7b-openorca.Q4_K_M.gguf"
    clients = [LlmClientType.LAMA_CPP]
    type = "mistral"
    """
    Config:
    - top_k="The top-k value to use for sampling."
    - top_p="The top-p value to use for sampling."
    - temperature="The temperature to use for sampling."
    - repetition_penalty="The repetition penalty to use for sampling."
    - last_n_tokens="The number of last tokens to use for repetition penalty."
    - seed="The seed value to use for sampling tokens."
    - max_new_tokens="The maximum number of new tokens to generate."
    - stop="A list of sequences to stop generation when encountered."
    - stream="Whether to stream the generated text."
    - reset="Whether to reset the model state before generating text."
    - batch_size="The batch size to use for evaluating tokens in a single prompt."
    - threads="The number of threads to use for evaluating tokens."
    - context_length="The maximum context length to use."
    - gpu_layers="The number of layers to run on GPU."
        - Set gpu_layers to the number of layers to offload to GPU.
        - Set to 0 if no GPU acceleration is available on your system.
    """

    config = {
        "top_k": 40,
        "top_p": 0.95,
        "temperature": 0.1,
        "repetition_penalty": 1.1,
        "last_n_tokens": 64,
        "seed": -1,
        "batch_size": 2,
        "threads": -1,
        "max_new_tokens": 2048,
        "stop": None,
        "stream": False,
        "reset": True,
        "context_length": 2048,
        "gpu_layers": 15,
        "mmap": True,
        "mlock": False,
    }
    system_template = "Bạn là một trợ lý hữu ích, tôn trọng và trung thực."
    qa_prompt_template = """
{system}
{question}
"""
    ctx_prompt_template = """
{system}
Thông tin bối cảnh dưới đây về các học phần hoặc chương trình đào tạo trong trường đại học Công Nghệ.
---------------------
{context}
---------------------
Dựa vào thông tin ngữ cảnh chứ không phải kiến ​​thức có sẵn, hãy tận dụng tất cả thông tin có được và trả lời câu hỏi dưới đây, hãy trả lời một cách lịch sự và lễ phép:
Câu hỏi như sau: {question}
"""

    ctx_prompt_template_tree = """
{system}
Câu hỏi ban đầu: "{question}"
Để hiểu rõ hơn về nhu cầu của người hỏi, chúng tôi đã thu thập các câu trả lời hiện có:
- Câu trả lời 1: "{existing_answer_1}"
- Câu trả lời 2: "{existing_answer_2}"
Dựa trên những thông tin đã được cung cấp:
1. Tổng hợp các thông tin từ hai câu trả lời đã cho để đề xuất một câu trả lời mới, toàn diện hơn, cung cấp thông tin đầy đủ và chính xác nhất có thể.
2. Những thông tin bạn lấy để đưa vào câu trả lời mới phải được lấy từ các câu trả lời trước đó, không được tạo thêm bất kì chi tiết nào mới.
3. Khi trả lời câu hỏi, không cần cố gắng giải thích những gì có các câu trả lời trước mà chỉ tập trung trả lời câu hỏi
"""

    refined_ctx_prompt_template = """
{system}
Câu hỏi ban đầu như sau: {question}
Chúng tôi đã cung cấp câu trả lời hiện có: {existing_answer}
Có thể tinh chỉnh câu trả lời hiện có (chỉ khi cần thiết) với một số ngữ cảnh khác bên dưới.
---------------------
{context}
---------------------
Với bối cảnh mới, hãy tinh chỉnh câu trả lời ban đầu để trả lời câu hỏi tốt hơn.
Nếu ngữ cảnh không hữu ích, hãy trả lại câu trả lời ban đầu, hãy trả lời một cách lịch sự và lễ phép.
"""
    refined_question_conversation_awareness_prompt_template = """<|im_start|>system
{system}<|im_end|>
<|im_start|>user
\nLịch sử chat:
---------------------
{chat_history}
---------------------
Follow Up Question: {question}
Với cuộc trò chuyện trên và một câu hỏi tiếp theo, hãy diễn đạt lại câu hỏi tiếp theo thành một câu hỏi độc lập.
Câu hỏi độc lập:<|im_end|>
<|im_start|>assistant
"""

    refined_answer_conversation_awareness_prompt_template = """<|im_start|>system
{system}<|im_end|>
<|im_start|>user
\nLịch sử chat:
---------------------
{chat_history}
---------------------
Xem xét bối cảnh được cung cấp trong Lịch sử trò chuyện, hãy trả lời câu hỏi bên dưới với nhận thức về cuộc trò chuyện:
{question}<|im_end|>
<|im_start|>assistant
"""
