import tkinter as tk
from PIL import Image, ImageTk
import os
import webbrowser
import sys

# ============================================================
# KONFIGURASI PATH
# ============================================================

# Ambil direktori tempat file script ini berada
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path ke gambar splash
IMAGE_PATH = os.path.join(BASE_DIR, "assets", "images", "img1.jpg")

# Path ke file aplikasi utama (index.html)
HTML_PATH = os.path.join(BASE_DIR, "index.html")

# Ukuran jendela splash
SPLASH_WIDTH = 680
SPLASH_HEIGHT = 1000

# ============================================================
# FUNGSI MEMBUKA APLIKASI
# ============================================================

def open_app():
    """Menutup splash screen dan membuka index.html di browser"""
    splash.destroy()  # Tutup jendela splash

    # Cek apakah file index.html ada
    if os.path.exists(HTML_PATH):
        # Buka di browser default
        webbrowser.open("file://" + HTML_PATH)
    else:
        # Tampilkan pesan error jika file tidak ditemukan
        print(f"❌ Error: File '{HTML_PATH}' tidak ditemukan!")
        print("   Pastikan file index.html berada di folder yang sama dengan splash_screen.py")
        # Bisa juga menggunakan messagebox jika ingin tampilan lebih rapi:
        # from tkinter import messagebox
        # messagebox.showerror("Error", f"File index.html tidak ditemukan!\n{HTML_PATH}")

# ============================================================
# MEMBUAT SPLASH SCREEN
# ============================================================

# Buat jendela utama
splash = tk.Tk()
splash.title("PMD Musik 12 TET")
splash.overrideredirect(True)  # Hilangkan border/title bar
splash.attributes('-topmost', True)  # Selalu di atas jendela lain

# Atur ukuran dan posisi di tengah layar
screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()
x_pos = (screen_width // 2) - (SPLASH_WIDTH // 2)
y_pos = (screen_height // 2) - (SPLASH_HEIGHT // 2)
splash.geometry(f"{SPLASH_WIDTH}x{SPLASH_HEIGHT}+{x_pos}+{y_pos}")

# ============================================================
# MUAT GAMBAR
# ============================================================

try:
    # Buka dan resize gambar
    image = Image.open(IMAGE_PATH)
    resized_image = image.resize((SPLASH_WIDTH, SPLASH_HEIGHT), Image.LANCZOS)
    img_tk = ImageTk.PhotoImage(resized_image)

    # Tampilkan gambar sebagai background
    label_bg = tk.Label(splash, image=img_tk)
    label_bg.pack(fill="both", expand=True)
    label_bg.image = img_tk  # Simpan referensi agar tidak dihapus garbage collector

except FileNotFoundError:
    # Jika gambar tidak ditemukan, tampilkan teks sebagai gantinya
    print(f"⚠️  Gambar tidak ditemukan: {IMAGE_PATH}")
    label_bg = tk.Label(
        splash,
        text="🎵 PMD Musik 12 TET\n\nGambar tidak ditemukan",
        font=("Arial", 24, "bold"),
        fg="white",
        bg="#1a1a2e",
        justify="center"
    )
    label_bg.pack(fill="both", expand=True)

except Exception as e:
    # Error lain (misal file korup)
    print(f"❌ Gagal memuat gambar: {e}")
    label_bg = tk.Label(
        splash,
        text=f"❌ Gagal memuat gambar\n{str(e)}",
        font=("Arial", 18),
        fg="red",
        bg="#1a1a2e",
        justify="center"
    )
    label_bg.pack(fill="both", expand=True)

# ============================================================
# TOMBOL MULAI (DITEMPATKAN DI ATAS GAMBAR)
# ============================================================

# Buat tombol dengan gaya yang menarik
btn_start = tk.Button(
    splash,
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

# Tempatkan tombol di bagian bawah tengah (90% dari tinggi layar)
btn_start.place(relx=0.5, rely=0.92, anchor="center")

# Efek hover sederhana (opsional)
def on_enter(e):
    btn_start.config(bg="#c73652", transform="scale(1.05)")

def on_leave(e):
    btn_start.config(bg="#e94560", transform="scale(1.0)")

btn_start.bind("<Enter>", on_enter)
btn_start.bind("<Leave>", on_leave)

# ============================================================
# JALANKAN APLIKASI
# ============================================================

if __name__ == "__main__":
    print("🎵 PMD Musik 12 TET - Splash Screen")
    print(f"📂 Direktori: {BASE_DIR}")
    print(f"🖼️  Gambar: {IMAGE_PATH}")
    print(f"🌐 HTML: {HTML_PATH}")
    print("=" * 50)
    splash.mainloop()