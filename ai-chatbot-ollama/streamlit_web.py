#basic AI Agent with 
import streamlit as st
from langchain_community.chat_message_histories import ChatMessageHistory  # store and manage chat history
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

#load AI model
llm = OllamaLLM(model="mistral")    # can use gemma or llama3 model also
# Initialize Memory
if "chat_history" not in st.session_state:
    st.session_state.chat_history = ChatMessageHistory()  # Stores user-AI conversation history

# Define AI Chat Prompt
prompt = PromptTemplate(
    input_variables=["chat_history", "question"],
    template="Previous conversation: {chat_history}\nUser: {question}\nAI:"
)
# Function to run AI chat with memory
def run_chain(question):

    # Retrieve past chat history
    chat_history_text = "\n".join(
        [
            f"{msg.type.capitalize()}: {msg.content}"
            for msg in st.session_state.chat_history.messages
        ]
    )

    # Generate AI response
    response = llm.invoke(
        prompt.format(
            chat_history=chat_history_text,
            question=question
        )
    )

    # Save conversation to memory
    st.session_state.chat_history.add_user_message(question)
    st.session_state.chat_history.add_ai_message(response)

    return response

# streamlit ui
# Streamlit UI
st.title("🤖 AI Chatbot with Memory")
st.write("Ask me anything!")

user_input = st.text_input("📝 Your Question:")

if user_input:
    response = run_chain(user_input)

    st.write(f"👤**You:** {user_input}")
    st.write(f"🤖**AI:** {response}")

# Show full chat history
st.subheader("📜 Chat History")

for msg in st.session_state.chat_history.messages:
    st.write(f"**{msg.type.capitalize()}**: {msg.content}")