import os
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai
from PIL import Image

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure Gemini API
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize Gemini Pro model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

def get_gemini_response(input_text, image):
    if input_text:
        response = model.generate_content([input_text, image])
    else:
        response = model.generate_content(image)
    return response.text

# Streamlit app UI
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini Application")

# Text input
input_text = st.text_input("Input Prompt:")

# File uploader for image
uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # Submit button
    if st.button("Generate Response"):
        with st.spinner("Generating response..."):
            response = get_gemini_response(input_text, image)
            st.subheader("Gemini Response:")
            st.write(response)

