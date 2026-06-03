from langchain_ollama import OllamaLLM

# load AI model form ollama
llm=OllamaLLM(model="mistral")     # mistral is  rpelaced by lamma 3 or gemma
print("\n Welcome to your AI Agent! ask me anything.")
while True:
    question=input("your Question (or type 'exit' to stop); " )
    if question.strip().lower()=="exit":
        print("Goodby!")
        break
    response= llm.invoke(question)
    print("\n AI response: ", response)  

