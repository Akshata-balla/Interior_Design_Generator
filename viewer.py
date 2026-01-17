'''
import streamlit as st

def display_home_tab():
    st.header("🏠 Welcome to AI Interior Designer")
    st.write("Transform your space using the power of AI.")
    st.info("Start by navigating to the **Upload** tab to provide a photo of your room.")

def display_upload_tab(preprocessor):
    st.header("📸 Upload Your Room")
    uploaded_file = st.file_uploader("Choose a room photo...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        st.session_state.uploaded_image = uploaded_file
        st.image(uploaded_file, caption="Original Image", use_container_width=True)
        
        if st.button("Process Image"):
            with st.spinner("Analyzing room layout..."):
                # This calls the preprocessor module you imported in app.py
                result = preprocessor.process(uploaded_file)
                st.session_state.segmentation_done = True
                st.success("Room analysis complete!")

def display_design_tab():
    st.header("🎨 Choose Your Style")
    style = st.selectbox("Select a Style", ["Modern", "Minimalist", "Industrial", "Bohemian", "Scandinavian"])
    color_palette = st.color_picker("Pick a base color", "#ffffff")
    prompt = st.text_area("Additional instructions", placeholder="e.g. Add a velvet blue sofa and gold lamps")
    
    # Store these in session state to use in the Results tab
    st.session_state.design_style = style
    st.session_state.design_prompt = prompt

def display_results_tab(generator, postprocessor, llm_designer_agent):
    st.header("✨ Generated Design")
    
    if st.session_state.uploaded_image is None:
        st.warning("Please upload an image first!")
        return

    if st.button("Generate Final Design"):
        with st.spinner("Reimagining your space..."):
            # This uses the generator module to call the AI
            try:
                # 1.Enhance prompt with LLM agent
                enhanced_prompt = llm_designer_agent.enhance(st.session_state.design_style, st.session_state.design_prompt)
                
                # 2. Generate image
                generated_url = generator.generate(st.session_state.uploaded_image, enhanced_prompt)
                
                # 3. Post-process (e.g. upscaling)
                final_image = postprocessor.clean_up(generated_url)
                
                st.image(final_image, caption="Your New Room", use_container_width=True)
                st.session_state.generated_images.append(final_image)
            except Exception as e:
                st.error(f"Generation failed: {e}")

def display_about_tab():
    st.header("ℹ️ About this Project")
    st.write("Created with Streamlit and Stable Diffusion.")
    st.write("This tool uses ControlNet architecture to maintain the structure of your room while changing the furniture and decor.")
'''
import streamlit as st

def display_home_tab():
    # Uses .main-header for the animated gradient effect
    st.markdown('<h1 class="main-header">AI Interior Design Studio</h1>', unsafe_allow_html=True)
    
    # Uses .feature-card for the 3D white card effect
    st.markdown("""
        <div class="feature-card">
            <h3 style="color: #2c3e50; margin-top: 0;">Reimagine Your Living Space</h3>
            <p>Leverage state-of-the-art AI to transform your room. Our system analyzes 
            your architecture and applies professional design styles in seconds.</p>
        </div>
    """, unsafe_allow_html=True)

def display_upload_tab(preprocessor):
    st.markdown('<h2 class="sub-header">Step 1: Upload Your Space</h2>', unsafe_allow_html=True)
    
    # Custom container for the uploader
    st.markdown('<div class="design-card">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Choose a high-quality photo of your room...", type=["jpg", "jpeg", "png"])
    st.markdown('</div>', unsafe_allow_html=True)
    
    if uploaded_file is not None:
        processed_img = preprocessor.process(uploaded_file)
        st.session_state.uploaded_image = processed_img
        st.image(processed_img, caption="Detected Room Layout", use_container_width=True, output_format="PNG")
        st.markdown('<div class="success-box">✅ Image successfully analyzed!</div>', unsafe_allow_html=True)

def display_design_tab():
    st.markdown('<h2 class="sub-header">Step 2: Define Your Aesthetic</h2>', unsafe_allow_html=True)
    
    if st.session_state.uploaded_image is None:
        st.warning("Please upload a photo in the 'Upload' tab first.")
        return

    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        style = st.selectbox("Select Design Theme", 
                             ["Modern Minimalist", "Scandinavian", "Industrial Loft", "Bohemian", "Luxury Classic"])
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="info-box">', unsafe_allow_html=True)
        custom_prompt = st.text_input("Special Requests", placeholder="e.g., Add a marble coffee table...")
        st.markdown('</div>', unsafe_allow_html=True)

def display_results_tab(generator, postprocessor, llm_designer_agent):
    st.markdown('<h2 class="sub-header">Step 3: Final Transformation</h2>', unsafe_allow_html=True)
    
    if st.session_state.uploaded_image is None:
        st.error("No image found. Please go back to the Upload tab.")
        return

    if st.button("Generate 3D Render"):
        with st.spinner("AI Designer is calculating lighting and textures..."):
            # This uses the .ai-description class for the italicized box
            st.markdown(f"""
                <div class="ai-description">
                    "The AI Agent suggests focusing on the natural light from the left window 
                    to highlight the new textures..."
                </div>
            """, unsafe_allow_html=True)
            
            # Placeholder for the actual generation logic
            st.info("Generation process started...")

def display_about_tab():
    st.markdown("""
        <div class="feature-card">
            <h2 style="color: #3498db;">System Information</h2>
            <p><b>Model:</b> Gemini 3 Flash & Stable Diffusion XL</p>
            <p><b>Version:</b> 2026.1.0</p>
            <hr>
            <p>This tool is designed for interior designers and homeowners to 
            visualize architectural changes instantly.</p>
        </div>
    """, unsafe_allow_html=True)
