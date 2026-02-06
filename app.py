import streamlit as st
import tempfile
from llm_router import get_llm
from ppt_generator import improve_existing_slides

st.set_page_config(page_title="Your Text, Your Style – Auto PPT Generator")
st.title("Auto PPT Generator")

text = st.text_area("Paste your text", height=250)
guidance = st.text_input("Optional guidance (e.g. investor pitch deck)")

provider = st.selectbox(
    "Choose LLM Provider",
    ["Groq", "OpenAI", "Anthropic", "Gemini"]
)

api_key = st.text_input("Enter API Key (never stored)", type="password")
template = st.file_uploader(
    "Upload PowerPoint Template (.pptx / .potx)",
    type=["pptx", "potx"]
)

if st.button("Presentation"):
    if not all([text, api_key, template]):
        st.error("All fields are required")
        st.stop()

    llm = get_llm(provider, api_key)

    prompt = f"""
STRICT FORMAT ONLY:

Slide Title: <title>
- bullet
- bullet

Guidance:
{guidance}

TEXT:
{text}
"""

    with st.spinner("Improving slides..."):
        outline = llm.generate(prompt)
        prs = improve_existing_slides(template, outline, text)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".pptx") as tmp:
            prs.save(tmp.name)
            ppt_path = tmp.name

    with open(ppt_path, "rb") as f:
        st.success("Presentation improved successfully!")
        st.download_button(
            "Download PPT",
            f,
            file_name="presentation.pptx"
        )