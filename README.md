# AI Assistants using LangChain and Ollama

A collection of AI assistant projects powered by **LangChain**, **Ollama**, and **Mistral LLM**, running completely locally on your machine without relying on external APIs.

## Projects Included

### 1. AI Chatbot with Memory

A context-aware chatbot that remembers previous messages during a conversation using LangChain's ChatMessageHistory.

#### Features

- Local LLM inference using Ollama
- Powered by Mistral LLM
- Conversation memory using ChatMessageHistory
- Context-aware responses
- Interactive command-line chatbot
- Privacy-friendly local execution

---

### 2. AI Voice Assistant

A voice-enabled AI assistant that can listen to user speech, generate responses using Mistral, and speak responses back to the user.

#### Features

- Speech-to-Text using SpeechRecognition
- Text-to-Speech using pyttsx3
- Local AI responses using Ollama and Mistral
- Conversation memory with LangChain
- Voice-based interaction
- Fully offline execution

## Tech Stack

- Python
- LangChain
- Ollama
- Mistral LLM
- SpeechRecognition
- PyAudio
- pyttsx3
- ChatMessageHistory

## Installation

### 1. Install Ollama

Download and install Ollama:

https://ollama.com

### 2. Pull the Mistral Model

```bash
ollama pull mistral
```

### 3. Install Dependencies

```bash
pip install langchain
pip install langchain-community
pip install langchain-core
pip install langchain-ollama
pip install SpeechRecognition
pip install pyttsx3
pip install pyaudio
```

## Running the AI Chatbot

```bash
python basic_ai_agen.py
```

Example:

```text
You: My name is Prachi

AI: Nice to meet you, Prachi!

You: What is my name?

AI: Your name is Prachi.
```

## Running the AI Voice Assistant

```bash
python ai_voice_assit.py
```

Example Workflow:

```text
🎤 Listening...

🗣️ You Said: What is artificial intelligence?

🤖 AI Response:
Artificial Intelligence (AI) refers to...
```

The assistant listens to your voice, processes the request using Mistral, and speaks the response back.

## Future Improvements

- Streamlit Web Interface
- Retrieval-Augmented Generation (RAG)
- PDF Question Answering
- Persistent Memory using SQLite
- Multi-Agent Workflows
- Voice Cloning Integration
- Document Knowledge Assistant

## Learning Outcomes

Through these projects, I gained hands-on experience with:

- Large Language Models (LLMs)
- LangChain Framework
- Prompt Engineering
- Conversational Memory
- Voice AI Systems
- Local AI Deployment
- Ollama Model Serving

## Author

Prachi Jha

GitHub: https://github.com/prachijha05

LinkedIn: https://www.linkedin.com/in/prachi-jha-b084b828b/
