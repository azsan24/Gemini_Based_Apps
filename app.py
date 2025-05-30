import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Gemini Pro model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Function to get response from Gemini
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Streamlit app UI
st.set_page_config(page_title="Gemini Pro Chatbot", page_icon="🤖")
st.title("🤖 Gemini Pro Chatbot")

user_input = st.text_input("Enter your message:")
submit = st.button("Submit")

# Handle submission
if submit and user_input:
    response = get_gemini_response(user_input)
    st.subheader("Response:")
    st.write(response)


