from langchain_community.chat_message_histories import ChatMessageHistory  #store and manage  chat histrory
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM


# Load AI Model from Ollama
llm = OllamaLLM(model="mistral")    # can use gemma or lamma 3 modle also
#initialize Memory
chat_history= ChatMessageHistory()  #store user-AI conversation history

#define AI Chat Prompt
prompt= PromptTemplate(
    input_variables=["chat_history" , "question"],
    template="Previous conversation: {chat_history}\nUser: {question}\nAI:"
)
#Function to run AI chat with memory
def run_chain(question):
    #retrieve chat history manually
    chat_history_text = "\n".join(
    [f"{msg.type.capitalize()}: {msg.content}" for msg in chat_history.messages]
)  
    #run the AI response generation
    response=llm.invoke(prompt.format(chat_history=chat_history_text,question=question))

    #store new user input and AI response in memory
    chat_history.add_user_message(question)
    chat_history.add_ai_message(response)

    return response  # thsi will generate AI response in chat

#Interactive CLI chatbot
print("\nAI Chatbot  with Memory")
print("type 'exit' to stop.")

while True:
    user_input = input("\n you: ")
    if user_input.lower()=="exit":
        print("\n goodbye!")
        break
    ai_response= run_chain(user_input)
    print(f"\n AI: {ai_response}")


####### chat without memory#########
#from langchain_ollama import OllamaLLM

# Load AI Model from Ollama
#llm = OllamaLLM(model="mistral")    # can use gemma or lamma 3 modle also

#print("\nWelcome to your AI Agent! Ask me anything.")

#while True:
  #  question = input("Your Question (or type 'exit' to stop): ")

    #if question.lower() == "exit":
        #print("Goodbye!")
      #  break

    #