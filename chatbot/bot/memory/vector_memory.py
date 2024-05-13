from typing import Any, Dict, List, Tuple
import asyncio
from cleantext import clean
from helpers.log import get_logger
from langchain.vectorstores import Chroma, Qdrant
from langchain_core.documents import Document
from qdrant_client import QdrantClient
from langchain_core.vectorstores import VectorStoreRetriever
import torch
from pathlib import Path
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from optimum.bettertransformer import BetterTransformer
from datasets import load_dataset
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
import pandas as pd
import pickle
from pyvi.ViTokenizer import tokenize
import numpy as np
import string, time
from bot.memory.check_relevance_docs import check_context_docs

logger = get_logger(__name__)
QDRANT_URL='https://c0ce2559-a99b-436f-ac8c-591a14348a0d.us-east4-0.gcp.cloud.qdrant.io'
QDRANT_API_KEY='8N_5UtXLjm-oqxE7QpS-VjyuWrb9yND5SGRSKZblOFM-2y3zxnq0Gw'
def read_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = file.read()
    return data

def split_text(text):
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.lower().split()
    words = [word for word in words if len(word.strip()) > 0]
    return words

def retrieve(question, embedder, bm25, courses_embs, meta_courses, topk=50):
    start_time = time.time()
    """
    Get most relevant chunks to the question using combination of BM25 and semantic scores.
    """
    ## initialize query for each retriever (BM25 and semantic)
    tokenized_query = split_text(question)
    # print(tokenize)
    segmented_question = tokenize(question)
    question_emb = embedder.encode([segmented_question])
    question_emb /= np.linalg.norm(question_emb, axis=1)[:, np.newaxis]

    ## get BM25 and semantic scores
    bm25_scores = bm25.get_scores(tokenized_query)
    semantic_scores = question_emb @ courses_embs.T
    semantic_scores = semantic_scores[0]
    # print("bm25_scores", bm25_scores, "\n" ,"semantic_scores", semantic_scores)
    ## update chunks' scores. 
    max_bm25_score = max(bm25_scores)
    min_bm25_score = min(bm25_scores)
    def normalize(x):
        return (x - min_bm25_score + 0.1) / \
        (max_bm25_score - min_bm25_score + 0.1)
        
    corpus_size = len(meta_courses)
    print("len_meta_courses: ", corpus_size)
    for i in range(corpus_size):
        meta_courses[i]["bm25_score"] = bm25_scores[i]
        meta_courses[i]["bm25_normed_score"] = normalize(bm25_scores[i])
        meta_courses[i]["semantic_score"] = semantic_scores[i]

    ## compute combined score (BM25 + semantic)
    for passage in meta_courses:
        passage["combined_score"] = passage["bm25_normed_score"] * 0.4 + \
                                    passage["semantic_score"] * 0.6

    ## sort passages by the combined score
    sorted_passages = sorted(meta_courses, key=lambda x: x["combined_score"], reverse=True)
    # print("top k: ",sorted_passages[:topk])
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Thời gian chạy của hàm retrieve:", elapsed_time, "giây")

    return sorted_passages[:topk]


def remove_duplicates(data_list):
    title_counts = {}
    unique_data_list = []
    processed_titles = set()

    for item in data_list:
        title = item.get("title")
        if title in title_counts:
            title_counts[title] += 1
        else:
            title_counts[title] = 1

    for item in data_list:
        title = item.get("title")
        if title_counts[title] > 1 and title not in processed_titles:
            unique_data_list.append(item)
            processed_titles.add(title)
        elif title_counts[title] == 1:
            unique_data_list.append(item)

    return unique_data_list

class VectorMemory:
    """
    Class for managing vector memory operations.

    Parameters:
    -----------
    embedding : Any
        The embedding object used for vectorization.

    verbose : bool, optional
        Whether to enable verbose mode (default is False).

    """

    def __init__(self, vector_store_path: str, embedding: Any, verbose=False) -> None:
        self.embedding = embedding
        self.verbose = verbose
        if self.embedding is None:
            logger.error("No embedder passed to VectorMemory")
            raise Exception("No embedder passed to VectorMemory")

        # self.index = self.load_memory_index(vector_store_path)
        self.meta_courses, self.bm25, self.courses_embs, self.embedder =  self.initialize_retriever(vector_store_path)



    def load_memory_index(self, vector_store_path: str) -> Chroma:
        """
        Loads the Chroma memory index from the given vector store path.

        Parameters:
        -----------
        vector_store_path : str
            The path to the vector store.

        Returns:
        -------
        Chroma
            The loaded Chroma memory index.

        """
        # client = QdrantClient(
        #     url=QDRANT_URL,api_key=QDRANT_API_KEY, prefer_grpc=False
        # )
        # index = Qdrant(
        #                 client=client,
        #                 embeddings=self.embedding,
        #                 collection_name='vector_store_rag_1'
        #                 )
        # index = Chroma(persist_directory=str(vector_store_path), embedding_function=self.embedding)
        # retriever = RerankRetriever(vectorstore = index.as_retriever(search_kwargs={"k":15}))
        # print(corpus_embs[0])
        embedder = SentenceTransformer('bkai-foundation-models/vietnamese-bi-encoder')
        return embedder
    def initialize_retriever(self, vector_store_path: str):
        # Load meta_courses from dataset
        meta_courses = load_dataset(
            "json",
            data_files=f"{vector_store_path}/courses_chunks.jsonl",
            split="train"
        ).to_list()

        # Tokenize courses
        tokenized_courses = [split_text(doc["passage"]) for doc in meta_courses]

        # Initialize BM25 retriever
        bm25 = BM25Okapi(tokenized_courses)

        # Load courses embeddings
        with open(f'{str(vector_store_path)}/courses_embedding.pkl', 'rb') as f:
            courses_embs = pickle.load(f)

        # Initialize SentenceTransformer embedder
        embedder = SentenceTransformer('bkai-foundation-models/vietnamese-bi-encoder')

        # Return the initialized retriever components
        return meta_courses, bm25, courses_embs, embedder

    def similarity_search_doc(
        self, query: str, k: int = 4, threshold: float = 0.01
    ) -> Tuple[List[Document], List[Dict[str, Any]]]:
        """
        Performs similarity search on the given query.

        Parameters:
        -----------
        query : str
            The query string.

        index : Chroma
            The Chroma index to perform the search on.

        k : int, optional
            The number of retrievals to consider (default is 4).

        threshold : float, optional
            The threshold for considering similarity scores (default is 0.2).


        Returns:
        -------
        Tuple[List[Document], List[Dict[str, Any]]]
            A tuple containing the list of matched documents and a list of their sources.

        """
        # root_folder = Path(__file__).resolve().parent.parent
        print("que riiii: ",query)
        # vector_store_path = 'vector_store/docs_index'
        # meta_courses = load_dataset(
        #     "json",
        #     data_files=f"{vector_store_path}/courses_chunks.jsonl",
        #     split="train"
        # ).to_list()
        # ## initiate BM25 retriever
        # tokenized_courses = [split_text(doc["passage"]) for doc in meta_courses]
        # bm25 = BM25Okapi(tokenized_courses)

        # with open(f'{str(vector_store_path)}/courses_embedding.pkl', 'rb') as f:
        #     courses_embs = pickle.load(f)

        # embedder = SentenceTransformer('bkai-foundation-models/vietnamese-bi-encoder')
        data = retrieve(query, self.embedder, self.bm25, self.courses_embs, self.meta_courses, topk=k)
        # print("data", data)
        # data = remove_duplicates(data)
        # print("data2: ", data)
        sources = []
        retrieved_contents = []
        # if data[0]['combined_score'] < 0.5:
        #     return retrieved_contents, sources
        for doc in data:
            file_path= f"/home/longcule/Videos/rag-chatbot/docstxt/{doc['title']}.txt"
            # print(file_path)
            print(file_path)
            data2 = read_md_file(file_path)
            print("ghi")
            doc['passage'] = data2
        
        # print("data3: ",data)
        # new_data = []  # Danh sách mới để chứa các tài liệu thỏa mãn điều kiện
        start_time = time.time()
        # tasks = [self.llm.async_generate_answer(p) for p in fmt_prompts]
        #     node_responses = await asyncio.gather(*tasks)
        for doc in data:
            retrieved_contents.append(doc['passage'])
        # list_check = check_context_docs(data, query)
        # print(list_check)
        # for idx, item in enumerate(data):
        #     # if item == 'CÓ':
        #         new_data.append(data[idx])
        #         retrieved_contents.append(data[idx]['passage'])
            # else:
            #     continue
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("Thời gian chạy check context relevance:", elapsed_time, "giây")
        
        for doc in data:
            sources.append(
                {
                    "score": round(doc['combined_score'], 3),
                    "document": doc['title'],
                    "content_preview": f"{doc['passage'][:100]}...",
                }
            )
        # print("source: ", sources)
        return retrieved_contents, sources

    @staticmethod
    def create_memory_index(embedding: Any, chunks: List, vector_store_path: str):
        # texts = [clean(doc.page_content, no_emoji=True) for doc in chunks]
        texts = [doc.page_content.replace("\n", " ") for doc in chunks]
        # print(texts)
        # print(texts)
        metadatas = [doc.metadata for doc in chunks]
        print("metadataaaaa: ", type(metadatas[0]))

        # memory_index = Qdrant.from_documents(
        #     chunks,
        #     embedding,
        #     url=QDRANT_URL,
        #     prefer_grpc=False,
        #     collection_name="vector_store_rag_1",
        #     api_key=QDRANT_API_KEY,
        #     timeout=100
        # )
        memory_index = Chroma.from_documents(
            chunks,
            embedding=embedding,
            persist_directory=vector_store_path,
        )
        memory_index.persist()
