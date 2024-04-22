import argparse
import sys,os
from pathlib import Path
from typing import List
# from PyPDF2 import PdfReader
from bot.memory.embedder import EmbedderHuggingFace
from bot.memory.vector_memory import VectorMemory
from helpers.log import get_logger
from langchain.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader
from langchain.text_splitter import MarkdownTextSplitter
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from sentence_transformers import SentenceTransformer
from pyvi.ViTokenizer import tokenize
import numpy as np
import pickle
import json
logger = get_logger(__name__)

import re

def clean_page_content(page_content):
    # Loại bỏ các ký tự không mong muốn
    cleaned_content = re.sub(r"[',\n|+=-]+", " ", page_content)

    return cleaned_content

# def get_pdf_text(pdf_docs):
#     text = ""
#     for pdf in pdf_docs:
#         pdf_reader = PdfReader(pdf)
#         for page in pdf_reader.pages:
#             text += page.extract_text()
#     return text


def load_documents(docs_path: str) -> List:
    """
    Loads Markdown documents from the specified path.

    Args:
        docs_path (str): The path to the documents.

    Returns:
        List: A list of loaded documents.

    Raises:
        None

    Example:
        >>> load_documents('/path/to/documents')
        [document1, document2, document3]
    """


    # loader = PyPDFLoader("/home/longcule/Videos/rag-chatbot/cshttt.pdf")
    # pages = loader.load_and_split()
    # text_loader_kwargs={'autodetect_encoding': True}
    # loader = DirectoryLoader(
    #     docs_path, 
    #     glob="./*.txt", 
    #     loader_cls=TextLoader, 
    #     loader_kwargs=text_loader_kwargs,
    #     show_progress=True,
    #     )
    # loader = TextLoader("/home/longcule/Videos/rag-chatbot/docstxt/2023.12.01_CTDT_nganh_HTTT_1.txt")
    loader = DirectoryLoader(
        docs_path,
        glob="**/*.md",
        loader_cls=UnstructuredMarkdownLoader,
        # loader_kwargs={"mode": "elements"},
        show_progress=True,
    )
    # file_paths = []  # Danh sách đường dẫn tới các tệp tin trong thư mục
    # sources = []
    # # Lặp qua tất cả các tệp tin trong thư mục
    # for filename in os.listdir(docs_path):
    #     file_path = os.path.join(docs_path, filename)

    # # Kiểm tra nếu tệp tin là một tệp tin văn bản
    # if os.path.isfile(file_path) and filename.endswith(".txt"):
    #     file_paths.append(file_path)
    #     loaders = TextLoader(file_path)
    #     sourse = loaders.load()
    #     sources.append(sourse)
    # return sources
    return loader.load()

def save_chunks_to_txt_file(chunks, output_file_path):
    with open(output_file_path, "w") as file:
        for i, chunk in enumerate(chunks, start=1):
            file.write(f"Chunk {i}:\n")
            file.write(str(chunk))
            file.write("\n\n")

# def split_chunks(sources: List, chunk_size: int = 512, chunk_overlap: int = 10) -> List:
#     """
#     Splits a list of sources into smaller chunks.

#     Args:
#         sources (List): The list of sources to be split into chunks.
#         chunk_size (int, optional): The maximum size of each chunk. Defaults to 512.
#         chunk_overlap (int, optional): The amount of overlap between consecutive chunks. Defaults to 0.

#     Returns:
#         List: A list of smaller chunks obtained from the input sources.
#     """
#     # for doc in sources:
#     #     print(doc.page_content)
#     #     data = clean_page_content(doc.page_content)
#     #     doc.page_content = data
#         # data = doc[0].metadata.get("source")
#         # doc[0].page_content = data
#     # print(sources)
#     # print(type(sources))
#     # text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,
#     #                                                  chunk_overlap=400)

#     # texts_sotay = text_splitter.split_documents(sources)
#     chunks = []
#     # print(type(sources))
#     output_file_path = '/home/longcule/Videos/rag-chatbot/chunkk234.txt'
#     splitter = MarkdownTextSplitter(chunk_size=chunk_size, chunk_overlap=400)
#     # data = text_splitter.split_documents(sources)
#     # print(data)
#     for chunk in splitter.split_documents(sources):
#         # print("chunk: ", type(chunk), chunk, "\n")
#         chunks.append(chunk)
#     save_chunks_to_txt_file(chunks, output_file_path)
#     return chunks

def get_courses(data_dir: str, chunk_size: int, chunk_overlap: int):
    """Transform a corpus of documents into a corpus of passages.
    
    Args:
        data_dir (str): directory that contains .txt files, each file contains text content of a wikipedia page.
    Returns:
        str: A corpus of chunks splitted from multiple initial documents. Each chunk will contain information about (id, title, passage)
    """
    corpus = []
    meta_corpus = []
    data_dir = f"{data_dir}/"
    filenames = os.listdir(data_dir)
    filenames = sorted(filenames)
    
    _id = 0
    docs = {}
    for filename in filenames:
        filepath = data_dir + filename
        title = filename.strip(".txt")
        with open(filepath, "r", encoding='utf-8') as f:
            text = f.read()
            docs[title] = text
            text = text.lstrip(title).strip()

            chunks = split_chunks(text, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
            chunks = [f"Title: {title}\n\n{chunk}" for chunk in chunks]
            meta_chunks = [{
                "title": title,
                "passage": chunks[i],
                "id": _id + i,
                "len": len(chunks[i].split())
            } for i in range(len(chunks))]
            _id += len(chunks)
            corpus.extend(chunks)
            meta_corpus.extend(meta_chunks)
    return meta_corpus

def split_chunks(text, chunk_size: int = 512, chunk_overlap: int = 10):
    """Split a long text into multiple chunks (passages) with managable sizes.
    
    Args:
        chunk_size (int): Maximum size of a chunk.
        chunk_overlap (int): Decide how many words are overlapped between two consecutive chunks. Basically #overlapped_words = chunk_size - chunk_overlap.
    Returns:
        str: Multiple chunks of text splitted from initial document text.
    """
    words = text.split()
    num_words = len(words)
    chunks = []
    start_idx = 0

    while True:
        end_idx = start_idx + chunk_size
        chunk = " ".join(words[start_idx:end_idx])
        chunks.append(chunk)
        if end_idx >= num_words:
            break
        start_idx += chunk_overlap

    return chunks


def build_memory_index(docs_path: str, vector_store_path: str, chunk_size: int, chunk_overlap: int):
    # sources = load_documents(str(docs_path))
    sources = get_courses(docs_path, chunk_size, chunk_overlap)
    logger.info(f"Number of chunks: {len(sources)}")
    # chunks = split_chunks(sources, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    # print("chunnn: ",chunks)
    # Import module
    with open(f"{vector_store_path}/courses_chunks.jsonl", "w") as outfile:
        for chunk in sources:
            d = json.dumps(chunk, ensure_ascii=False) + "\n"
            outfile.write(d)

    model = SentenceTransformer('bkai-foundation-models/vietnamese-bi-encoder').cuda()
    segmented_courses = [tokenize(example["passage"]) for example in sources]
    embeddings = model.encode(segmented_courses)
    embeddings /= np.linalg.norm(embeddings, axis=1)[:, np.newaxis]

    # logger.info(f"Number of Chunks: {len(chunks)}")
    # embedding = EmbedderHuggingFace().get_embedding()
    # VectorMemory.create_memory_index(embedding, chunks, vector_store_path)
    with open(f"{vector_store_path}/courses_embedding.pkl", 'wb') as f:
        pickle.dump(embeddings, f)
    logger.info("Memory Index has been created successfully!")


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Memory Builder")
    parser.add_argument(
        "--chunk-size",
        type=int,
        help="The maximum size of each chunk. Defaults to 512.",
        required=False,
        default=512,
    )
    parser.add_argument(
        "--chunk-overlap",
        type=int,
        help="The amount of overlap between consecutive chunks. Defaults to 0.",
        required=False,
        default=0,
    )

    return parser.parse_args()


def main(parameters):
    root_folder = Path(__file__).resolve().parent.parent
    doc_path = root_folder / "docstxt"
    vector_store_path = root_folder / "vector_store" / "docs_index"
    if not vector_store_path.exists():
        # Tạo thư mục nếu chưa tồn tại
        os.makedirs(vector_store_path)
    build_memory_index(
        str(doc_path),
        str(vector_store_path),
        parameters.chunk_size,
        parameters.chunk_overlap,
    )


if __name__ == "__main__":
    try:
        args = get_args()
        main(args)
    except Exception as error:
        logger.error(f"An error occurred: {str(error)}", exc_info=True, stack_info=True)
        sys.exit(1)
