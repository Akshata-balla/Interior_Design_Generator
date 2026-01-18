# theme_config_css.py

CSS_STYLES = """
<style>
    /* Main styling - Midnight Studio Theme */
    .main {
        background-color: #080742; /* Deep Navy from your palette */
    }
    
    /* Animated Gradient Header - Using Navy to Coral Transition */
    .main-header {
        font-size: 3.5rem;
        background: linear-gradient(45deg, #5872ee, #ff8b8b, #ffbc94, #080742);
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
    
    .sub-header {
        font-size: 2rem;
        color: #ffffff;
        border-bottom: 3px solid #ff8b8b; /* Coral Accent */
        padding-bottom: 0.8rem;
        margin-bottom: 2rem;
        font-weight: 600;
        position: relative;
        overflow: hidden;
    }
    
    /* Dark Feature Cards with Coral/Peach Glow */
    .feature-card {
        background: rgba(255, 255, 255, 0.05);
        color: #e0e0e0;
        padding: 2.5rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
    }
    
    .feature-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 40px rgba(255, 139, 139, 0.2); /* Coral Glow */
        border: 1px solid rgba(255, 139, 139, 0.5);
    }
    
    /* Dark Mode Tabs - Using the Electric Blue and Navy */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(8, 7, 66, 0.6); /* Navy with Transparency */
        backdrop-filter: blur(15px);
        padding: 12px;
        border-radius: 18px;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(88, 114, 238, 0.3);
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #5872ee, #010c92) !important; /* Electric Blue to Navy */
        color: white !important;
        box-shadow: 0 4px 15px rgba(88, 114, 238, 0.4);
    }

    /* AI Description Box - Peach Left Border */
    .ai-description {
        background: rgba(255, 255, 255, 0.03);
        border-left: 5px solid #ffbc94; /* Peach Accent */
        padding: 2rem;
        border-radius: 15px;
        color: #d1d1d1;
        font-style: italic;
    }

    /* Radial Background using your Palette Colors */
    .stApp {
        background: radial-gradient(circle at top right, #010c92, #080742);
        background-attachment: fixed;
    }
</style>
"""
