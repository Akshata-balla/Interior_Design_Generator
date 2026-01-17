'''from google import genai
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
    '''
ent color palette, 
    and architectural features like windows or moldings.
    """

import streamlit as st
from google import genai
from PIL import Image

def describe_image_with_gemini(image):
    """
    Analyzes the uploaded room photo using Gemini 2.0 Flash 
    to provide a detailed design context.
    """
    # 1. Initialize client using Streamlit Secrets
    if "GOOGLE_API_KEY" in st.secrets:
        client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
    else:
        st.error("Missing GOOGLE_API_KEY in Streamlit Secrets.")
        return "Error: No API Key found."

    # 2. Define the instruction for the AI
    prompt = """
    Analyze this room photo and provide a detailed 100-word description for a designer. 
    Include: furniture layout, lighting, color palette, and architectural features.
    """

    try:
        # 3. Generate the description
        response = client.models.generate_content(
            model='gemini-2.0-flash',
            contents=[prompt, image]
        )
        return response.text
    except Exception as e:
        return f"Gemini Error: {e}"

def enhance(style_name, user_prompt):
    """
    REQUIRED BY APP.PY:
    Turns a simple user request into a professional prompt for the image generator.
    """
    return f"A professional high-end {style_name} interior design. {user_prompt}. 8k, photorealistic, architectural photography."
