# app.py
import streamlit as st

st.set_page_config(
    page_title="PMD Musik 12 TET",
    page_icon="🎵",
    layout="wide"
)

st.title("🎵 PMD Musik 12 TET")
st.markdown("*Eksplorasi Mikrotonal — Inovasi Sistem 20 Nada per Oktaf*")

st.markdown("---")

st.markdown("""
### Pilih Fitur

| Fitur | Deskripsi |
|-------|-----------|
| [🎹 Keyboard Digital](keyboard.html) | Mainkan 20 nada per oktaf dengan 8 instrumen |
| [🎵 AI Composer](ai_composer.html) | Ciptakan melodi dengan AI |
| [🎤 AI Transcriber](ai_transcriber.html) | Rekam & transkripsi nada |
| [🎶 Chord Progression](ai_chord_progression.html) | Ubah melodi menjadi akord |
""")

st.markdown("---")
st.caption("Berdasarkan Karya Tulis Ilmiah: Eksplorasi Musik Sistem 12-TET (20 Nada per Oktaf) — Sukma Riadi Pakpahan, SST")