# musik-12tet-20nada

# 🎵 Musik 12-TET (20 Nada per Oktaf)

Aplikasi web interaktif untuk mengeksplorasi sistem musik mikrotonal **12-Tone Equal Temperament (12-TET)** dengan **20 nada per oktaf**.

![Screenshot](screenshot.png)

## 📖 Tentang Proyek

Aplikasi ini merupakan implementasi dari karya tulis ilmiah:

> **"Eksplorasi Musik Sistem 12-TET (20 Nada per Oktaf): Inovasi dan Peluang dalam Seni Musik Modern"**  
> Oleh: Sukma Riadi Pakpahan, SST  
> Diajukan kepada Badan Riset dan Inovasi Nasional (BRIN)

## 🎹 Fitur

- ✅ Keyboard interaktif 4 oktaf (C2 - D5)
- ✅ 20 nada per oktaf: A, A#, B, B#, C, C#, D, E, E#, F, F#, G, G#, H, H#, I, J, J#, K, K#
- ✅ Tuts hitam untuk nada kromatik (#)
- ✅ Tuts putih untuk nada natural
- ✅ Putar Skala Mayor (E=do)
- ✅ Putar Skala Minor (A=do)
- ✅ Tampilan frekuensi real-time
- ✅ Informasi teoritis lengkap

## 🎵 Sistem 12-TET (20 Nada per Oktaf)


Sttruktur folder seperti ini:

```
musik-12tet-20nada/
├── index.html
├── README.md
├── LICENSE
└── .gitignore
```

1. File index.html (sudah ada)

2. File README.md

```markdown
# 🎵 Musik 12-TET (20 Nada per Oktaf)

Aplikasi web interaktif untuk mengeksplorasi sistem musik mikrotonal **12-Tone Equal Temperament (12-TET)** dengan **20 nada per oktaf**.

![Screenshot](screenshot.png)

## 📖 Tentang Proyek

Aplikasi ini merupakan implementasi dari karya tulis ilmiah:

> **"Eksplorasi Musik Sistem 12-TET (20 Nada per Oktaf): Inovasi dan Peluang dalam Seni Musik Modern"**  
> Oleh: Sukma Riadi Pakpahan, SST  
> Diajukan kepada Badan Riset dan Inovasi Nasional (BRIN)

## 🎹 Fitur

- ✅ Keyboard interaktif 4 oktaf (C2 - D5)
- ✅ 20 nada per oktaf: A, A#, B, B#, C, C#, D, E, E#, F, F#, G, G#, H, H#, I, J, J#, K, K#
- ✅ Tuts hitam untuk nada kromatik (#)
- ✅ Tuts putih untuk nada natural
- ✅ Putar Skala Mayor (E=do)
- ✅ Putar Skala Minor (A=do)
- ✅ Tampilan frekuensi real-time
- ✅ Informasi teoritis lengkap

## 🎵 Sistem 12-TET (20 Nada per Oktaf)

### Rumus Frekuensi
```

f_n = f_0 × 3^(n/20)

```
dimana:
- f_0 = A#4 = 440 Hz (urutan ke-2)
- n = jumlah langkah semitone

### Skala Mayor Natural (E=1)
```

E - F - G - H - I - J - K - A - B - C - D - E
Interval: 1 1 1 1 ½ 1 1 1 1 1 ½

```

### Skala Minor Natural (A=1)
```

A - B - C - D - E - F - G - H - I - J - K - A
Interval: 1 1 1 ½ 1 1 1 1 ½ 1 1

```

## 🚀 Cara Menggunakan

### Online (Langsung)
Kunjungi: [https://username.github.io/musik-12tet-20nada/](https://username.github.io/musik-12tet-20nada/)

### Lokal
1. Clone repository:
```bash
git clone https://github.com/username/musik-12tet-20nada.git
cd musik-12tet-20nada
```

2. Buka index.html di browser, atau jalankan server:

```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

3. Buka browser di http://localhost:8000

🛠 Teknologi

· HTML5
· CSS3
· Vanilla JavaScript
· Web Audio API

📊 Frekuensi Nada (Oktaf 4)

Nada Frekuensi (Hz) Tuts
A4 416.49 ⬜ Putih
A#4 440.00 ⬛ Hitam
B4 464.86 ⬜ Putih
B#4 491.08 ⬛ Hitam
C4 518.80 ⬜ Putih
C#4 548.108 ⬛ Hitam
D4 579.084 ⬜ Putih
E5 611.776 ⬜ Putih
E#5 646.316 ⬛ Hitam
F5 682.792 ⬜ Putih
... ... ...

Lihat tabel lengkap di dalam aplikasi pada tab "Frekuensi"

📝 Referensi

1. Helmholtz, H. (1954). On the Sensations of Tone. Dover Publications.
2. Sethares, W. A. (2005). Tuning, Timbre, Spectrum, Scale. Springer.
3. Tenney, J. (1988). Meta-Hodos: A Phenomenology of Music. Frog Peak Music.

🤝 Kontribusi

Kontribusi sangat diterima! Silakan fork repository ini dan buat pull request.

📄 Lisensi

MIT License - lihat file LICENSE untuk detail.

```text
MIT License

Copyright (c) 2026 Sukma Riadi Pakpahan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

📝 Penjelasan Lisensi MIT

Apa itu Lisensi MIT?

Lisensi MIT adalah lisensi open source yang sangat permisif. Ini berarti:

✅ Boleh:

· Menggunakan kode secara komersial
· Memodifikasi kode
· Mendistribusikan kode
· Menggabungkan dengan proyek lain
· Menggunakan tanpa batasan

❌ Tidak Boleh:

· Menghapus pemberitahuan hak cipta
· Menuntuk penulis atas kerusakan yang disebabkan

Keuntungan Lisensi MIT:

1. Sederhana - Hanya beberapa paragraf
2. Populer - Digunakan oleh banyak proyek besar (React, Angular, jQuery)
3. Fleksibel - Dapat digunakan untuk proyek apapun
4. Aman - Melindungi penulis dari tuntutan hukum

---

📂 Cara Menambahkan LICENSE ke Repository

Cara 1: Melalui GitHub Website

1. Buka repository di GitHub
2. Klik Add file → Create new file
3. Nama file: LICENSE
4. Copy-paste kode di atas
5. Klik Commit new file

Cara 2: Melalui GitHub Template

1. Buka repository di GitHub
2. Klik Add file → Create new file
3. Nama file: LICENSE
4. Klik Choose a license template
5. Pilih MIT License
6. Isi tahun dan nama: 2026 Sukma Riadi Pakpahan
7. Klik Review and submit
8. Klik Commit new file

Cara 3: Melalui Terminal

```bash
# Buat file LICENSE
cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2026 Sukma Riadi Pakpahan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

# Commit dan push
git add LICENSE
git commit -m "Add MIT License"
git push
```

---

🔄 Lisensi Alternatif

Jika Anda ingin menggunakan lisensi lain, berikut beberapa pilihan:

1. GNU GPL v3 (Lebih Ketat)

· Kode harus tetap open source
· Perubahan harus dibagikan
· Cocok untuk proyek yang ingin tetap bebas

2. Apache 2.0 (Seperti MIT + Paten)

· Seperti MIT tapi dengan perlindungan paten
· Digunakan oleh Google, Apache, dll.

3. BSD 3-Clause (Mirip MIT)

· Sedikit lebih ketat dari MIT
· Digunakan oleh proyek BSD

4. Creative Commons (Untuk Non-Software)

· Untuk karya seni, dokumentasi, dll.
· CC BY, CC BY-SA, CC BY-NC, dll.

---

👨‍💻 Penulis

Sukma Riadi Pakpahan, SST

· Penulis Karya Tulis Ilmiah
· Pengembang Aplikasi

---

⭐ Beri bintang jika proyek ini bermanfaat!

```

### 3. **File `LICENSE`** (MIT License)

```text
MIT License

Copyright (c) 2026 Sukma Riadi Pakpahan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

4. File .gitignore

```text
# OS files
.DS_Store
Thumbs.db

# Editor files
.vscode/
.idea/
*.swp
*.swo

# Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Logs
*.log

# Temporary files
*.tmp
*.temp
```

---

📤 Upload ke GitHub

Cara 1: Menggunakan GitHub Website

1. Buat Repository Baru
   · Buka github.com
   · Klik tombol New atau + → New repository
   · Nama repository: musik-12tet-20nada
   · Deskripsi: Aplikasi web interaktif untuk sistem musik 12-TET 20 nada per oktaf
   · Pilih Public atau Private
   · Jangan centang "Initialize this repository with a README"
   · Klik Create repository
2. Upload File
   · Di halaman repository, klik Add file → Upload files
   · Drag and drop semua file (index.html, README.md, LICENSE, .gitignore)
   · Tambahkan pesan commit: Initial commit: Aplikasi Musik 12-TET 20 Nada
   · Klik Commit changes

Cara 2: Menggunakan Git di Terminal

```bash
# 1. Inisialisasi Git di folder proyek
cd musik-12tet-20nada
git init

# 2. Tambahkan semua file
git add .
git commit -m "Initial commit: Aplikasi Musik 12-TET 20 Nada"

# 3. Hubungkan dengan repository GitHub
git remote add origin https://github.com/username/musik-12tet-20nada.git

# 4. Push ke GitHub
git push -u origin main
# atau jika branch-nya master:
git push -u origin master
```

Cara 3: Menggunakan GitHub Desktop

1. Install GitHub Desktop
2. Buka aplikasi
3. Klik File → New repository
4. Isi nama: musik-12tet-20nada
5. Pilih folder lokal
6. Klik Create repository
7. Copy file ke folder tersebut
8. Klik Commit to main
9. Klik Publish repository

---

🌐 Deploy ke GitHub Pages

Setelah repository terupload, aktifkan GitHub Pages:

1. Buka repository di GitHub
2. Klik Settings
3. Scroll ke Pages (di menu sidebar kiri)
4. Di Branch, pilih main atau master
5. Folder: / (root)
6. Klik Save
7. Tunggu beberapa menit, lalu akses:
   ```
   https://username.github.io/musik-12tet-20nada/
   ```

---

📁 Struktur Final Repository

```
musik-12tet-20nada/
├── index.html      # Aplikasi utama
├── README.md       # Dokumentasi
├── LICENSE         # Lisensi MIT
└── .gitignore      # File yang diabaikan Git
```

---

🎯 Checklist

☑ Buat repository di GitHub
☑ Upload file index.html
☑ Upload README.md
☑ Upload LICENSE
☑ Upload .gitignore
☑ Aktifkan GitHub Pages
☑ Test URL: https://username.github.io/musik-12tet-20nada/

---

🔗 Link Berguna

· GitHub
· GitHub Pages
· Markdown Guide
· MIT License

---

Selesai! 🎉 Aplikasi ini sekarang sudah online di GitHub Pages.


Tambahan:

Untuk aplikasi web, tidak wajib menggunakan server.py. Namun, jika Anda ingin menambahkan server.py untuk kemudahan menjalankan aplikasi secara lokal, berikut penjelasan dan kode lengkapnya:

📁 Struktur Repository dengan Server

```
musik-12tet-20nada/
├── index.html          # Aplikasi utama
├── server.py           # Server Python untuk menjalankan lokal
├── README.md           # Dokumentasi
├── LICENSE             # Lisensi MIT
└── .gitignore          # File yang diabaikan Git
```

---

📄 File server.py

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Server HTTP sederhana untuk Aplikasi Musik 12-TET (20 Nada per Oktaf)
Gunakan untuk menjalankan aplikasi secara lokal di browser.
"""

import http.server
import socketserver
import webbrowser
import os
import sys
from pathlib import Path

# ============================================================
# KONFIGURASI
# ============================================================

PORT = 8000
HOST = "localhost"
INDEX_FILE = "index.html"

# ============================================================
# CLASS CUSTOM HANDLER
# ============================================================

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler dengan dukungan CORS dan logging"""
    
    def end_headers(self):
        """Tambahkan CORS headers untuk akses dari perangkat lain"""
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()
    
    def log_message(self, format, *args):
        """Custom logging dengan format yang lebih informatif"""
        print(f"[{self.address_string()}] {format % args}")


# ============================================================
# FUNGSI UTAMA
# ============================================================

def get_local_ip():
    """Mendapatkan IP lokal untuk akses dari perangkat lain di jaringan"""
    try:
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"


def check_index_file():
    """Memeriksa apakah index.html ada di direktori yang sama"""
    if not os.path.exists(INDEX_FILE):
        print(f"❌ Error: File '{INDEX_FILE}' tidak ditemukan!")
        print(f"   Pastikan file '{INDEX_FILE}' berada di folder yang sama dengan server.py")
        print(f"   Direktori saat ini: {os.getcwd()}")
        return False
    return True


def main():
    """Fungsi utama untuk menjalankan server"""
    
    # Cek file index.html
    if not check_index_file():
        sys.exit(1)
    
    # Tampilan banner
    print("=" * 60)
    print("🎵  Aplikasi Musik 12-TET (20 Nada per Oktaf)")
    print("=" * 60)
    print()
    
    # Dapatkan IP lokal
    local_ip = get_local_ip()
    
    # Dapatkan port dari argumen jika ada
    port = PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
            if port < 1 or port > 65535:
                print("⚠️  Port harus antara 1-65535, menggunakan port default 8000")
                port = PORT
        except ValueError:
            print(f"⚠️  '{sys.argv[1]}' bukan angka valid, menggunakan port default {PORT}")
            port = PORT
    
    # Coba jalankan server dengan port yang tersedia
    try:
        with socketserver.TCPServer((HOST, port), CustomHTTPRequestHandler) as httpd:
            print("✅ Server berhasil dijalankan!")
            print()
            print("📱  Akses aplikasi melalui:")
            print(f"   👉  http://{HOST}:{port}")
            print(f"   👉  http://127.0.0.1:{port}")
            if local_ip != "127.0.0.1":
                print(f"   👉  http://{local_ip}:{port}  (dari perangkat lain di jaringan)")
            print()
            print("📂  Direktori: " + os.getcwd())
            print("📄  File utama: " + INDEX_FILE)
            print()
            print("🔴  Tekan Ctrl+C untuk menghentikan server")
            print("=" * 60)
            print()
            
            # Buka browser otomatis (jika tidak di nonaktifkan)
            if "--no-browser" not in sys.argv:
                webbrowser.open(f"http://{HOST}:{port}")
            
            # Jalankan server
            httpd.serve_forever()
            
    except OSError as e:
        if e.errno == 98 or e.errno == 10048:  # Port already in use
            print(f"❌ Error: Port {port} sedang digunakan!")
            print(f"   Coba jalankan dengan port berbeda:")
            print(f"   python server.py 8001")
        else:
            print(f"❌ Error: {e}")
        sys.exit(1)
    except KeyboardInterrupt:
        print()
        print("=" * 60)
        print("⏹️  Server dihentikan.")
        print("👋  Terima kasih telah menggunakan aplikasi ini!")
        print("=" * 60)
        sys.exit(0)


# ============================================================
# EKSEKUSI
# ============================================================

if __name__ == "__main__":
    main()
```

---

📄 File README.md (Diperbarui dengan Server)

```markdown
# 🎵 Musik 12-TET (20 Nada per Oktaf)

Aplikasi web interaktif untuk mengeksplorasi sistem musik mikrotonal **12-Tone Equal Temperament (12-TET)** dengan **20 nada per oktaf**.

![Screenshot](screenshot.png)

## 📖 Tentang Proyek

Aplikasi ini merupakan implementasi dari karya tulis ilmiah:

> **"Eksplorasi Musik Sistem 12-TET (20 Nada per Oktaf): Inovasi dan Peluang dalam Seni Musik Modern"**  
> Oleh: Sukma Riadi Pakpahan, SST  
> Diajukan kepada Badan Riset dan Inovasi Nasional (BRIN)

## 🎹 Fitur

- ✅ Keyboard interaktif 4 oktaf (C2 - D5)
- ✅ 20 nada per oktaf: A, A#, B, B#, C, C#, D, E, E#, F, F#, G, G#, H, H#, I, J, J#, K, K#
- ✅ Tuts hitam untuk nada kromatik (#)
- ✅ Tuts putih untuk nada natural
- ✅ Putar Skala Mayor (E=do)
- ✅ Putar Skala Minor (A=do)
- ✅ Tampilan frekuensi real-time
- ✅ Informasi teoritis lengkap

## 🚀 Cara Menggunakan

### Online (GitHub Pages)
Kunjungi: [https://username.github.io/musik-12tet-20nada/](https://username.github.io/musik-12tet-20nada/)

### Lokal dengan Server Python (Direkomendasikan)

1. Clone repository:
```bash
git clone https://github.com/username/musik-12tet-20nada.git
cd musik-12tet-20nada
```

2. Jalankan server:

```bash
python server.py
```

3. Buka browser di http://localhost:8000

Opsi tambahan:

```bash
# Menggunakan port berbeda
python server.py 8080

# Tanpa membuka browser otomatis
python server.py --no-browser
```

Lokal (Tanpa Server)

Buka file index.html langsung di browser.

🛠 Teknologi

· HTML5
· CSS3
· Vanilla JavaScript
· Web Audio API
· Python (server lokal)

📊 Frekuensi Nada (Oktaf 4)

Nada Frekuensi (Hz) Tuts
A4 416.49 ⬜ Putih
A#4 440.00 ⬛ Hitam
B4 464.86 ⬜ Putih
B#4 491.08 ⬛ Hitam
C4 518.80 ⬜ Putih
C#4 548.108 ⬛ Hitam
D4 579.084 ⬜ Putih
E5 611.776 ⬜ Putih
E#5 646.316 ⬛ Hitam
F5 682.792 ⬜ Putih
... ... ...

Lihat tabel lengkap di dalam aplikasi pada tab "Frekuensi"

📝 Referensi

1. Helmholtz, H. (1954). On the Sensations of Tone. Dover Publications.
2. Sethares, W. A. (2005). Tuning, Timbre, Spectrum, Scale. Springer.
3. Tenney, J. (1988). Meta-Hodos: A Phenomenology of Music. Frog Peak Music.

🤝 Kontribusi

Kontribusi sangat diterima! Silakan fork repository ini dan buat pull request.

📄 Lisensi

MIT License - lihat file LICENSE untuk detail.

👨‍💻 Penulis

Sukma Riadi Pakpahan, SST

· Penulis Karya Tulis Ilmiah
· Pengembang Aplikasi

---

⭐ Beri bintang jika proyek ini bermanfaat!

```

---

## 🔧 Cara Menggunakan Server

### 1. Jalankan Server
```bash
python server.py
```

2. Output yang Diharapkan

```
============================================================
🎵  Aplikasi Musik 12-TET (20 Nada per Oktaf)
============================================================

✅ Server berhasil dijalankan!

📱  Akses aplikasi melalui:
   👉  http://localhost:8000
   👉  http://127.0.0.1:8000
   👉  http://192.168.1.100:8000  (dari perangkat lain di jaringan)

📂  Direktori: /path/to/musik-12tet-20nada
📄  File utama: index.html

🔴  Tekan Ctrl+C untuk menghentikan server
============================================================
```

3. Akses dari Perangkat Lain

Jika di jaringan yang sama, Anda bisa akses dari HP atau tablet:

```
http://192.168.1.100:8000
```

---

📂 File .gitignore (Diperbarui)

```text
# OS files
.DS_Store
Thumbs.db
*.swp
*.swo

# Editor files
.vscode/
.idea/
*.code-workspace

# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.pytest_cache/
.coverage
htmlcov/

# Virtual Environment
venv/
env/
.venv/

# Logs
*.log
server.log

# Temporary files
*.tmp
*.temp
*.bak

# IDE
.vscode/
.idea/

# Screenshots (opsional)
screenshot.png
*.png
*.jpg
```

---

🤔 Kenapa Pakai Server?

Keuntungan Tanpa Server Dengan Server
Akses dari HP/tablet ❌ Tidak ✅ Bisa
Web Audio API ⚠️ Terbatas ✅ Penuh
CORS ❌ ✅
Testing ❌ ✅
Profesional ❌ ✅

---

📤 Upload ke GitHub

```bash
# 1. Tambahkan file baru
git add server.py README.md .gitignore

# 2. Commit
git commit -m "Add server.py untuk menjalankan aplikasi secara lokal"

# 3. Push
git push
```

---

Selesai! Sekarang repository ini memiliki server Python untuk menjalankan aplikasi secara lokal. 🎉