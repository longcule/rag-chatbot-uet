from abc import ABC
from typing import Any

from langchain.embeddings import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings
import getpass
import os, time

os.environ["OPENAI_API_KEY"] = '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'
class Embedder(ABC):
    embedder: Any

    def get_embedding(self):
        return self.embedder


class EmbedderHuggingFace(Embedder):
    # def __init__(self, model_name: str = "keepitreal/vietnamese-sbert"):
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
    # def __init__(self, model_name: str = "text-embedding-3-small"):
        self.embedder = HuggingFaceEmbeddings(model_name=model_name)
        # self.embedder = OpenAIEmbeddings(model=model_name, show_progress_bar=True)

        