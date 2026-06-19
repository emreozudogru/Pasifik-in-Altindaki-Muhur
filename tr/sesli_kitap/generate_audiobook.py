#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pasifik’in Altındaki Mühür - Sesli Kitap Üretici (Windows Uyumlu + Retry)

Yüksek kaliteli Türkçe ses için edge-tts kullanır.

Kullanım:
    python generate_audiobook.py

Veya çift tıkla: run_audiobook.bat
"""

import asyncio
import re
import sys
import time
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
VOICE = "tr-TR-EmelNeural"   # Kadın sesi (tavsiye edilir)
# VOICE = "tr-TR-AhmetNeural"  # Erkek sesi

RATE = "-12%"                # Okuma hızı (daha yavaş = daha rahat dinlenir)
PITCH = "+0Hz"

MAX_RETRIES = 3              # Her bölüm için maksimum deneme sayısı
RETRY_DELAY = 5              # Denemeler arası bekleme (saniye)

# Dosya yolları (script'in bulunduğu klasöre göre)
SCRIPT_DIR = Path(__file__).parent.resolve()
OUTPUT_DIR = SCRIPT_DIR / "mp3"
CHAPTER_DIR = SCRIPT_DIR / "metinler"
PLAYLIST_FILE = SCRIPT_DIR / "playlist.m3u"
# ================================================

async def generate_audio(text: str, output_path: Path) -> bool:
    """Tek bir metni seslendirip MP3 olarak kaydeder. Başarılı olursa True döner."""
    communicate = edge_tts.Communicate(text, VOICE, rate=RATE, pitch=PITCH)
    await communicate.save(str(output_path))
    return True

def clean_text(text: str) -> str:
    """TTS için metni temizler."""
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("#") or line.startswith("---") or not line:
            continue
        # Emoji ve özel karakterleri temizle
        line = re.sub(r'[🌑]', '', line)
        line = " ".join(line.split())
        lines.append(line)
    return "\n".join(lines)

async def process_chapter(chapter_file: Path, index: int, total: int) -> bool:
    """Bir bölümü işler (retry ile)."""
    output_file = OUTPUT_DIR / f"bolum_{index:02d}.mp3"

    # Zaten varsa atla
    if output_file.exists():
        print(f"[{index}/{total}] Atlandı (zaten var): {output_file.name}")
        return True

    text = chapter_file.read_text(encoding="utf-8")
    clean = clean_text(text)

    if not clean.strip():
        print(f"[{index}/{total}] Atlandı (boş): {chapter_file.name}")
        return True

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            print(f"[{index}/{total}] İşleniyor: {chapter_file.name} (deneme {attempt}/{MAX_RETRIES})")
            await generate_audio(clean, output_file)
            print(f"[{index}/{total}] ✓ Oluşturuldu: {output_file.name}")
            return True
        except Exception as e:
            print(f"[{index}/{total}] Hata (deneme {attempt}): {str(e)[:80]}")
            if attempt < MAX_RETRIES:
                print(f"  {RETRY_DELAY} saniye sonra tekrar denenecek...")
                time.sleep(RETRY_DELAY)
            else:
                print(f"[{index}/{total}] BAŞARISIZ: {chapter_file.name}")
                return False

    return False

async def main():
    print("=" * 55)
    print("  Pasifik'in Altındaki Mühür - Sesli Kitap Üretici")
    print("  Ses: " + VOICE)
    print("=" * 55)
    print()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    chapter_files = sorted(CHAPTER_DIR.glob("bolum_*.txt"))

    if not chapter_files:
        print("HATA: bolum_*.txt dosyaları bulunamadı!")
        print("Bu scripti 'sesli_kitap' klasörünün içinde çalıştırdığınızdan emin olun.")
        input("Kapatmak için Enter'a basın...")
        return

    print(f"Toplam {len(chapter_files)} bölüm bulundu.\n")

    playlist_lines = []
    success_count = 0

    for i, chapter_file in enumerate(chapter_files, 1):
        success = await process_chapter(chapter_file, i, len(chapter_files))
        if success:
            success_count += 1
            playlist_lines.append(f"mp3/bolum_{i:02d}.mp3")

    # Playlist oluştur
    if playlist_lines:
        with open(PLAYLIST_FILE, "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            f.write("# Sesli Kitap: Pasifik'in Altındaki Mühür\n")
            f.write("# Yazar: Emre Ozudogru\n\n")
            for line in playlist_lines:
                f.write(line + "\n")

    print("\n" + "=" * 55)
    print(f"İşlem tamamlandı! Başarılı: {success_count}/{len(chapter_files)}")
    print(f"MP3 dosyaları: {OUTPUT_DIR}")
    print(f"Playlist: {PLAYLIST_FILE}")
    print("\nVLC ile playlist.m3u dosyasını açabilirsiniz.")
    print("=" * 55)
    print("\nKapatmak için Enter'a basın...")
    input()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nİşlem kullanıcı tarafından iptal edildi.")
        input("Kapatmak için Enter'a basın...")
    except Exception as e:
        print(f"\nBeklenmedik hata: {e}")
        input("Kapatmak için Enter'a basın...")
