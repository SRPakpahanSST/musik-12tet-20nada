import tkinter as tk
from tkinter import messagebox
import os
import webbrowser
import sys

# ============================================================
# KONFIGURASI PATH (GAMBAR DI ROOT)
# ============================================================

# Ambil direktori tempat file ini berada
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path gambar splash (di root)
IMAGE_SPLASH = os.path.join(BASE_DIR, "img1.jpg")   # untuk splash screen
IMAGE_APP = os.path.join(BASE_DIR, "img2.jpg")      # untuk halaman utama (opsional)

# Path file index.html (aplikasi utama)
HTML_PATH = os.path.join(BASE_DIR, "index.html")

# Ukuran jendela splash
SPLASH_WIDTH = 680
SPLASH_HEIGHT = 1000

print("=" * 50)
print("🎵 PMD Musik 12 TET - Splash Screen")
print(f"📂 BASE_DIR: {BASE_DIR}")
print(f"🖼️  IMAGE_SPLASH: {IMAGE_SPLASH}")
print(f"🌐 HTML_PATH: {HTML_PATH}")
print("=" * 50)

# ============================================================
# FUNGSI CEK FILE
# ============================================================

def file_exists(path):
    return os.path.exists(path)

# ============================================================
# FUNGSI MEMBUKA APLIKASI
# ============================================================

def open_app():
    """Menutup splash dan membuka index.html di browser"""
    splash.destroy()
    if file_exists(HTML_PATH):
        webbrowser.open("file://" + HTML_PATH)
    else:
        messagebox.showerror(
            "File Tidak Ditemukan",
            f"File index.html tidak ditemukan!\n\nPastikan file index.html berada di:\n{HTML_PATH}"
        )
        print(f"❌ Error: '{HTML_PATH}' tidak ditemukan!")

# ============================================================
# FUNGSI MEMUAT GAMBAR (DENGAN FALLBACK)
# ============================================================

def load_image(path, width, height):
    try:
        from PIL import Image, ImageTk
        if file_exists(path):
            img = Image.open(path)
            img = img.resize((width, height), Image.LANCZOS)
            return ImageTk.PhotoImage(img)
        else:
            print(f"⚠️  Gambar tidak ditemukan: {path}")
            return None
    except ImportError:
        print("⚠️  Pustaka Pillow tidak terinstall. Gunakan 'pip install Pillow'")
        return None
    except Exception as e:
        print(f"⚠️  Gagal memuat gambar: {e}")
        return None

# ============================================================
# MEMBUAT SPLASH SCREEN
# ============================================================

splash = None

def create_splash():
    global splash
    splash = tk.Tk()
    splash.title("PMD Musik 12 TET")
    splash.overrideredirect(True)          # tanpa border
    splash.attributes('-topmost', True)    # selalu di atas

    # Posisi tengah layar
    sw = splash.winfo_screenwidth()
    sh = splash.winfo_screenheight()
    x = (sw - SPLASH_WIDTH) // 2
    y = (sh - SPLASH_HEIGHT) // 2
    splash.geometry(f"{SPLASH_WIDTH}x{SPLASH_HEIGHT}+{x}+{y}")

    # --- Muat gambar splash ---
    img = load_image(IMAGE_SPLASH, SPLASH_WIDTH, SPLASH_HEIGHT)

    if img:
        # Tampilkan gambar sebagai background
        label = tk.Label(splash, image=img)
        label.pack(fill="both", expand=True)
        label.image = img  # simpan referensi
    else:
        # Fallback: canvas dengan teks
        canvas = tk.Canvas(splash, width=SPLASH_WIDTH, height=SPLASH_HEIGHT,
                           bg="#1a1a2e", highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        canvas.create_text(SPLASH_WIDTH//2, SPLASH_HEIGHT//2 - 60,
                           text="🎵 PMD Musik 12 TET",
                           font=("Arial", 36, "bold"), fill="#f5a623")
        canvas.create_text(SPLASH_WIDTH//2, SPLASH_HEIGHT//2 + 20,
                           text="Pedang Mata Dua Musik Digital\nMikrotonal 20 Nada per Oktaf",
                           font=("Arial", 18), fill="#cccccc", justify="center")
        canvas.create_text(SPLASH_WIDTH//2, SPLASH_HEIGHT//2 + 130,
                           text="(Gambar tidak ditemukan, mode teks)",
                           font=("Arial", 12), fill="#666666")

    # --- Tombol Mulai ---
    btn = tk.Button(
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
        bd=0
    )
    btn.place(relx=0.5, rely=0.92, anchor="center")

    # Efek hover
    def on_enter(e):
        btn.config(bg="#c73652")
    def on_leave(e):
        btn.config(bg="#e94560")
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    # --- Tombol keluar (opsional) ---
    btn_exit = tk.Button(
        splash,
        text="✕",
        font=("Arial", 14),
        bg="transparent",
        fg="#888",
        relief="flat",
        cursor="hand2",
        command=lambda: splash.destroy(),
        bd=0
    )
    btn_exit.place(x=SPLASH_WIDTH - 40, y=10)

    splash.mainloop()

# ============================================================
# EKSEKUSI
# ============================================================

if __name__ == "__main__":
    try:
        create_splash()
    except Exception as e:
        print(f"❌ ERROR FATAL: {e}")
        import traceback
        traceback.print_exc()
        # Tampilkan pesan error dengan tkinter jika memungkinkan
        try:
            root_err = tk.Tk()
            root_err.withdraw()
            messagebox.showerror(
                "Error Fatal",
                f"Terjadi error:\n\n{str(e)}\n\nPastikan semua file dan dependensi terinstall."
            )
            root_err.destroy()
        except:
            pass
        sys.exit(1)