#!/usr/bin/env python3
"""
Pasifik’in Altındaki Mühür - Sesli Kitap Üretici
Yüksek kaliteli Türkçe ses için edge-tts kullanır (ücretsiz, doğal ses).

Kurulum:
    pip install -r requirements.txt

Kullanım:
    python generate_audiobook.py

Önerilen Türkçe sesler:
- tr-TR-EmelNeural (kadın, çok doğal)
- tr-TR-AhmetNeural (erkek)

Tüm bölümleri ayrı MP3 olarak üretir ve bir playlist oluşturur.
"""

import asyncio
import os
import subprocess
from pathlib import Path

try:
    import edge_tts
except ImportError:
    print("edge-tts kurulu değil. 'pip install edge-tts' çalıştırın.")
    exit(1)

# Ayarlar
VOICE = "tr-TR-EmelNeural"  # İyi bir Türkçe kadın sesi. Değiştirebilirsin.
RATE = "-10%"               # Biraz yavaş oku (daha rahat dinlenir)
PITCH = "+0Hz"
OUTPUT_DIR = Path("sesli_kitap/mp3")
CHAPTER_DIR = Path("sesli_kitap")
PLAYLIST_FILE = "sesli_kitap/playlist.m3u"

async def generate_audio(text: str, output_path: Path):
    """Tek bir metni seslendirip MP3 olarak kaydeder."""
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH)
    await communicate.save(str(output_path))
    print(f"✓ Oluşturuldu: {output_path.name}")

def clean_text(text: str) -> str:
    """TTS için metni temizle."""
    # Başlıkları ve gereksiz markdown kalıntılarını temizle
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("#") or line.startswith("---") or not line:
            continue
        # Fazla boşlukları temizle
        line = " ".join(line.split())
        lines.append(line)
    return "\n".join(lines)

async def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    chapter_files = sorted(CHAPTER_DIR.glob("bolum_*.txt"))
    if not chapter_files:
        print("Hata: bolum_*.txt dosyaları bulunamadı!")
        return

    playlist_lines = []

    for i, chapter_file in enumerate(chapter_files, 1):
        text = chapter_file.read_text(encoding="utf-8")
        clean = clean_text(text)

        if not clean.strip():
            print(f"Atlandı (boş): {chapter_file.name}")
            continue

        output_file = OUTPUT_DIR / f"bolum_{i:02d}.mp3"

        print(f"İşleniyor: {chapter_file.name} → {output_file.name}")
        await generate_audio(clean, output_file)

        # Playlist için göreli yol
        playlist_lines.append(f"mp3/{output_file.name}")

    # M3U playlist oluştur
    with open(PLAYLIST_FILE, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        f.write("# Sesli Kitap: Pasifik’in Altındaki Mühür\n")
        f.write("# Yazar: Emre Ozudogru\n\n")
        for line in playlist_lines:
            f.write(line + "\n")

    print(f"\n✅ Tamamlandı!")
    print(f"   MP3 dosyaları: {OUTPUT_DIR}")
    print(f"   Playlist: {PLAYLIST_FILE}")
    print(f"\nVLC, Windows Media Player veya telefonunuzda playlist dosyasını açabilirsiniz.")

if __name__ == "__main__":
    asyncio.run(main())
