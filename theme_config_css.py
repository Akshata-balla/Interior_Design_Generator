# theme_config_css.py

CSS_STYLES = """
<style>
    /* Main styling - Enhanced Clean White Theme */
    .main {
        background-color: #ffffff;
    }
    
    /* Animated Gradient Header */
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
    
    .sub-header {
        font-size: 2rem;
        color: #2c3e50;
        border-bottom: 3px solid #3498db;
        padding-bottom: 0.8rem;
        margin-bottom: 2rem;
        font-weight: 600;
        position: relative;
        overflow: hidden;
    }
    
    .sub-header::after {
        content: '';
        position: absolute;
        bottom: -3px;
        left: -100%;
        width: 100%;
        height: 3px;
        background: linear-gradient(90deg, transparent, #e74c3c, transparent);
        animation: slideLine 3s ease-in-out infinite;
    }
    
    @keyframes slideLine {
        0% { left: -100%; }
        50% { left: 100%; }
        100% { left: 100%; }
    }
    
    /* Enhanced Cards with 3D Effects */
    .feature-card {
        background: linear-gradient(135deg, #ffffff 0%, #f8f9fa 100%);
        color: #2c3e50;
        padding: 2.5rem;
        border-radius: 20px;
        margin: 1.5rem 0;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        border: 1px solid #e1e8ed;
        position: relative;
        overflow: hidden;
    }
    
    .feature-card:hover {
        transform: translateY(-10px) scale(1.02);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
    }
    
    /* Enhanced Tabs with Glass Morphism */
    .stTabs [data-baseweb="tab-list"] {
        gap: 6px;
        background: rgba(255, 255, 255, 0.8);
        backdrop-filter: blur(10px);
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 1.5rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
        width: fit-content !important;
    }
    
    .stTabs [data-baseweb="tab"] {
        height: 52px;
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-radius: 13px;
        padding: 12px 22px;
        color: #2c3e50;
        font-weight: 600;
        font-size: 1.2rem;
        transition: all 0.3s ease;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #3498db, #2980b9) !important;
        color: white !important;
    }

    /* AI Description Box */
    .ai-description {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        border-left: 5px solid #3498db;
        padding: 2rem;
        border-radius: 15px;
        margin: 1.5rem 0;
        font-style: italic;
    }

    /* Background Animation */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        background-attachment: fixed;
    }
</style>
"""
