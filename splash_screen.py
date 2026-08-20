import tkinter as tk
from tkinter import messagebox
import os
import sys
import webbrowser

# ============================================================
# KONFIGURASI
# ============================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "img1.jpg")
HTML_PATH = os.path.join(BASE_DIR, "index.html")

WIDTH = 680
HEIGHT = 1000

print("=" * 50)
print("🎵 SPLASH SCREEN DEBUG")
print(f"BASE_DIR  : {BASE_DIR}")
print(f"IMAGE_PATH: {IMAGE_PATH}")
print(f"HTML_PATH : {HTML_PATH}")
print(f"FILE img1.jpg exists? {os.path.exists(IMAGE_PATH)}")
print(f"FILE index.html exists? {os.path.exists(HTML_PATH)}")
print("=" * 50)

# ============================================================
# FUNGSI BUKA APLIKASI
# ============================================================

def open_app():
    """Tutup splash dan buka index.html di browser"""
    root.destroy()
    if os.path.exists(HTML_PATH):
        webbrowser.open("file://" + HTML_PATH)
    else:
        messagebox.showerror(
            "File Tidak Ditemukan",
            f"File index.html tidak ditemukan!\n\n{HTML_PATH}"
        )

# ============================================================
# BUAT WINDOW SPLASH
# ============================================================

root = tk.Tk()
root.title("PMD Musik 12 TET")
root.overrideredirect(True)          # hilangkan border
root.attributes('-topmost', True)    # selalu di atas

# Ukuran dan posisi tengah
sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()
x = (sw - WIDTH) // 2
y = (sh - HEIGHT) // 2
root.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

# Background default (jika gambar gagal)
root.config(bg="#1a1a2e")

# ============================================================
# MUAT GAMBAR (TANPA PILLOW)
# ============================================================

img = None
if os.path.exists(IMAGE_PATH):
    try:
        # PhotoImage hanya support GIF, PGM, PPM, PNG (tergantung versi Tk)
        # Untuk JPG, butuh Pillow. Kita coba dulu.
        img = tk.PhotoImage(file=IMAGE_PATH)
        print("✅ Gambar berhasil dimuat dengan PhotoImage")
    except Exception as e:
        print(f"⚠️ Gagal memuat gambar dengan PhotoImage: {e}")
        img = None
else:
    print("⚠️ File img1.jpg tidak ditemukan, gunakan mode teks")

# ============================================================
# TAMPILAN
# ============================================================

if img:
    # Jika gambar berhasil dimuat
    label = tk.Label(root, image=img, bg="#1a1a2e")
    label.pack(fill="both", expand=True)
    label.image = img  # simpan referensi
else:
    # Mode teks (fallback)
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT,
                       bg="#1a1a2e", highlightthickness=0)
    canvas.pack(fill="both", expand=True)

    canvas.create_text(WIDTH//2, HEIGHT//2 - 60,
                       text="🎵 PMD Musik 12 TET",
                       font=("Arial", 36, "bold"), fill="#f5a623")

    canvas.create_text(WIDTH//2, HEIGHT//2 + 20,
                       text="Pedang Mata Dua Musik Digital\nMikrotonal 20 Nada per Oktaf",
                       font=("Arial", 18), fill="#cccccc", justify="center")

    if os.path.exists(IMAGE_PATH):
        canvas.create_text(WIDTH//2, HEIGHT//2 + 130,
                           text="(Gambar tidak bisa ditampilkan, mode teks)",
                           font=("Arial", 12), fill="#666666")
    else:
        canvas.create_text(WIDTH//2, HEIGHT//2 + 130,
                           text="(img1.jpg tidak ditemukan, mode teks)",
                           font=("Arial", 12), fill="#666666")

# ============================================================
# TOMBOL MULAI
# ============================================================

btn = tk.Button(
    root,
    text="🚀 Mulai",
    font=("Arial", 20, "bold"),
    bg="#e94560",
    fg="white",
    relief="flat",
    padx=40,
    pady=12,
    cursor="hand2",
    command=open_app,
    activebackground="#c73652",
    activeforeground="white",
    bd=0,
    highlightthickness=0
)
btn.place(relx=0.5, rely=0.92, anchor="center")

# Efek hover
def on_enter(e):
    btn.config(bg="#c73652")
def on_leave(e):
    btn.config(bg="#e94560")
btn.bind("<Enter>", on_enter)
btn.bind("<Leave>", on_leave)

# ============================================================
# TOMBOL KELUAR (opsional)
# ============================================================

exit_btn = tk.Button(
    root,
    text="✕",
    font=("Arial", 14),
    bg="transparent",
    fg="#888",
    relief="flat",
    cursor="hand2",
    command=root.destroy,
    bd=0,
    highlightthickness=0
)
exit_btn.place(x=WIDTH - 40, y=10)

# ============================================================
# JALANKAN
# ============================================================

print("✅ Splash screen siap ditampilkan. Menjalankan mainloop...")
root.mainloop()
print("🔄 Splash screen ditutup.")