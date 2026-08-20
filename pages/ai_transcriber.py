import streamlit as st

st.set_page_config(page_title="AI Transcriber", page_icon="🎤", layout="wide")

st.title("🎤 AI Audio Transcriber")
st.markdown("*Bersenandung atau mainkan melodi, AI akan menuliskannya*")

try:
    with open("ai_transcriber.html", "r", encoding="utf-8") as f:
        html = f.read()
    # Gunakan st.iframe dengan izin mikrofon
    st.iframe(
        srcdoc=html,
        height=800,
        scrolling=True,
        allow="microphone; autoplay"
    )
except FileNotFoundError:
    st.error("⚠️ File ai_transcriber.html tidak ditemukan. Pastikan file ada di root.")