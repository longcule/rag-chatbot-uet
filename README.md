# RAG (Retrieval-augmented generation) ChatBot for UET
## Made By Longcule
# Check List
- [x]  Collect data 
- [x]  Convert docx2md 
- [x] Clean data(clean table, rewrite.md format) 
- [x] Build Chatbot RAG MVP(Minimum Viable Product)
- [x] Build Chatbot with History Conventions 
- [ ] Improve RAG
- [ ] Process Input RAG(Refine the input question) 
- [ ] Process Pipeline RAG to Retrieval best relevance context 
- [ ] Edit UI Application Chatbot 
- [ ] Save Conventions to Database 
- [ ] Deploy to Server 

## Prerequisites

* Python 3.10+
* GPU supporting CUDA 12 and up.
* Poetry 1.7.0

### Install Poetry

Install Poetry with the official installer by following this [link](https://python-poetry.org/docs/#installing-with-the-official-installer).

You must use the current adopted version of Poetry defined [here](https://github.com/umbertogriffo/rag-chatbot/blob/main/version/poetry).

If you have poetry already installed and is not the right version, you can downgrade (or upgrade) poetry through:
```
poetry self update <version>
```

## Bootstrap Environment

To easily install the dependencies we created a make file.

### How to use the make file

> [!IMPORTANT]
> Run `Setup` as your init command (or after `Clean`).

* Check: ```make check```
  * Use it to check that `which pip3` and `which python3` points to the right path.
* Setup: ```make setup```
  * Creates an environment and installs all dependencies.
* Update: ```make update```
  * Update an environment and installs all updated dependencies.
* Tidy up the code: ```make tidy```
  * Run Ruff check and format.
* Clean: ```make clean```
  * Removes the environment and all cached files.
* Test: ```make test```
  * Runs all tests.
  * Using [pytest](https://pypi.org/project/pytest/)

## Run the RAG Chatbot

To interact with a GUI type:
```shell
streamlit run chatbot/rag_chatbot_app.py -- --model mistral --k 4 --synthesis-strategy async_tree_summarization
```