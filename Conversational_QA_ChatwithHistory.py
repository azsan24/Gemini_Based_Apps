import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Configure Gemini with API key
genai.configure(api_key=api_key)

# Load the Gemini model and start a chat session
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])

# Function to get Gemini response
def ask_gemini(question):
    return chat.send_message(question, stream=True)

# Set up the Streamlit web app
st.set_page_config(page_title="Gemini Chatbot")
st.title("🤖 Gemini LLM Chatbot")

# Store chat history in session state
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Input box and submit button
user_input = st.text_input("Ask something:")
if st.button("Submit") and user_input:
    response = ask_gemini(user_input)
    
    # Save user message
    st.session_state["chat_history"].append(("You", user_input))
    
    # Show and save bot response
    st.subheader("Response:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state["chat_history"].append(("Gemini", chunk.text))

# Display chat history
st.subheader("Chat History:")
for sender, message in st.session_state["chat_history"]:
    st.write(f"{sender}: {message}")
