#!/bin/bash
#
# Pasifik’in Altındaki Mühür - Linux Sesli Kitap Üretici
#
# Önerilen: edge-tts (Python) — en iyi Türkçe kalite
# Alternatif: espeak-ng (daha düşük kalite)
#
# Kullanım:
#   chmod +x generate_audiobook_linux.sh
#   ./generate_audiobook_linux.sh
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHAPTER_DIR="$SCRIPT_DIR/metinler"
OUTPUT_DIR="$SCRIPT_DIR/mp3"
VOICE="tr-TR-EmelNeural"
RATE="-12%"

mkdir -p "$OUTPUT_DIR"

echo "========================================"
echo "  Pasifik’in Altındaki Mühür - Linux"
echo "  edge-tts ile Türkçe ses"
echo "========================================"
echo

if ! command -v python3 &> /dev/null; then
    echo "Hata: python3 bulunamadı."
    exit 1
fi

if ! python3 -c "import edge_tts" 2>/dev/null; then
    echo "edge-tts kurulu değil. Kurmak için:"
    echo "  pip3 install edge-tts"
    exit 1
fi

python3 "$SCRIPT_DIR/generate_audiobook.py"