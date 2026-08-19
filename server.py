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