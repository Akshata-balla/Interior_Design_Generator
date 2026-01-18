# theme_config_css.py

CSS_STYLES = """
<style>
    /* 1. Deepen the Background so it is clearly NOT white */
    .stApp {
        background-color: #DCD6E8 !important; 
        background-image: linear-gradient(180deg, #DCD6E8 0%, #C8BED9 100%) !important;
    }

    /* 2. FORCE ALL TEXT TO BLACK */
    /* This targets headers, paragraphs, labels, and markdown */
    html, body, [class*="st-"], .main-header, .sub-header, p, span, label {
        color: #000000 !important;
    }

    /* 3. Gradient Header - Kept colorful but with dark contrast */
    .main-header {
        font-size: 3.5rem;
        background: linear-gradient(45deg, #0B0742, #5A72EE, #9983CF, #000000);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 800;
        animation: gradientShift 8s ease infinite;
    }

    /* 4. SHARP SQUARE TABS - High Contrast */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0px;
        background: #0B0742 !important; /* Navy Bar */
        padding: 0px;
        border-radius: 0px; 
    }
    
    .stTabs [data-baseweb="tab"] {
        background: #ffffff !important;
        border-radius: 0px !important; 
        padding: 10px 30px;
        color: #000000 !important; /* Black Tab Text */
        font-weight: 700;
        border: 1px solid #0B0742 !important;
    }

    /* Active Tab using your Lavender color */
    .stTabs [aria-selected="true"] {
        background: #9983CF !important;
        color: #000000 !important; /* Black text on Lavender */
        border-bottom: 5px solid #FF918B !important; 
    }

    /* 5. Square Content Boxes */
    .info-box, .stAlert, div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.4) !important;
        border: 2px solid #0B0742 !important;
        color: #000000 !important;
        border-radius: 0px !important;
    }

    /* 6. Fix for Input Fields */
    .stSelectbox div[data-baseweb="select"], .stTextArea textarea, .stTextInput input {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 0px !important;
        border: 2px solid #0B0742 !important;
    }

    /* 7. Square Buttons */
    .stButton button {
        background: #0B0742 !important;
        color: #ffffff !important; /* White text looks better on Navy button */
        border-radius: 0px !important;
        box-shadow: 4px 4px 0px #000000 !important;
    }
    
    .stButton button:hover {
        background: #9983CF !important;
        color: #000000 !important;
    }
</style>
"""
