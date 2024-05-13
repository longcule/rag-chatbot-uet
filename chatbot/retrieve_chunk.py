import argparse
import sys, json
import time
from pathlib import Path
from bot.client.client_settings import get_client, get_clients
from bot.client.llm_client import LlmClient
from bot.conversation.conversation_retrieval import ConversationRetrieval
from bot.conversation.ctx_strategy import (
    BaseSynthesisStrategy,
    get_ctx_synthesis_strategies,
    get_ctx_synthesis_strategy,
)
from bot.memory.embedder import EmbedderHuggingFace
from bot.memory.vector_memory import VectorMemory
from bot.model.model_settings import get_model_setting, get_models
from helpers.log import get_logger
from helpers.prettier import prettify_source

def load_llm_client(llm_client_name: str, model_folder: Path, model_name: str) -> LlmClient:
    model_settings = get_model_setting(model_name)
    clients = [client.value for client in model_settings.clients]
    if llm_client_name not in clients:
        llm_client_name = clients[0]
    llm = get_client(llm_client_name, model_folder=model_folder, model_settings=model_settings)

    return llm


def load_conversational_retrieval(_llm: LlmClient) -> ConversationRetrieval:
    conversation_retrieval = ConversationRetrieval(_llm)
    return conversation_retrieval


def load_ctx_synthesis_strategy(ctx_synthesis_strategy_name: str, _llm: LlmClient) -> BaseSynthesisStrategy:
    ctx_synthesis_strategy = get_ctx_synthesis_strategy(ctx_synthesis_strategy_name, llm=_llm)
    return ctx_synthesis_strategy


def load_index(vector_store_path: Path) -> VectorMemory:
    """
    Loads a Vector Memory index based on the specified vector store path.

    Args:
        vector_store_path (Path): The path to the vector store.

    Returns:
        VectorMemory: An instance of the VectorMemory class with the loaded index.
    """
    embedding = EmbedderHuggingFace().get_embedding()
    index = VectorMemory(vector_store_path=str(vector_store_path), embedding=embedding)

    return index



def retrieve_docs(parameters, user_input: str) -> None:
    """
    Main function to run the RAG Chatbot application.

    Args:
        parameters: Parameters for the application.
    """

    root_folder = Path(__file__).resolve().parent.parent
    model_folder = root_folder / "models"
    vector_store_path = root_folder / "vector_store" / "docs_index"
    Path(model_folder).parent.mkdir(parents=True, exist_ok=True)

    client_name = parameters.client
    model_name = parameters.model
    synthesis_strategy_name = parameters.synthesis_strategy

    llm = load_llm_client(client_name, model_folder, model_name)
    conversational_retrieval = load_conversational_retrieval(_llm=llm)
    ctx_synthesis_strategy = load_ctx_synthesis_strategy(synthesis_strategy_name, _llm=llm)
    index = load_index(vector_store_path)

    refined_user_input = conversational_retrieval.refine_question(user_input)
    print("retriveinput: ",refined_user_input)
    
    retrieved_contents, sources = index.similarity_search_doc(query=refined_user_input, k=10)
                # print("retrive: ", retrieved_contents)
        # Display assistant response in chat message container
    docs_path = []
    for source in sources:
        docs_path.append(source['document'])
    # start_time = time.time()
    # print(retrieved_contents)
    # print("halo1")
    # streamer, fmt_prompts = conversational_retrieval.context_aware_answer(
    #     ctx_synthesis_strategy, refined_user_input, retrieved_contents
    #             )

    # took = time.time() - start_time
    # print(took)
    # print(streamer)
    # print("halo")
    return docs_path

def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="RAG Chatbot")

    client_list = get_clients()
    default_client = client_list[0]

    model_list = get_models()
    default_model = model_list[0]

    synthesis_strategy_list = get_ctx_synthesis_strategies()
    default_synthesis_strategy = synthesis_strategy_list[0]

    parser.add_argument(
        "--client",
        type=str,
        choices=client_list,
        help=f"Client to be used. Defaults to {default_client}.",
        required=False,
        const=default_client,
        nargs="?",
        default=default_client,
    )

    parser.add_argument(
        "--model",
        type=str,
        choices=model_list,
        help=f"Model to be used. Defaults to {default_model}.",
        required=False,
        const=default_model,
        nargs="?",
        default=default_model,
    )

    parser.add_argument(
        "--synthesis-strategy",
        type=str,
        choices=synthesis_strategy_list,
        help=f"Model to be used. Defaults to {default_synthesis_strategy}.",
        required=False,
        const=default_synthesis_strategy,
        nargs="?",
        default=default_synthesis_strategy,
    )

    parser.add_argument(
        "--k",
        type=int,
        help="Number of chunks to return from the similarity search. Defaults to 2.",
        required=False,
        default=2,
    )

    return parser.parse_args()

# if __name__ == "__main__":
#     try:
#         args = get_args()
#         # user_input = 'Khoa học dịch vụ là gì?'
#         # gen_qa_dataset(args, user_input)
#         # Đọc file JSON
#         with open('/home/longcule/Videos/rag-chatbot/retrieve_testset_final.json', 'r', encoding='utf-8') as file:
#             data = json.load(file)

#         ans_1 = []
#         for item in data:
#             question = item['question']
            
#             # print("context: ", context, "question: ", question)
#             # Kiểm tra và lưu câu trả lời
#             resp = retrieve_docs(args, question)
#             # ans_1.append(resp)
#             ans_1.append({"question": question, "file_path_retrieve": resp, "file_path_target": item['file_path_target']})


#             # Lưu kết quả vào file mới
#             with open('retrieve_docs_1.json', 'w', encoding='utf-8') as file:
#                 json.dump(ans_1, file, ensure_ascii=False)

#     except Exception as error:
#         # logger.error(f"An error occurred: {str(error)}", exc_info=True, stack_info=True)
#         print(str(error))
#         sys.exit(1)

args = get_args()
question = 'Sinh viên cần làm gì trong môn tác tử thông minh và robot'
resp = retrieve_docs(args, question)
print(resp)