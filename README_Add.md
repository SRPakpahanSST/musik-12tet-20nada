```markdown
# 🎵 PMD Musik 12 TET

**Pedang Mata Dua Musik Digital — Eksplorasi Mikrotonal 20 Nada per Oktaf**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Built with love](https://img.shields.io/badge/built%20with-%E2%9D%A4-red)](https://github.com/srpakpahansst/musik-12tet-20nada)

> Berdasarkan karya tulis ilmiah: **Eksplorasi Musik Sistem 12-TET (20 Nada per Oktaf): Inovasi dan Peluang dalam Seni Musik Modern** — Sukma Riadi Pakpahan, SST

---

## 📖 Tentang Proyek

**PMD Musik 12 TET** adalah aplikasi web interaktif yang mengimplementasikan sistem musik **12-Tone Equal Temperament (12-TET) dengan 20 nada per oktaf**. Sistem ini merupakan inovasi dalam dunia musik mikrotonal, memperluas skala konvensional 12 nada per oktaf menjadi 20 nada dengan rasio frekuensi **3^(1/20)** dan faktor oktaf **×3**, dengan **A4 = 440 Hz** sebagai acuan (ditempatkan pada posisi ke‑2 dalam oktaf).

Aplikasi ini menyediakan:

- 🎹 **Keyboard digital** interaktif dengan 3/4/5 oktaf (20 nada per oktaf)
- 🎶 **Mode Akord** dengan sustain (C2–B#3), putih = Mayor, hitam = Minor
- 🎵 **AI Composer** (generasi melodi berbasis deskripsi atau prompt OpenAI)
- 🎤 **AI Transcriber** (rekam audio dari mikrofon, deteksi pitch, transkripsi ke notasi 20‑TET)
- 🎼 **Chord Progression Generator** (analisis progresi akord dari hasil transkripsi)
- 🎛️ **Efek audio** (Reverb, Delay, Amplifier) dan 8 pilihan instrumen

---

## 🚀 Fitur Utama

### 🎹 Keyboard
- Tampilan piano virtual dengan tuts putih dan hitam (20 nada per oktaf)
- Pilihan oktaf: 3, 4, atau 5
- Dua mode:
  - **Nada Tunggal**: mainkan nada tunggal, secara otomatis merekam melodi untuk diputar ulang
  - **Akord**: tekan tuts di rentang C2–B#3 (20 nada) untuk membunyikan akord triad (Mayor untuk tuts putih, Minor untuk tuts hitam) dengan sustain, selalu menggunakan suara piano
- Tombol **Mayor** dan **Minor** memutar ulang melodi yang telah direkam (bukan tangga nada)

### 🎵 AI Composer
- Dua mode input:
  - **Deskripsi**: tulis deskripsi melodi (misal: *“melodi yang perlahan meningkat, romantis”*) → sistem menghasilkan melodi simulasi
  - **Prompt AI**: masukkan OpenAI API Key dan prompt spesifik → AI GPT‑3.5 menghasilkan notasi nada
- Kontrol mood (6 pilihan), skala (Mayor/Minor), dan tempo
- Tombol **Generate**, **Play**, **Stop**, **Clear**

### 🎤 AI Transcriber
- **Rekam audio** dari mikrofon (maks. 22 menit) dengan visualisasi waveform
- Dua algoritma deteksi pitch:
  - **Standar** (Autokorelasi)
  - **Improved (YIN)** dengan interpolasi parabolik, normalisasi, median filter, dan high‑pass filter opsional
- Mode frekuensi: Vokal, Instrumental, Full Range
- Sensitivitas (ambang deteksi) dapat diatur
- Hasil transkripsi ditampilkan sebagai urutan nada (20 nada per oktaf) dan dapat diputar ulang

### 🎶 Chord Progression Generator
- Masukkan hasil transkripsi (misal: `E3 → G3 → H3 → ...`)
- Sistem menentukan nada dasar dan skala (Mayor/Minor) secara otomatis atau manual
- Menampilkan progresi akord dengan notasi Romawi (I, ii, iii, IV, V, vi, vii°)
- Menggunakan interval terts (mayor=4, minor=3) dan kwint (7) dalam sistem 20‑TET

### 🎛️ Kontrol Audio
- 8 instrumen: Sine, Square, Sawtooth, Triangle, Organ, Piano, Flute, Trumpet
- Reverb (0‑100%)
- Delay (0‑100%)
- Amplifier (0.5× – 3.0×)

---

## 📂 Struktur Proyek

```

/
├── index.html          # Aplikasi utama (single‑file HTML/CSS/JavaScript)
├── README.md           # Dokumentasi proyek (file ini)
├── splash.png          # Gambar splash screen (opsional)
└── LICENSE             # Lisensi MIT (opsional)

```

---

## 🔧 Instalasi & Menjalankan

Aplikasi ini adalah **single‑file HTML** yang dapat dijalankan langsung di browser tanpa server web.

1. **Clone repositori** (atau unduh file `index.html`):
   ```bash
   git clone https://github.com/srpakpahansst/musik-12tet-20nada.git
   cd musik-12tet-20nada
```

2. Buka index.html di browser favorit Anda (disarankan Chrome, Firefox, atau Edge).
3. Izinkan akses mikrofon saat menggunakan fitur AI Transcriber.

⚠️ Untuk pengalaman terbaik, gunakan browser modern dengan dukungan Web Audio API dan MediaRecorder.

---

🧠 Teori Singkat

Sistem 12‑TET dengan 20 Nada per Oktaf

· Rumus frekuensi:
    f_n = f_0 × 3^(n/20), dengan n = jumlah langkah dari nada referensi
· Nada referensi: A4 = 440 Hz (berada di urutan ke‑2 dalam oktaf)
· Oktaf berikutnya: dikalikan dengan faktor 3 (bukan 2)
· Simbol nada (dalam satu oktaf):
    E, E#, F, F#, G, G#, H, H#, I, J, J#, K, K#, A, A#, B, B#, C, C#, D
· Skala Mayor natural (E = 1/do):
    E – F – G – H – I – J – K – A – B – C – D – E
    Interval: 1 1 1 1 ½ 1 1 1 1 1 ½
· Skala Minor natural (A = 1/do):
    A – B – C – D – E – F – G – H – I – J – K – A
    Interval: 1 1 1 ½ 1 1 1 1 ½ 1 1

Akord (Triad)

· Mayor: root + 4 langkah (terts mayor) + 7 langkah (kwint)
· Minor: root + 3 langkah (terts minor) + 7 langkah (kwint)
· Rentang akord yang didukung: C2–B#3 (20 nada)

---

🎮 Cara Penggunaan

Tab Keyboard

· Pilih Nada Tunggal atau Akord.
· Klik tuts untuk memainkan nada/akord.
· Pada mode Tunggal, setiap tuts yang ditekan akan direkam ke dalam melodi.
· Gunakan tombol Mayor atau Minor untuk memutar ulang melodi rekaman.
· Atur instrumen, reverb, delay, dan amplifier sesuai keinginan.

Tab AI Composer

· Pilih mode Deskripsi atau Prompt AI.
· Masukkan teks, pilih mood, skala, tempo.
· Klik Generate → sistem menghasilkan melodi.
· Klik Play untuk mendengar, Stop untuk menghentikan, Clear untuk menghapus.

Tab AI Transcriber

· Klik tombol mikrofon 🎤 untuk mulai merekam.
· Pilih algoritma (Standar / Improved YIN), mode, dan sensitivitas.
· Setelah rekaman berhenti (manual atau otomatis 22 menit), klik AI Transcribe.
· Hasil transkripsi akan muncul; klik Play Hasil untuk mendengarkan.

Tab Chord Progression

· Salin hasil transkripsi dari tab Transcriber ke kotak input.
· Pilih mode analisis (Otomatis, Mayor, Minor) dan jumlah akord.
· Klik Generate Progresi → tampilkan progresi akord.

---

🌐 Demo & Deployment

Aplikasi ini dapat di‑deploy ke berbagai platform statis:

· Streamlit Cloud (dengan mengubah ke app.py jika diperlukan)
· GitHub Pages
· Netlify / Vercel
· Apache / Nginx (sebagai file statis)

---

🤝 Kontribusi

Kontribusi sangat diterima! Silakan buka issue atau pull request untuk:

· Perbaikan bug
· Penambahan fitur (misal: instrumen baru, efek audio, visualisasi)
· Peningkatan algoritma deteksi pitch
· Dokumentasi

---

📜 Lisensi

Distributed under the MIT License. Lihat file LICENSE untuk informasi lebih lanjut.

---

👨‍💻 Penulis

Sukma Riadi Pakpahan, SST

· Karya Tulis Ilmiah: Eksplorasi Musik Sistem 12-TET (20 Nada per Oktaf): Inovasi dan Peluang dalam Seni Musik Modern
· GitHub: @srpakpahansst

---

🙏 Ucapan Terima Kasih

· Badan Riset dan Inovasi Nasional (BRIN)
· Komunitas musik mikrotonal dan pengembang open‑source
· Semua pihak yang mendukung pengembangan sistem musik inovatif ini

---

„Dari keisengan timbul suatu kebrilianan.“ — Sukma Riadi Pakpahan

```