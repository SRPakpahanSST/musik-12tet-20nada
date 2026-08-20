import streamlit as st

st.set_page_config(page_title="Chord Progression Generator", page_icon="🎵", layout="wide")

st.title("🎵 Chord Progression Generator")
st.markdown("*Ubah hasil transkripsi nada menjadi progresi akord*")

try:
    with open("ai_chord_progression.html", "r", encoding="utf-8") as f:
        html = f.read()
    st.components.v1.html(html, height=900, scrolling=True)
except FileNotFoundError:
    st.error("⚠️ File ai_chord_progression.html tidak ditemukan. Pastikan file ada di root.")