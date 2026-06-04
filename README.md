# AI Chatbot using LangChain and Ollama

A context-aware AI chatbot powered by **LangChain**, **Ollama**, and **Mistral LLM**, running completely locally on your machine.

## Features

* Local LLM inference using Ollama
* Powered by Mistral LLM
* Conversation memory using LangChain ChatMessageHistory
* Context-aware responses based on previous interactions
* Interactive command-line chatbot interface
* Privacy-friendly (runs locally without external APIs)

## Tech Stack

* Python
* LangChain
* Ollama
* Mistral LLM
* ChatMessageHistory

## Installation

### 1. Install Ollama

Download and install Ollama from:

https://ollama.com

### 2. Pull the Mistral model

```bash
ollama pull mistral
```

### 3. Install dependencies

```bash
pip install langchain langchain-community langchain-core langchain-ollama
```

### 4. Run the chatbot

```bash
python chatbot.py
```

## Example

```text
You: My name is Prachi

AI: Nice to meet you, Prachi!

You: What is my name?

AI: Your name is Prachi.
```

The chatbot remembers previous messages within the session using LangChain's ChatMessageHistory.

## Future Improvements

* PDF Question Answering (RAG)
* Vector Database Integration
* Streamlit Web Interface
* Persistent Chat Memory using SQLite
* Multi-document Knowledge Assistant

## Author

Prachi Jha

* GitHub: https://github.com/prachijha05
* LinkedIn: https://www.linkedin.com/in/prachi-jha-b084b828b/
