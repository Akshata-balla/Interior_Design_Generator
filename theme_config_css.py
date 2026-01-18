# theme_config_css.py

CSS_STYLES = """
<style>
    /* 1. Fix the "Too Blue" problem by using a Neutral Dark Base */
    .stApp {
        background-color: #121212; /* Neutral Deep Charcoal */
        background-image: radial-gradient(circle at 20% 20%, #080742 0%, #121212 100%);
        background-attachment: fixed;
    }

    /* 2. Vibrant Multi-Color Header */
    .main-header {
        font-size: 3.8rem;
        background: linear-gradient(to right, #5872EE, #FF8B8B, #FFBC94);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        font-weight: 800;
        margin-bottom: 2rem;
    }
    
    /* 3. High Contrast Sub-headers */
    .sub-header {
        font-size: 2rem;
        color: #FFBC94; /* Peach text for warmth */
        border-left: 5px solid #FF8B8B; /* Coral side-border instead of bottom */
        padding-left: 15px;
        margin: 2rem 0;
        font-weight: 600;
    }
    
    /* 4. Square-ish Tabs (Removed Circles) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background: #1E1E1E; /* Dark Grey surface */
        padding: 8px;
        border-radius: 4px; /* Square edges */
        border: 1px solid #333333;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        background-color: transparent !important;
        border-radius: 4px !important;
        color: #888888 !important;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    /* Square Selection Highlight with Coral Underline */
    .stTabs [aria-selected="true"] {
        background-color: rgba(88, 114, 238, 0.15) !important; /* Soft Blue Square Tint */
        color: #FFBC94 !important; /* Peach Text */
        border-bottom: 3px solid #FF8B8B !important; /* Sharp Coral Underline */
    }

    /* 5. Feature Cards with Distinct Colors */
    .feature-card {
        background: #1E1E1E; 
        color: #FFFFFF;
        padding: 2rem;
        border-radius: 8px; /* Square-ish */
        border: 1px solid #333333;
        box-shadow: 10px 10px 0px #FF8B8B; /* Retro Sharp Offset Shadow */
    }
    
    /* 6. AI Results Box - Multi-Tone Glass */
    .ai-description {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 188, 148, 0.3);
        border-top: 4px solid #5872EE; /* Blue top */
        border-bottom: 4px solid #FF8B8B; /* Coral bottom */
        padding: 2rem;
        border-radius: 4px;
        color: #E0E0E0;
    }

    /* Fix for Selectboxes and Inputs */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #1E1E1E;
        border: 1px solid #FFBC94;
        color: white;
    }
</style>
"""
