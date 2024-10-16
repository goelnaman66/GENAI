from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langserve import add_routes

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(model="Gemma2-9b-It", groq_api_key=groq_api_key)



# Create Prompt Templates
system_template = "translate the following into {langauge}:"
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ('user', '{text}')
    ]
)

parser = StrOutputParser()

chain = prompt_template | llm | parser


# APP Definition

app = FastAPI(title="Langchain Server",
              version="1.0",
              description="A simple API server using langchain runnable interfaces")


## Adding chain routes
add_routes(
    app,
    chain,
    path="/chain"
)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port = 8005)