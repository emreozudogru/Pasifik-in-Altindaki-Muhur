#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pasifik’in Altındaki Mühür - Sesli Kitap Üretici (Windows Uyumlu)

Yüksek kaliteli Türkçe ses için edge-tts kullanır (ücretsiz, doğal ses).

Windows'ta çalıştırmak için:
1. Python kurulu olmalı (https://www.python.org/downloads/)
2. Bu klasöre girip run_audiobook.bat dosyasına çift tıkla

Veya komut satırından:
    python generate_audiobook.py
"""

import asyncio
import sys
from pathlib import Path

try:
    import edge_tts
except ImportError:
    print("Hata: edge-tts kurulu değil!")
    print("Lütfen şu komutu çalıştırın:")
    print("    pip install edge-tts")
    input("Devam etmek için Enter'a basın...")
    sys.exit(1)

# ==================== AYARLAR ====================
# Türkçe sesler (kaliteli olanlar):
# tr-TR-EmelNeural   → Kadın (tavsiye edilir)
# tr-TR-AhmetNeural  → Erkek
VOICE = "tr-TR-EmelNeural"

# Okuma hızı: "-" yavaşlatır, "+" hızlandırır
RATE = "-12%"

# Ses tonu
PITCH = "+0Hz"

# Çıktı klasörü (bu scriptin bulunduğu klasörün içinde mp3 diye bir klasör oluşturur)
SCRIPT_DIR = Path(__file__).parent.resolve()
OUTPUT_DIR = SCRIPT_DIR / "mp3"
CHAPTER_DIR = SCRIPT_DIR
PLAYLIST_FILE = SCRIPT_DIR / "playlist.m3u"
# ================================================

async def generate_audio(text: str, output_path: Path):
    """Metni seslendirip MP3 olarak kaydeder."""
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH)
    await communicate.save(str(output_path))
    print(f"✓ Oluşturuldu: {output_path.name}")

def clean_text(text: str) -> str:
    """TTS için metni temizler."""
    lines = []
    for line in text.splitlines():
        line = line.strip()
        # Başlıkları, ayırıcıları ve boş satırları atla
        if line.startswith("#") or line.startswith("---") or not line:
            continue
        # Fazla boşlukları temizle
        line = " ".join(line.split())
        lines.append(line)
    return "\n".join(lines)

async def main():
    print("=" * 50)
    print("Pasifik'in Altındaki Mühür - Sesli Kitap")
    print("Ses: " + VOICE)
    print("=" * 50)
    print()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Bölüm dosyalarını bul
    chapter_files = sorted(CHAPTER_DIR.glob("bolum_*.txt"))

    if not chapter_files:
        print("HATA: bolum_XX.txt dosyaları bulunamadı!")
        print("Lütfen bu scripti 'sesli_kitap' klasörünün içinde çalıştırdığınızdan emin olun.")
        input("Devam etmek için Enter'a basın...")
        return

    print(f"Toplam {len(chapter_files)} bölüm bulundu.\n")

    playlist_lines = []

    for i, chapter_file in enumerate(chapter_files, 1):
        print(f"İşleniyor ({i}/{len(chapter_files)}): {chapter_file.name}")

        try:
            text = chapter_file.read_text(encoding="utf-8")
        except Exception as e:
            print(f"  Dosya okunamadı: {e}")
            continue

        clean = clean_text(text)

        if not clean.strip():
            print("  Atlandı (boş içerik)")
            continue

        output_file = OUTPUT_DIR / f"bolum_{i:02d}.mp3"

        try:
            await generate_audio(clean, output_file)
            playlist_lines.append(f"mp3/{output_file.name}")
        except Exception as e:
            print(f"  Hata oluştu: {e}")
            print("  İnternet bağlantınızı kontrol edin.")

    # Playlist oluştur
    if playlist_lines:
        with open(PLAYLIST_FILE, "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            f.write("#EXTINF:-1,Sesli Kitap - Pasifik'in Altındaki Mühür\n")
            f.write("# Yazar: Emre Ozudogru\n\n")
            for line in playlist_lines:
                f.write(line + "\n")

        print("\n" + "=" * 50)
        print("✓ İşlem tamamlandı!")
        print(f"  MP3 dosyaları: {OUTPUT_DIR}")
        print(f"  Playlist dosyası: {PLAYLIST_FILE}")
        print("\nVLC Media Player ile playlist.m3u dosyasını açabilirsiniz.")
    else:
        print("\nHiçbir bölüm işlenemedi.")

    print("\nKapatmak için Enter'a basın...")
    input()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nİşlem iptal edildi.")
        input("Kapatmak için Enter'a basın...")
