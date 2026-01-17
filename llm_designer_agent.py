'''
from google import genai
from PIL import Image
import streamlit as st

def describe_image_with_gemini(image):
    """Describe image using the new Google Gen AI SDK"""
    
    # 1. Initialize the client using your secret key
    if "GOOGLE_API_KEY" in st.secrets:
        client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
    else:
        st.error("Missing GOOGLE_API_KEY in Streamlit Secrets")
        return "Error: No API Key"

    # 2. Define the refined prompt
    prompt = """
    Describe this room in a detailed paragraph. Mention:
    - Visible furniture and layout
    - Colors, textures, and lighting
    - Current interior style
    - Suggestions for a modern redesign
    """

    try:
        # 3. Generate content using Gemini 2.0 Flash
        # Note: The new SDK handles PIL images directly in the list
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=[prompt, image]
        )
        return response.text
    except Exception as e:
        return f"Error during description: {e}"

def enhance(style_name, user_prompt):
    """Standard prompt enhancement for the image generator"""
    return f"A professional {style_name} interior design. {user_prompt}. 8k, photorealistic."
    
ent color palette, 
    and architectural features like windows or moldings.

'''


import streamlit as st
import google.generativeai as genai

def analyze_room(image, style_pref):
    """
    Connects to Gemini to provide design feedback.
    """
    # Look for the API Key in Streamlit Secrets
    api_key = st.secrets.get("GOOGLE_API_KEY")
    
    if not api_key:
        return "Please configure your GOOGLE_API_KEY in Streamlit Secrets to get AI advice."

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"As a professional interior designer, look at this image and suggest how to achieve a {style_pref} style."
        
        # If image is provided, send both prompt and image
        if image:
            response = model.generate_content([prompt, image])
        else:
            response = model.generate_content(prompt)
            
        return response.text
    except Exception as e:
        return f"AI Agent is resting (Error: {str(e)})"
