import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

st.set_page_config(page_title="Ollama QnA Bot")
st.title("Project 1: QnA Chatbot with LangChain + Ollama + Streamlit")

user_question = st.text_input("Enter your question:")

if user_question:
    llm = OllamaLLM(model="llama3.2", temperature=0.7)

    prompt = ChatPromptTemplate.from_template(
        "You are a helpful assistant. Answer the following question: {question}"
    )

    chain = prompt | llm | StrOutputParser()
    
    response = chain.invoke({"question": user_question})
    
    st.write(response)