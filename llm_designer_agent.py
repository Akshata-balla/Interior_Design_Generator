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
from google import genai

def analyze_room(image, style_pref):
    """
    Connects to Gemini 2.0 to provide design feedback.
    """
    # Pull the API Key from your Streamlit Secrets
    api_key = st.secrets.get("GOOGLE_API_KEY")
    
    if not api_key:
        return "API Key missing. Please add GOOGLE_API_KEY to your Streamlit Secrets."

    try:
        # The new 2026 Client syntax
        client = genai.Client(api_key=api_key)
        
        prompt = f"You are a professional interior designer. Analyze this room and suggest a {style_pref} transformation."
        
        # Use the newest model version
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[prompt, image] if image else prompt
        )
            
        return response.text
    except Exception as e:
        return f"Designer is currently unavailable: {str(e)}"

