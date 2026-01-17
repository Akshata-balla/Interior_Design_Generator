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
    st.markdown('<h1 class="main-header">AI Interior Design Generator</h1>', unsafe_allow_html=True)
    st.markdown("""
        <div class="feature-card">
            <h2>Welcome to Your AI Design Studio</h2>
            <p>Transform any room instantly using advanced AI. Upload a photo, 
            choose a style, and let the designer agent do the rest.</p>
        </div>
    """, unsafe_allow_html=True)

def display_upload_tab(preprocessor):
    st.markdown('<h2 class="sub-header">1. Upload Your Room Photo</h2>', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Upload an image of the room you want to redesign", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # This calls the function in preprocessor.py
        processed_img = preprocessor.process(uploaded_file)
        st.session_state.uploaded_image = processed_img
        
        st.image(processed_img, caption="Original Room Photo", use_container_width=True)
        st.success("Image uploaded and processed successfully! Move to the 'Design' tab.")

def display_design_tab():
    st.markdown('<h2 class="sub-header">2. Configure Your Design</h2>', unsafe_allow_html=True)
    if st.session_state.uploaded_image is None:
        st.warning("Please upload an image in the 'Upload' tab first.")
        return

    col1, col2 = st.columns(2)
    with col1:
        st.selectbox("Design Theme", ["Modern", "Scandinavian", "Industrial", "Bohemian", "Minimalist"])
    with col2:
        st.text_area("Specific Instructions", placeholder="e.g. Add a blue velvet sofa and oak flooring...")

def display_results_tab(generator, postprocessor, llm_designer_agent):
    st.markdown('<h2 class="sub-header">3. Your AI Transformation</h2>', unsafe_allow_html=True)
    if st.session_state.uploaded_image is None:
        st.error("Missing input image. Please upload one in the 'Upload' tab.")
        return

    if st.button("Generate Design"):
        with st.spinner("AI Designer is reimagining your space..."):
            # Logic for calling generator would go here
            st.info("Generation logic triggered.")

def display_about_tab():
    st.markdown('<div class="info-box"><h3>About the AI Interior Designer</h3><p>Version 1.0.0 powered by Gemini and Stable Diffusion.</p></div>', unsafe_allow_html=True)
