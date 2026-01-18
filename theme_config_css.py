# theme_config_css.py

CSS_STYLES = """
<style>
    /* 1. Base Structure - Deep Charcoal instead of Blue to fix "too blue" issue */
    .stApp {
        background: #121212; 
        background-image: radial-gradient(circle at 20% 20%, #080742 0%, #121212 100%);
        background-attachment: fixed;
        color: #ffffff;
    }

    /* 2. Main Header - Animated Multi-Tone Gradient */
    .main-header {
        font-size: 3.8rem;
        background: linear-gradient(45deg, #5872EE, #FF8B8B, #FFBC94, #5872EE);
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 2rem;
        font-weight: 800;
        padding: 1rem;
        animation: gradientShift 8s ease infinite;
    }
    
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* 3. Sub-header - Sharp Square Left Border (Peach Accent) */
    .sub-header {
        font-size: 2.2rem;
        color: #FFBC94; 
        border-left: 6px solid #FF8B8B;
        padding-left: 20px;
        margin-bottom: 2rem;
        font-weight: 600;
        background: rgba(255, 255, 255, 0.03);
    }
    
    /* 4. Sharp Square Tabs - Fixed Right Space and Shapes */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: #1E1E1E;
        padding: 10px;
        border-radius: 4px; /* Sharp edges */
        border: 1px solid #333333;
        width: fit-content !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        background: #252525 !important;
        border-radius: 4px !important; /* Square shape */
        padding: 10px 25px;
        color: #888888 !important;
        font-weight: 600;
        transition: all 0.3s ease;
        border: 1px solid transparent !important;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        color: #5872EE !important;
        background: #2A2A2A !important;
    }

    /* Active Tab - Coral Underline with Blue Tint */
    .stTabs [aria-selected="true"] {
        background: rgba(88, 114, 238, 0.15) !important;
        color: #FFBC94 !important;
        border-bottom: 4px solid #FF8B8B !important; /* Square sharp underline */
    }

    /* 5. Feature Cards - Square with Retro Shadow */
    .feature-card {
        background: #1E1E1E;
        color: #ffffff;
        padding: 2.5rem;
        border-radius: 4px; /* Square */
        margin: 1.5rem 0;
        border: 1px solid #333333;
        box-shadow: 8px 8px 0px #5872EE; /* Sharp Offset Shadow */
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translate(-4px, -4px);
        box-shadow: 12px 12px 0px #FF8B8B; /* Switches color on hover */
    }

    /* 6. AI Results Box - Square Glass Morphism */
    .ai-description {
        background: rgba(255, 255, 255, 0.03);
        border-left: 5px solid #FFBC94;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
        padding: 2rem;
        border-radius: 0px; /* Fully square */
        margin: 1.5rem 0;
        font-style: italic;
        color: #E0E0E0;
    }

    /* 7. Enhanced Buttons - Square and Bold */
    .stButton button {
        background: linear-gradient(135deg, #FF8B8B, #FFBC94);
        color: #080742; /* Dark text for contrast */
        border: none;
        padding: 12px 30px;
        border-radius: 4px; /* Square */
        font-weight: 700;
        box-shadow: 4px 4px 0px #5872EE;
        transition: all 0.2s ease;
    }
    
    .stButton button:hover {
        transform: translate(-2px, -2px);
        box-shadow: 6px 6px 0px #ffffff;
        background: linear-gradient(135deg, #FFBC94, #FF8B8B);
    }

    /* Inputs and Selectors */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #1E1E1E;
        border: 1px solid #333333;
        border-radius: 4px;
        color: white;
    }
    
    .stSelectbox div[data-baseweb="select"]:focus {
        border-color: #FFBC94;
    }
</style>
"""
