import streamlit as st
import base64

# ------------------------------
# Page Config
# ------------------------------
st.set_page_config(page_title="GenAI Gallery", page_icon="🤖", layout="wide")

# ------------------------------
# Load Images as Base64
# ------------------------------
def get_base64(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

bg_img = get_base64("webbackground.png")
# logo_img = get_base64("EY Logo.png")

# ------------------------------
# CSS Styling
# ------------------------------
st.markdown(
    f"""
    <style>
        /* Background */
        .stApp {{
            background: url("data:image/png;base64,{bg_img}");
            background-size: cover;
            background-position: center;
        }}
        /* Logo */
        .logo-container {{
            display: flex;
            align-items: center;
            justify-content: flex-start;
            margin-bottom: 10px;
        }}
        .logo-container img {{
            width: 120px;
        }}
        /* Title */
        h1 {{
            text-align: center;
            color: white !important;
        }}
        /* Cards */
        .app-card {{
            border: 2px solid #FFD500; /* EY Yellow */
            border-radius: 15px;
            padding: 30px 20px;
            text-align: center;
            background-color: rgba(0,0,0,0.7); /* semi-transparent black */
            color: white;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.5);
            transition: all 0.3s ease-in-out;
            height: 150px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .app-card:hover {{
            background-color: rgba(255,213,0,0.9); /* Yellow hover */
            color: black;
            transform: translateY(-5px);
            box-shadow: 4px 4px 12px rgba(0,0,0,0.8);
        }}
        .app-link {{
            text-decoration: none !important;
            color: inherit;
            font-size: 18px;
            font-weight: 600;
        }}

        .app-link:hover {{
            text-decoration: none !important;  /* 👈 this removes the underline */
            }}
        /* Descriptions */
        .desc {{
            text-align: center;
            font-size: 14px;
            margin-top: 10px;
            color: white;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ------------------------------
# Header with Logo
# ------------------------------
# st.markdown(
#     f"""
#     <div class="logo-container">
#         <img src="data:image/png;base64,{logo_img}">
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

st.markdown("<h1>GenAI Gallery</h1>", unsafe_allow_html=True)
st.markdown("---")

# ------------------------------
# Apps + Descriptions
# ------------------------------
apps = [
    {
        "name": "📊 Project Compliance Assessment Tool",
        "url": "https://project-compliance-assessment-tool.vercel.app/",
        "desc": "Helps assess compliance levels for projects with automated scoring."
    },
    {
        "name": "📑 Contract Analyzer",
        "url": "https://contract-analyser-gemini-ttmesivvnk87vwgy6sn2q5.streamlit.app/",
        "desc": "AI-powered tool to analyze contracts and highlight risks & key clauses."
    },
    {
        "name": "📂 PDF Analyser",
        "url": "https://ey-pdf-analyser-gyh5rcrq67ryebaxfnzsek.streamlit.app/",
        "desc": "Extracts and summarizes insights from PDF documents efficiently."
    },
    {
        "name": "🤖 Risk & Compliance Chatbot",
        "url": "https://chatbotgit-ircaoqjrauujwxeaxsculf.streamlit.app/",
        "desc": "Interactive chatbot to answer compliance and regulatory queries."
    },
    {
        "name": "📈 SOC Dashboard",
        "url": "https://project-app.streamlit.app/",
        "desc": "Security Operations Center dashboard for monitoring and insights."
    }
]

# ------------------------------
# Display Cards
# ------------------------------
cols = st.columns(5)

for app, col in zip(apps, cols):
    with col:
        st.markdown(
            f"""
            <a href="{app['url']}" target="_blank" class="app-link">
                <div class="app-card">{app['name']}</div>
            </a>
            <div class="desc">{app['desc']}</div>
            """,
            unsafe_allow_html=True,
        )


