import tkinter as tk
from tkinter import messagebox
import os
import sys
import webbrowser
from PIL import Image, ImageTk   # <-- butuh Pillow

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_PATH = os.path.join(BASE_DIR, "img1.jpg")
HTML_PATH = os.path.join(BASE_DIR, "index.html")
WIDTH, HEIGHT = 680, 1000

def open_app():
    root.destroy()
    if os.path.exists(HTML_PATH):
        webbrowser.open("file://" + HTML_PATH)
    else:
        messagebox.showerror("Error", f"index.html tidak ditemukan di {HTML_PATH}")

root = tk.Tk()
root.overrideredirect(True)
root.attributes('-topmost', True)
sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry(f"{WIDTH}x{HEIGHT}+{(sw-WIDTH)//2}+{(sh-HEIGHT)//2}")

img = None
if os.path.exists(IMAGE_PATH):
    try:
        pil_img = Image.open(IMAGE_PATH)
        pil_img = pil_img.resize((WIDTH, HEIGHT), Image.LANCZOS)
        img = ImageTk.PhotoImage(pil_img)
        print("✅ Gambar dimuat dengan Pillow")
    except Exception as e:
        print(f"❌ Gagal muat gambar: {e}")

if img:
    label = tk.Label(root, image=img)
    label.pack(fill="both", expand=True)
    label.image = img
else:
    # fallback teks
    canvas = tk.Canvas(root, bg="#1a1a2e", highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    canvas.create_text(WIDTH//2, HEIGHT//2 - 60, text="🎵 PMD Musik 12 TET",
                       font=("Arial", 36, "bold"), fill="#f5a623")
    canvas.create_text(WIDTH//2, HEIGHT//2 + 20, text="Pedang Mata Dua Musik Digital\nMikrotonal 20 Nada per Oktaf",
                       font=("Arial", 18), fill="#cccccc", justify="center")
    canvas.create_text(WIDTH//2, HEIGHT//2 + 130, text="(Gambar tidak ditemukan atau gagal dimuat)",
                       font=("Arial", 12), fill="#666666")

btn = tk.Button(root, text="🚀 Mulai", font=("Arial", 20, "bold"),
                bg="#e94560", fg="white", relief="flat", padx=40, pady=12,
                cursor="hand2", command=open_app, activebackground="#c73652",
                activeforeground="white", bd=0)
btn.place(relx=0.5, rely=0.92, anchor="center")

root.mainloop()