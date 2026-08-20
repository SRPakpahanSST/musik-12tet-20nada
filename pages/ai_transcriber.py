import streamlit as st

st.set_page_config(page_title="AI Transcriber", page_icon="🎤")

st.title("🎤 AI Transcriber")

with open("ai_transcriber.html", "r", encoding="utf-8") as f:
    html = f.read()

st.components.v1.html(html, height=800, scrolling=True)