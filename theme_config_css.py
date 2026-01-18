# theme_config_css.py

CSS_STYLES = """
<style>
    /* Main styling - Premium Deep Dark Theme */
    .main {
        background-color: #0e1117;
    }
    
    /* Animated Gradient Header */
    .main-header {
        font-size: 3.5rem;
        background: linear-gradient(45deg, #3498db, #a29bfe, #ff7675, #55efc4);
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
        border-bottom: 3px solid #3498db;
        padding-bottom: 0.8rem;
        margin-bottom: 2rem;
        font-weight: 600;
        position: relative;
        overflow: hidden;
    }
    
    /* Dark Feature Cards with Neon Glow */
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
        box-shadow: 0 20px 40px rgba(52, 152, 219, 0.2);
        border: 1px solid rgba(52, 152, 219, 0.5);
    }
    
    /* Dark Mode Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(15px);
        padding: 12px;
        border-radius: 18px;
        margin-bottom: 1.5rem;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #3498db, #8e44ad) !important;
        color: white !important;
    }

    /* AI Description Box */
    .ai-description {
        background: rgba(255, 255, 255, 0.03);
        border-left: 5px solid #00d2ff;
        padding: 2rem;
        border-radius: 15px;
        color: #d1d1d1;
        font-style: italic;
    }

    /* Deep Space Background */
    .stApp {
        background: radial-gradient(circle at top right, #1e272e, #0f141a);
        background-attachment: fixed;
    }
</style>
"""
