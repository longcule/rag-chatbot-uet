from pathlib import Path
from typing import Any, Iterator, Union

from llama_cpp import CreateCompletionResponse, CreateCompletionStreamResponse, Llama

from bot.client.llm_client import LlmClient, LlmClientType
from bot.model.model import Model

import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import google.generativeai as genai

load_dotenv()



class LamaCppClient(LlmClient):
    def __init__(self, model_folder: Path, model_settings: Model):
        if LlmClientType.LAMA_CPP not in model_settings.clients:
            raise ValueError(
                f"{model_settings.file_name} is a not supported by the {LlmClientType.LAMA_CPP.value} client."
            )
        super().__init__(model_folder, model_settings)

    # def _load_llm(self) -> Any:`  `
    #     llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_API_KEY)
    #     return llm

    # def _load_tokenizer(self) -> Any:
    #     return None

    def generate_answer(self, prompt: str) -> str:
        """
        Generates an answer based on the given prompt using the language model.

        Args:
            prompt (str): The input prompt for generating the answer.
            max_new_tokens (int): The maximum number of new tokens to generate (default is 512).

        Returns:
            str: The generated answer.
        """
        # output = self.llm(prompt, max_tokens=max_new_tokens, echo=False, **self.model_settings.config_answer)
        print("hello, im here!!!")

        genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
        model = genai.GenerativeModel(model_name = "gemini-pro")
        response = model.generate_content(prompt)
        # tweet_chain = LLMChain(llm=self.llm, prompt=prompt, verbose=True)
        # resp = tweet_chain.run(topic=prompt)
        answer = response.text
        # print("ans llm: ", answer)

        return answer

    async def async_generate_answer(self, prompt: str) -> str:
        """
        Generates an answer based on the given prompt using the language model.

        Args:
            prompt (str): The input prompt for generating the answer.
            max_new_tokens (int): The maximum number of new tokens to generate (default is 512).

        Returns:
            str: The generated answer.
        """
        genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
        model = genai.GenerativeModel(model_name = "gemini-pro")
        response = model.generate_content(prompt)
        # tweet_chain = LLMChain(llm=self.llm, prompt=prompt, verbose=True)
        # resp = tweet_chain.run(topic=prompt)
        answer = response.text
        # print("ans llm: ", answer)

        return answer

    # def stream_answer(self, prompt: str, skip_prompt: bool = True, max_new_tokens: int = 512) -> str:
    #     """
    #     Generates an answer by streaming tokens using the TextStreamer.

    #     Args:
    #         prompt (str): The input prompt for generating the answer.
    #         skip_prompt (bool): Whether to skip the prompt tokens during streaming (default is True).
    #         max_new_tokens (int): The maximum number of new tokens to generate (default is 512).

    #     Returns:
    #         str: The generated answer.
    #     """
    #     answer = ""
    #     stream = self.start_answer_iterator_streamer(prompt, max_new_tokens=max_new_tokens)

    #     for output in stream:
    #         token = output["choices"][0]["text"]
    #         answer += token
    #         print(token, end="", flush=True)

    #     return answer

    # def start_answer_iterator_streamer(
    #     self, prompt: str, skip_prompt: bool = True, max_new_tokens: int = 512
    # ) -> Union[CreateCompletionResponse, Iterator[CreateCompletionStreamResponse]]:
    #     stream = self.llm.create_completion(
    #         prompt, max_tokens=max_new_tokens, stream=True, **self.model_settings.config_answer
    #     )
    #     return stream

    async def async_start_answer_iterator_streamer(
        self, prompt: str
    ) -> Union[CreateCompletionResponse, Iterator[CreateCompletionStreamResponse]]:
        # stream = self.llm.create_completion(
        #     prompt, max_tokens=max_new_tokens, stream=True, **self.model_settings.config_answer
        # )
        # return stream
        genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
        model = genai.GenerativeModel(model_name = "gemini-pro")
        response = model.generate_content(prompt)
        # tweet_chain = LLMChain(llm=self.llm, prompt=prompt, verbose=True)
        # resp = tweet_chain.run(topic=prompt)
        answer = response.text
        # print("ans llm: ", answer)

        return answer

    # def parse_token(self, token):
    #     return token["choices"][0]["text"]



# class LamaCppClient(LlmClient):
#     def __init__(self, model_folder: Path, model_settings: Model):
#         if LlmClientType.LAMA_CPP not in model_settings.clients:
#             raise ValueError(
#                 f"{model_settings.file_name} is a not supported by the {LlmClientType.LAMA_CPP.value} client."
#             )
#         super().__init__(model_folder, model_settings)

#     def _load_llm(self) -> Any:
#         llm = Llama(model_path=str(self.model_path), **self.model_settings.config)
#         return llm

#     def _load_tokenizer(self) -> Any:
#         return None

#     def generate_answer(self, prompt: str, max_new_tokens: int = 512) -> str:
#         """
#         Generates an answer based on the given prompt using the language model.

#         Args:
#             prompt (str): The input prompt for generating the answer.
#             max_new_tokens (int): The maximum number of new tokens to generate (default is 512).

#         Returns:
#             str: The generated answer.
#         """
#         output = self.llm(prompt, max_tokens=max_new_tokens, echo=False, **self.model_settings.config_answer)

#         answer = output["choices"][0]["text"]
#         print("ans llm: ", answer)

#         return answer

    # async def async_generate_answer(self, prompt: str, max_new_tokens: int = 512) -> str:
        """
        Generates an answer based on the given prompt using the language model.

        Args:
            prompt (str): The input prompt for generating the answer.
            max_new_tokens (int): The maximum number of new tokens to generate (default is 512).

        Returns:
            str: The generated answer.
        """
        # genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
        # model = genai.GenerativeModel(model_name = "gemini-pro")
        # response = model.generate_content(prompt)
        # # tweet_chain = LLMChain(llm=self.llm, prompt=prompt, verbose=True)
        # # resp = tweet_chain.run(topic=prompt)
        # answer = response.text
        # # print("ans llm: ", answer)

        # return answer
        # output = self.llm(prompt, max_tokens=max_new_tokens, echo=False, **self.model_settings.config_answer)

        # answer = output["choices"][0]["text"]

        # return answer

#     def stream_answer(self, prompt: str, skip_prompt: bool = True, max_new_tokens: int = 512) -> str:
#         """
#         Generates an answer by streaming tokens using the TextStreamer.

#         Args:
#             prompt (str): The input prompt for generating the answer.
#             skip_prompt (bool): Whether to skip the prompt tokens during streaming (default is True).
#             max_new_tokens (int): The maximum number of new tokens to generate (default is 512).

#         Returns:
#             str: The generated answer.
#         """
#         answer = ""
#         stream = self.start_answer_iterator_streamer(prompt, max_new_tokens=max_new_tokens)

#         for output in stream:
#             token = output["choices"][0]["text"]
#             answer += token
#             print(token, end="", flush=True)

#         return answer

#     def start_answer_iterator_streamer(
#         self, prompt: str, skip_prompt: bool = True, max_new_tokens: int = 512
#     ) -> Union[CreateCompletionResponse, Iterator[CreateCompletionStreamResponse]]:
#         stream = self.llm.create_completion(
#             prompt, max_tokens=max_new_tokens, stream=True, **self.model_settings.config_answer
#         )
#         return stream

    # async def async_start_answer_iterator_streamer(
    #     self, prompt: str, skip_prompt: bool = True, max_new_tokens: int = 512
    # ) -> Union[CreateCompletionResponse, Iterator[CreateCompletionStreamResponse]]:
    #     # stream = self.llm.create_completion(
    #     #     prompt, max_tokens=max_new_tokens, stream=True, **self.model_settings.config_answer
    #     # )
    #     # return stream
    #     genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))
    #     model = genai.GenerativeModel(model_name = "gemini-pro")
    #     response = model.generate_content(prompt)
    #     # tweet_chain = LLMChain(llm=self.llm, prompt=prompt, verbose=True)
    #     # resp = tweet_chain.run(topic=prompt)
    #     answer = response.text
    #     # print("ans llm: ", answer)

    #     return answer

#     def parse_token(self, token):
#         return token["choices"][0]["text"]
