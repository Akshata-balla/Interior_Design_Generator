# theme_config_css.py

CSS_STYLES = """
<style>
    /* Main styling - Midnight Studio Theme with High-Contrast Accents */
    .stApp {
        background: radial-gradient(circle at top right, #010c92, #080742, #040320);
        background-attachment: fixed;
    }

    /* Animated Gradient Header - Mixing the full palette */
    .main-header {
        font-size: 3.5rem;
        background: linear-gradient(45deg, #5872ee, #FF8B8B, #FFBC94, #5872ee);
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
    
    /* Sub-header with a bright Peach-Coral Underline */
    .sub-header {
        font-size: 2.2rem;
        color: #FFBC94; /* Peach color for text visibility */
        border-bottom: 3px solid #FF8B8B; /* Coral Accent */
        padding-bottom: 0.5rem;
        margin-bottom: 1.5rem;
        font-weight: 600;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    /* Cards with a soft Blue Glow but Coral Hover effect */
    .feature-card {
        background: rgba(255, 255, 255, 0.07);
        color: #ffffff;
        padding: 2rem;
        border-radius: 20px;
        margin: 1rem 0;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.8);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(88, 114, 238, 0.2);
        transition: all 0.3s ease;
    }
    
    .feature-card:hover {
        transform: translateY(-5px);
        border: 1px solid #FF8B8B; /* Glows Coral on hover */
        box-shadow: 0 12px 40px rgba(255, 139, 139, 0.2);
    }
    
    /* Tabs - Improved contrast to stop the "all blue" look */
    .stTabs [data-baseweb="tab-list"] {
        gap: 12px;
        background: rgba(4, 3, 32, 0.8); 
        padding: 10px 20px;
        border-radius: 50px; /* Pill shape */
        border: 1px solid #5872ee;
    }
    
    .stTabs [data-baseweb="tab"] {
        color: #5872ee !important; /* Electric Blue for inactive tabs */
        font-weight: 700;
    }

    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #FF8B8B, #FFBC94) !important; /* Coral-Peach Active Tab */
        color: #080742 !important; /* Dark Navy text for readability on bright tab */
        border-radius: 40px !important;
        box-shadow: 0 4px 15px rgba(255, 139, 139, 0.4);
    }

    /* AI Description Box - Warm Glow */
    .ai-description {
        background: rgba(255, 188, 148, 0.1); /* Very faint Peach background */
        border-left: 6px solid #FFBC94; /* Solid Peach Border */
        padding: 2rem;
        border-radius: 10px;
        color: #ffffff;
        font-size: 1.1rem;
        line-height: 1.6;
        box-shadow: inset 0 0 15px rgba(0,0,0,0.2);
    }

    /* Input elements customization */
    .stSelectbox div[data-baseweb="select"] {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid #5872ee;
        color: white;
    }
</style>
"""
