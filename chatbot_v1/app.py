# Q&A Chatbot

from langchain.llms import OpenAI 
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os

## FUnction to load OpenAI model and get responses 
os.environ["OPEN_API_KEY"] = "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"

def get_openai_responses(question):
    llm = OpenAI(openai_api_key = os.getenv("OPEN_API_KEY") , model_name = "text-davinci-003" , temperature = 0.5)
    response = llm(question)
    return response

## Initialize Streamlit app

st.set_page_config(page_title = "Q&A Demo")
st.header("Langchain Application")

input = st.text_input("Input : ", key = "input")
response = get_openai_responses(input)

submit = st.button("Ask the question")

## If ask buttion is clicked

if submit:
    st.subheader("the response is")
    st.write(response)
