from langchain_community.llms import Ollama

def get_llm_chain():
    llm = Ollama(model="llama3")
    return llm