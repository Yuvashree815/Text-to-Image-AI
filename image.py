import requests
import streamlit as st
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/stabilityai/sdxl-turbo"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

prompt = st.text_input('Enter a prompt')

if st.button('Generate'):
    if prompt:
        image_bytes = query({"inputs": prompt})
        
        # Check if the response is an image
        try:
            image = Image.open(io.BytesIO(image_bytes))
            st.image(image, caption='Generated Image')
        except Exception as e:
            st.error("Failed to generate image. Please try again.")
            st.write(e)
    else:
        st.error("Please enter a prompt.")
