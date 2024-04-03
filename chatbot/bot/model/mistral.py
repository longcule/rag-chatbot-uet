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
    qa_prompt_template = """<|im_start|>system
{system}<|im_end|>
<|im_start|>user
{question}<|im_end|>
<|im_start|>assistant
"""
    ctx_prompt_template = """<|im_start|>system
{system}<|im_end|>
<|im_start|>user
Thông tin bối cảnh dưới đây về các học phần hoặc chương trình đào tạo trong trường đại học Công Nghệ.
---------------------
{context}
---------------------
Dựa vào thông tin ngữ cảnh chứ không phải kiến ​​thức có sẵn, hãy trả lời câu hỏi dưới đây,:
{question}<|im_end|>
<|im_start|>assistant
"""
    refined_ctx_prompt_template = """<|im_start|>system
{system}<|im_end|>
<|im_start|>user
Truy vấn ban đầu như sau: {question}
Chúng tôi đã cung cấp câu trả lời hiện có: {existing_answer}
Chúng tôi có cơ hội để tinh chỉnh câu trả lời hiện có
(chỉ khi cần thiết) với một số ngữ cảnh khác bên dưới.
---------------------
{context}
---------------------
Với bối cảnh mới, hãy tinh chỉnh câu trả lời ban đầu để trả lời truy vấn tốt hơn.
Nếu ngữ cảnh không hữu ích, hãy trả lại câu trả lời ban đầu.
Refined Answer:<|im_end|>
<|im_start|>assistant
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
