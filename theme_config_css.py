# theme_config_css.py

CSS_STYLES = """
<style>
    /* 1. New Background - Soft Frosted Lavender (Ensures 100% text visibility) */
    .stApp {
        background-color: #f3f0f7;
        background-image: linear-gradient(180deg, #f3f0f7 0%, #e8e4f0 100%);
        background-attachment: fixed;
    }

    /* 2. Main Header - Gradient using your full palette */
    .main-header {
        font-size: 3.5rem;
        background: linear-gradient(45deg, #0B0742, #5A72EE, #9983CF, #FF918B);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 800;
        animation: gradientShift 8s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* 3. Sub-header - Sharp Square with Lavender Accent */
    .sub-header {
        font-size: 1.8rem;
        color: #0B0742; /* Deep Navy for maximum legibility */
        border-left: 10px solid #9983CF; /* Lavender from your image */
        padding: 10px 20px;
        margin-bottom: 1.5rem;
        font-weight: 700;
        background: rgba(255, 255, 255, 0.6);
    }
    
    /* 4. Square Tabs - Clean and Professional */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0px;
        background: #dcd6e8;
        padding: 0px;
        border-radius: 0px; 
        border: 1px solid #c8bed9;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background: #ffffff !important;
        border-radius: 0px !important; 
        padding: 10px 30px;
        color: #0B0742 !important;
        font-weight: 700;
        border: 1px solid #c8bed9 !important;
    }

    /* Active Tab - Deep Navy with Sky Blue Bottom Border */
    .stTabs [aria-selected="true"] {
        background: #0B0742 !important;
        color: #ffffff !important;
        border-bottom: 5px solid #5A72EE !important;
    }

    /* 5. Feature Cards - High Contrast White */
    .feature-card {
        background: #ffffff;
        color: #0B0742;
        padding: 2.5rem;
        border-radius: 0px; 
        margin: 1.5rem 0;
        border: 1px solid #c8bed9;
        box-shadow: 8px 8px 0px #9983CF; /* Lavender Shadow */
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translate(-4px, -4px);
        box-shadow: 12px 12px 0px #FF918B; /* Coral Shadow on hover */
    }

    /* 6. Info Box - Using the Lavender Theme */
    .info-box {
        background: #ffffff;
        border: 1px solid #c8bed9;
        border-left: 10px solid #5A72EE;
        padding: 1.5rem;
        border-radius: 0px;
        color: #0B0742;
        font-weight: 500;
    }

    /* 7. Enhanced Square Buttons */
    .stButton button {
        background: #0B0742;
        color: white;
        border: none;
        padding: 12px 40px;
        border-radius: 0px;
        font-weight: 700;
        box-shadow: 4px 4px 0px #9983CF;
        transition: all 0.2s ease;
    }
    
    .stButton button:hover {
        background: #5A72EE;
        transform: translateY(-2px);
        box-shadow: 6px 6px 0px #0B0742;
    }

    /* 8. Input visibility fix */
    .stSelectbox div[data-baseweb="select"], .stTextArea textarea, .stTextInput input {
        background-color: white !important;
        color: #0B0742 !important;
        border-radius: 0px !important;
        border: 1px solid #c8bed9 !important;
    }
</style>
"""
