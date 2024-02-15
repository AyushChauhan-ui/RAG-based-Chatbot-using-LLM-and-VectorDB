# RAG-based-Chatbot-using-LLM-and-VectorDB


## Description

This project implements a RAG-based chatbot for information retrieval using large language models(LLM), langchain and vectorDB set-up on a local environment using ollama. Chainlit is utilizerd for chatbot interaction. It consists of two main scripts: `load.py` for loading and storing documents in a Vector Database (vdb) and `app.py` for starting the chatbot that leverages the stored information for answering queries.

## Installation

1. Go to the directory in which you want to work you want to work and Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   
   ```
   
2. Install the required dependencies:

   ```bash
   pip install langchain langchain_community chainlit 
   ```

3. Download Ollama for Linux using command:
    ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```
    Start ollama for interaction using command:
   ```bash
   ollama serve
   ```
   
4. Paralelly download the model to be used (in this case mistral) using command:
   ```bash
   ollama run mistral
   ```

5. Run the `load.py` script to load documents and create a Vector Database (vdb):

   ```bash
   python load.py
   ```
   
6. Run the `app.py` script to start the chatbot:

   ```bash
   chainlit run app.py
   ```

## Usage

- Upon running `app.py`, a link to chainlit app is created. After opening the link, the chatbot will start and prompt you with a welcome message. You can interact with it by sending queries.

## Project Structure

- **load.py**: Loads documents from a PDF file, splits them into chunks, and stores them in a Vector Database using the Chroma vector store and GPT-4 based embeddings.

- **app.py**: Implements the chatbot using Langchain library and chainlit. It sets up a RetrievalQA model for answering queries based on the stored information.


## Acknowledgments

- This project uses Langchain and Chainlit libraries for natural language processing and chatbot development.

