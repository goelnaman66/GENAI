# Simple OpenAI app using GEnAI

import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")
## Langsmith tracking

os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY")
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

## Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpful assistant. Please respond to the question asked"),
        ("user", "Question: {question}")

    ]
)

## streamlit framework 
st.title("Ollama App")
input_text = st.text_input("Something you have in mind...")

### ollma llama2
llm = Ollama(model="llama2")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)