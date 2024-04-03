import argparse
import sys
from pathlib import Path
from typing import List
import re
from langchain.document_loaders import DirectoryLoader, UnstructuredMarkdownLoader



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
    loader = DirectoryLoader(
        docs_path,
        glob="**/*.md",
        loader_cls=UnstructuredMarkdownLoader,
        # loader_kwargs={"mode": "elements"},
        show_progress=True,
    )
    return loader.load()


# def split_chunks(sources: List, chunk_size: int = 512, chunk_overlap: int = 0) -> List:
#     """
#     Splits a list of sources into smaller chunks.

#     Args:
#         sources (List): The list of sources to be split into chunks.
#         chunk_size (int, optional): The maximum size of each chunk. Defaults to 512.
#         chunk_overlap (int, optional): The amount of overlap between consecutive chunks. Defaults to 0.

#     Returns:
#         List: A list of smaller chunks obtained from the input sources.
#     """
#     chunks = []
#     splitter = MarkdownTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
#     for chunk in splitter.split_documents(sources):
#         chunks.append(chunk)
#     return chunks


def split_chunks(sources):
    """
    Splits a list of sources into smaller chunks.

    Args:
        sources (List): The list of sources to be split into chunks.
        chunk_size (int, optional): The maximum size of each chunk. Defaults to 512.
        chunk_overlap (int, optional): The amount of overlap between consecutive chunks. Defaults to 0.

    Returns:
        List: A list of smaller chunks obtained from the input sources.
    """
    chunks = []
    current_chunk = []
    for source in sources:
        print(type(source))
        if re.match(r"^[1-9]\. ", source) or re.match(r"^10\. ", source):  # Kiểm tra nếu header bắt đầu từ 1. đến 10.
            if current_chunk:
                chunks.append(current_chunk)
                current_chunk = []
        current_chunk.append(source)
    if current_chunk:
        chunks.append(current_chunk)
    return chunks

docs_path = '/home/longcule/Videos/rag-chatbot/docs2'

sources = load_documents(str(docs_path))

print(split_chunks(sources))