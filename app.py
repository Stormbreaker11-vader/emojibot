#from langchain_openai import OpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
#os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
[
        ("system", "You are a helpful asistant PLease response to the user and if you don't know the answer simply say nahi pata bhai"),
        ("user", "Question:{question}")
    ]
)

#framework for streamlit


st.title('my chatbot')
input_text=st.text_input("kuch bhi puchle bhai")

#run ollama phi3

llm=Ollama(model="m/emojitron")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

