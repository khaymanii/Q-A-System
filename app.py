import os
import streamlit as st
from langchain_community.llms import OpenAI
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the OpenAI API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

#Function to return the response
def load_answer(question):
    llm = OpenAI(model_name="gpt-3.5-turbo-instruct",temperature=0)
    answer=llm(question)
    return answer


#App UI starts here
st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("Simple Q & A App")

#Gets the user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text


user_input=get_text()
response = load_answer(user_input)

submit = st.button('Generate')  

#If generate button is clicked
if submit:

    st.subheader("Answer:")

    st.write(response)

