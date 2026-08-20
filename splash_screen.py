import tkinter as tk
from tkinter import messagebox
import os
import sys
import webbrowser

# ============================================================
# KONFIGURASI PATH (AMAN UNTUK SEGALA LINGKUNGAN)
# ============================================================

# Ambil direktori tempat file script ini berada
try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
except NameError:
    # Jika __file__ tidak tersedia (misal di interactive shell)
    BASE_DIR = os.getcwd()

# Path ke gambar splash
IMAGE_PATH = os.path.join(BASE_DIR, "assets", "images", "img1.jpg")

# Path ke file aplikasi utama (index.html)
HTML_PATH = os.path.join(BASE_DIR, "index.html")

# Ukuran jendela splash
SPLASH_WIDTH = 680
SPLASH_HEIGHT = 1000

print("=" * 50)
print("🎵 PMD Musik 12 TET - Splash Screen")
print(f"📂 BASE_DIR: {BASE_DIR}")
print(f"🖼️  IMAGE_PATH: {IMAGE_PATH}")
print(f"🌐 HTML_PATH: {HTML_PATH}")
print("=" * 50)

# ============================================================
# FUNGSI CEK FILE
# ============================================================

def check_file(path, name):
    if os.path.exists(path):
        print(f"✅ {name} ditemukan: {path}")
        return True
    else:
        print(f"❌ {name} TIDAK ditemukan: {path}")
        return False

# ============================================================
# FUNGSI MEMBUKA APLIKASI
# ============================================================

def open_app():
    """Menutup splash screen dan membuka index.html di browser"""
    splash.destroy()  # Tutup jendela splash

    # Cek apakah file index.html ada
    if os.path.exists(HTML_PATH):
        # Buka di browser default
        print(f"🌐 Membuka: {HTML_PATH}")
        webbrowser.open("file://" + HTML_PATH)
    else:
        # Tampilkan pesan error jika file tidak ditemukan
        messagebox.showerror(
            "File Tidak Ditemukan",
            f"File index.html tidak ditemukan!\n\nPastikan file index.html berada di:\n{HTML_PATH}"
        )
        print(f"❌ Error: File '{HTML_PATH}' tidak ditemukan!")

# ============================================================
# FUNGSI MEMUAT GAMBAR
# ============================================================

def load_splash_image():
    """Mencoba memuat gambar, jika gagal return None"""
    try:
        from PIL import Image, ImageTk
        if os.path.exists(IMAGE_PATH):
            image = Image.open(IMAGE_PATH)
            resized_image = image.resize((SPLASH_WIDTH, SPLASH_HEIGHT), Image.LANCZOS)
            return ImageTk.PhotoImage(resized_image)
        else:
            print(f"⚠️  File gambar tidak ditemukan: {IMAGE_PATH}")
            return None
    except ImportError:
        print("⚠️  Pustaka PIL (Pillow) tidak terinstall. Gunakan 'pip install Pillow'")
        return None
    except Exception as e:
        print(f"⚠️  Gagal memuat gambar: {e}")
        return None

# ============================================================
# MEMBUAT SPLASH SCREEN
# ============================================================

splash = None  # Global agar bisa diakses di fungsi

def create_splash():
    global splash
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

    # === BACKGROUND ===
    img_tk = load_splash_image()

    if img_tk:
        # Jika gambar berhasil dimuat
        label_bg = tk.Label(splash, image=img_tk)
        label_bg.pack(fill="both", expand=True)
        label_bg.image = img_tk  # Simpan referensi
    else:
        # Jika gambar gagal dimuat, buat background berwarna dengan teks
        canvas = tk.Canvas(
            splash,
            width=SPLASH_WIDTH,
            height=SPLASH_HEIGHT,
            bg="#1a1a2e",
            highlightthickness=0
        )
        canvas.pack(fill="both", expand=True)

        # Teks judul
        canvas.create_text(
            SPLASH_WIDTH // 2,
            SPLASH_HEIGHT // 2 - 50,
            text="🎵 PMD Musik 12 TET",
            font=("Arial", 36, "bold"),
            fill="#f5a623",
            anchor="center"
        )
        canvas.create_text(
            SPLASH_WIDTH // 2,
            SPLASH_HEIGHT // 2 + 30,
            text="Pedang Mata Dua Musik Digital\nMikrotonal 20 Nada per Oktaf",
            font=("Arial", 18),
            fill="#cccccc",
            anchor="center",
            justify="center"
        )
        canvas.create_text(
            SPLASH_WIDTH // 2,
            SPLASH_HEIGHT // 2 + 120,
            text="(Gambar tidak ditemukan, menggunakan mode teks)",
            font=("Arial", 12),
            fill="#666666",
            anchor="center"
        )
        label_bg = canvas  # Untuk referensi

    # === TOMBOL MULAI ===
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

    # Tempatkan tombol di bagian bawah (92% dari tinggi)
    btn_start.place(relx=0.5, rely=0.92, anchor="center")

    # Efek hover sederhana
    def on_enter(e):
        btn_start.config(bg="#c73652")

    def on_leave(e):
        btn_start.config(bg="#e94560")

    btn_start.bind("<Enter>", on_enter)
    btn_start.bind("<Leave>", on_leave)

    # === TOMBOL KELUAR (Opsional) ===
    # Tombol kecil di pojok kanan atas untuk keluar
    btn_exit = tk.Button(
        splash,
        text="✕",
        font=("Arial", 14),
        bg="transparent",
        fg="#888",
        relief="flat",
        cursor="hand2",
        command=lambda: splash.destroy(),
        bd=0,
        highlightthickness=0
    )
    btn_exit.place(x=SPLASH_WIDTH - 40, y=10)

    # === MENJALANKAN ===
    splash.mainloop()

# ============================================================
# EKSEKUSI DENGAN HANDLING ERROR GLOBAL
# ============================================================

if __name__ == "__main__":
    try:
        create_splash()
    except Exception as e:
        # Jika terjadi error fatal, tampilkan di console dan messagebox
        print(f"❌ ERROR FATAL: {e}")
        import traceback
        traceback.print_exc()
        try:
            root_err = tk.Tk()
            root_err.withdraw()  # Sembunyikan jendela utama
            messagebox.showerror(
                "Error Fatal",
                f"Terjadi error saat menjalankan splash screen:\n\n{str(e)}\n\n"
                "Pastikan semua file dan dependensi terinstall dengan benar."
            )
            root_err.destroy()
        except:
            pass
        sys.exit(1)