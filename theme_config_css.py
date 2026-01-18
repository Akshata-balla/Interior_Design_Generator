# theme_config_css.py

CSS_STYLES = """
<style>
    /* 1. Main Background - Clean White */
    .stApp {
        background: #ffffff;
        background-attachment: fixed;
    }

    /* 2. Animated Gradient Header - Original Colors (#2c3e50, #3498db, #9b59b6, #e74c3c) */
    .main-header {
        font-size: 3.5rem;
        background: linear-gradient(45deg, #2c3e50, #3498db, #9b59b6, #e74c3c);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 700;
        padding: 1rem;
        animation: gradientShift 8s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* 3. Sub-header - Sharp Square Left Border */
    .sub-header {
        font-size: 2rem;
        color: #2c3e50;
        border-left: 8px solid #3498db; /* Sharp Square Accent */
        padding-left: 15px;
        margin-bottom: 2rem;
        font-weight: 600;
        background: #f8f9fa;
    }
    
    /* 4. Square Tabs - No Circles, Clean Lines */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0px; /* Merged square look */
        background: #f8f9fa;
        padding: 0px;
        border-radius: 0px; 
        border: 1px solid #e1e8ed;
        width: fit-content !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 55px;
        background: #ffffff !important;
        border-radius: 0px !important; /* Forces Square */
        padding: 10px 25px;
        color: #2c3e50 !important;
        font-weight: 600;
        border: 1px solid #e1e8ed !important;
        margin: 0px !important;
    }
    
    /* Square Selection Highlight with Original Blue Underline */
    .stTabs [aria-selected="true"] {
        background: #3498db !important;
        color: white !important;
        border-bottom: 4px solid #2c3e50 !important;
    }

    /* 5. Feature Cards - Original White/Gray Gradient with Square Corners */
    .feature-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        color: #2c3e50;
        padding: 2.5rem;
        border-radius: 0px; /* Sharp Square */
        margin: 1.5rem 0;
        box-shadow: 10px 10px 0px #3498db; /* Sharp offset shadow */
        border: 1px solid #e1e8ed;
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translate(-5px, -5px);
        box-shadow: 15px 15px 0px #e74c3c; /* Red highlight on hover */
    }

    /* 6. AI Description Box - Square & Clean */
    .ai-description {
        background: #f8f9fa;
        border: 1px solid #e1e8ed;
        border-left: 10px solid #3498db;
        padding: 2rem;
        border-radius: 0px;
        font-style: italic;
        color: #2c3e50;
    }

    /* 7. Enhanced Square Buttons */
    .stButton button {
        background: #3498db;
        color: white;
        border: none;
        padding: 15px 35px;
        border-radius: 0px; /* Sharp Square */
        font-weight: 600;
        box-shadow: 5px 5px 0px #2c3e50;
        transition: all 0.2s ease;
    }
    
    .stButton button:hover {
        background: #e74c3c;
        transform: translate(-2px, -2px);
        box-shadow: 7px 7px 0px #2c3e50;
    }

    /* Input fields - Original styling but Square */
    .stTextArea textarea, .stTextInput input {
        border-radius: 0px !important;
        border: 2px solid #e1e8ed;
        background: #ffffff;
    }
</style>
"""
