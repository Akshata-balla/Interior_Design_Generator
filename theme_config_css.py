CSS_STYLES = """
<style>
    /* 1. Main Background - Using 80ED99 */
    .stApp {
        background-color: #80ED99 !important;
        background-image: linear-gradient(180deg, #80ED99 0%, #57CC99 100%) !important;
        background-attachment: fixed;
    }

    /* 2. FORCE ALL TEXT TO BLACK - Ensures 100% Visibility */
    html, body, [class*="st-"], p, span, label, .stMarkdown, h1, h2, h3 {
        color: #000000 !important;
        font-weight: 600; /* Slightly bolder for better visibility on green */
    }

    /* 3. Main Header - Using the full Emerald Palette */
    .main-header {
        font-size: 3.5rem;
        /* Using Verdigris (38A3A5) to Keppel (48B89F) to Emerald (57CC99) */
        background: linear-gradient(45deg, #38A3A5, #48B89F, #57CC99, #225A5E);
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

    /* 4. Sharp Square Navigation Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 0px;
        background: #38A3A5 !important; /* Verdigris background for the bar */
        padding: 0px;
        border-radius: 0px; 
    }
    
    .stTabs [data-baseweb="tab"] {
        background: #ffffff !important;
        border-radius: 0px !important; 
        padding: 12px 30px;
        color: #000000 !important; /* Black text on tabs */
        font-weight: 700;
        border: 1px solid #38A3A5 !important;
    }

    /* Active Tab */
    .stTabs [aria-selected="true"] {
        background: #57CC99 !important; /* Emerald active tab */
        color: #000000 !important;
        border-bottom: 5px solid #225A5E !important;
    }

    /* 5. Sharp Square Cards - White background for contrast */
    .feature-card, .info-box, .stAlert, div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.9) !important;
        border: 3px solid #38A3A5 !important;
        color: #000000 !important;
        border-radius: 0px !important;
        box-shadow: 8px 8px 0px #225A5E !important; /* Dark offset shadow */
    }

    /* 6. Inputs & Selectboxes */
    .stSelectbox div[data-baseweb="select"], .stTextArea textarea, .stTextInput input {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 0px !important;
        border: 2px solid #38A3A5 !important;
    }

    /* 7. Enhanced Square Buttons */
    .stButton button {
        background: #225A5E !important; /* Deepest Green */
        color: #ffffff !important; /* White text for contrast on dark green */
        border-radius: 0px !important;
        border: none !important;
        font-weight: 700;
        padding: 15px 40px;
        box-shadow: 4px 4px 0px #38A3A5 !important;
        transition: all 0.3s ease;
    }

    .stButton button:hover {
        background: #48B89F !important; /* Keppel hover */
        color: #000000 !important;
        transform: translate(-2px, -2px);
        box-shadow: 6px 6px 0px #225A5E !important;
    }

    /* 8. Sub-headers with Palette Accent */
    .sub-header {
        color: #000000 !important;
        border-left: 10px solid #38A3A5;
        padding-left: 15px;
        background: rgba(255, 255, 255, 0.4);
        font-weight: 700;
        margin-bottom: 1rem;
    }
</style>
"""
