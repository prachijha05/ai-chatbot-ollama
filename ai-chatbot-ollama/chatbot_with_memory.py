# Basic AI Agent with Memory

from langchain_community.chat_message_histories import ChatMessageHistory  # store and manage chat history
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM


# Load AI Model from Ollama
llm = OllamaLLM(model="mistral")    # can use gemma or llama3 model also

# Initialize Memory
chat_history = ChatMessageHistory()   # store user-AI conversation history


# Define AI Chat Prompt
prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="Previous conversation: {chat_history}\nUser: {question}\nAI:"
)


# Function to run AI chat with memory
def run_chain(question):

    # Retrieve chat history manually
    chat_history_text = "\n".join(
        [f"{msg.type.capitalize()}: {msg.content}" for msg in chat_history.messages]
    )

    # Run the AI response generation
    response = llm.invoke(
        prompt.format(
            chat_history=chat_history_text,
            question=question
        )
    )

    # Store new user input and AI response in memory
    chat_history.add_user_message(question)
    chat_history.add_ai_message(response)

    return response   # this will generate AI response in chat


# Interactive CLI chatbot
print("\nAI Chatbot with Memory")
print("Type 'exit' to stop.")

while True:
    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("\nGoodbye!")
        break

    ai_response = run_chain(user_input)
    print(f"\nAI: {ai_response}")