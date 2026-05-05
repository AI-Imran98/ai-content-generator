import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

# Page config
st.set_page_config(
    page_title="AI Content Generator",
    page_icon="✍️",
    layout="centered"
)

# Title
st.title("✍️ AI Content Generator")
st.subheader("Generate professional content instantly!")

# Content type selection
content_type = st.selectbox(
    "Select content type:",
    [
        "Blog Post",
        "Email",
        "Social Media Post",
        "Product Description",
        "Cover Letter"
    ]
)

# Topic input
topic = st.text_input("Enter your topic or subject:")

# Tone selection
tone = st.selectbox(
    "Select tone:",
    ["Professional", "Friendly", "Formal", "Casual", "Persuasive"]
)

# Word count
word_count = st.slider(
    "Approximate word count:",
    min_value=50,
    max_value=500,
    value=200,
    step=50
)

# Generate function
def generate_content(content_type, topic, tone, word_count):
    prompt = f"""
    Write a {content_type} about: {topic}
    
    Requirements:
    - Tone: {tone}
    - Approximate word count: {word_count} words
    - Make it engaging and professional
    - Ready to use, no placeholders
    
    Write only the content, no explanations.
    """
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    return response.text

# Generate button
if st.button("🚀 Generate Content", type="primary"):
    if topic:
        with st.spinner("Generating content..."):
            content = generate_content(
                content_type, topic, tone, word_count
            )
        
        st.success("✅ Content generated!")
        
        # Show content
        st.markdown("### Generated Content:")
        st.markdown(content)
        
        # Copy button
        st.code(content, language=None)
        
    else:
        st.warning("⚠️ Please enter a topic first!")

# Footer
st.markdown("---")
st.markdown("*Powered by Google Gemini AI*")