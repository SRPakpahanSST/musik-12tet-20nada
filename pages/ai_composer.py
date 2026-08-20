import streamlit as st

st.set_page_config(page_title="AI Composer", page_icon="🎵", layout="wide")

st.title("🎵 AI Music Composer")
st.markdown("*Ciptakan melodi otomatis dengan kecerdasan buatan*")

try:
    with open("ai_composer.html", "r", encoding="utf-8") as f:
        html = f.read()
    st.components.v1.html(html, height=800, scrolling=True)
except FileNotFoundError:
    st.error("⚠️ File ai_composer.html tidak ditemukan. Pastikan file ada di root.")
