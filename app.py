# app.py
import streamlit as st
import base64

# ============================================================
# KONFIGURASI HALAMAN
# ============================================================

st.set_page_config(
    page_title="Musik 12-TET (20 Nada per Oktaf)",
    page_icon="🎵",
    layout="wide"
)

# ============================================================
# JUDUL
# ============================================================

st.title("🎵 Musik 12-TET (20 Nada per Oktaf)")
st.markdown("""
*Eksplorasi Mikrotonal — Inovasi Sistem 20 Nada per Oktaf*
""")

st.markdown("---")

# ============================================================
# BACA FILE HTML
# ============================================================

def load_html():
    """Membaca file index.html"""
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        # Jika file tidak ditemukan, gunakan HTML minimal
        return create_minimal_html()

def create_minimal_html():
    """Membuat HTML minimal jika index.html tidak ditemukan"""
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Musik 12-TET</title>
        <style>
            body { 
                font-family: Arial; 
                background: #1a1a2e; 
                color: #eee; 
                text-align: center;
                padding: 50px;
            }
            .error {
                color: #e94560;
                font-size: 24px;
            }
        </style>
    </head>
    <body>
        <div class="error">⚠️ File index.html tidak ditemukan</div>
        <p>Pastikan file index.html berada di folder yang sama dengan app.py</p>
    </body>
    </html>
    """

# ============================================================
# TAMPILKAN APLIKASI
# ============================================================

# Baca HTML
html_content = load_html()

# Tampilkan dengan komponen HTML
st.components.v1.html(
    html_content,
    height=700,
    scrolling=True
)

# ============================================================
# SIDEBAR - INFORMASI
# ============================================================

with st.sidebar:
    st.header("📖 Informasi")
    
    st.markdown("""
    ### Sistem 12-TET (20 Nada per Oktaf)
    
    **Rumus Frekuensi:**
    ```
    f_n = f_0 × 3^(n/20)
    ```
    
    **Skala Mayor (E=1):**
    ```
    E - F - G - H - I - J - K - A - B - C - D - E
    ```
    
    **Skala Minor (A=1):**
    ```
    A - B - C - D - E - F - G - H - I - J - K - A
    ```
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ### 🎹 Keyboard
    - **Tuts Putih**: Nada Natural
    - **Tuts Hitam**: Nada Kromatik (#)
    - Klik tuts untuk mendengar nada
    """)
    
    st.markdown("---")
    
    # ===== TAMBAHAN: LINK KE HALAMAN AI =====
    st.markdown("### 🤖 Fitur AI")
    st.markdown("""
    - [🎵 AI Composer](/ai_composer)
    - [🎤 AI Transcriber](/ai_transcriber)
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ### 📚 Referensi
    1. Helmholtz, H. (1954). *On the Sensations of Tone*
    2. Sethares, W. A. (2005). *Tuning, Timbre, Spectrum, Scale*
    3. Tenney, J. (1988). *Meta-Hodos*
    """)
    
    st.markdown("---")
    
    st.caption("© 2026 Sukma Riadi Pakpahan, SST")

# ============================================================
# FOOTER
# ============================================================

st.markdown("---")
st.caption("Berdasarkan Karya Tulis Ilmiah: Eksplorasi Musik Sistem 12-TET (20 Nada per Oktaf)")