#########################################################
########### BASIC AI AGENT (WITHOUT MEMORY) #############
#########################################################

from langchain_ollama import OllamaLLM

# Load AI Model from Ollama
llm = OllamaLLM(model="mistral")    # can use gemma or llama3 model also

print("\nWelcome to your AI Agent! Ask me anything.")

while True:

    question = input(
        "Your Question (or type 'exit' to stop): "
    )

    if question.lower() == "exit":
        print("Goodbye!")
        break

    response = llm.invoke(question)

    print("\nAI Response:", response)