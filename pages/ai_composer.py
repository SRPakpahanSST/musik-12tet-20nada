import streamlit as st

st.set_page_config(page_title="AI Composer", page_icon="🎵")

st.title("🎵 AI Composer")

# Baca file HTML yang sudah dibuat
with open("ai_composer.html", "r", encoding="utf-8") as f:
    html = f.read()

# Tampilkan di iframe
st.components.v1.html(html, height=800, scrolling=True)