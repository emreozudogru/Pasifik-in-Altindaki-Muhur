#!/bin/bash
#
# Pasifik’in Altındaki Mühür - macOS Sesli Kitap Üretici (say)
#
# Kullanım:
#   chmod +x generate_audiobook_mac.sh
#   ./generate_audiobook_mac.sh
#
# Çıktı: .aiff dosyaları (MP3'e gerek yok)
#

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CHAPTER_DIR="$SCRIPT_DIR/metinler"
OUTPUT_DIR="$SCRIPT_DIR/aiff"          # mp3 yerine aiff klasörü
VOICE="Samantha"                       # macOS kadın sesi
RATE="180"                             # Konuşma hızı

mkdir -p "$OUTPUT_DIR"

echo "========================================"
echo "  Pasifik’in Altındaki Mühür - macOS"
echo "  Ses: $VOICE | Hız: $RATE"
echo "  Çıktı: .aiff"
echo "========================================"
echo

for i in $(seq -w 1 22); do
    chapter_file="$CHAPTER_DIR/bolum_${i}.txt"
    aiff_file="$OUTPUT_DIR/bolum_${i}.aiff"

    if [ ! -f "$chapter_file" ]; then
        echo "[$i/22] Atlandı (dosya yok): $chapter_file"
        continue
    fi

    if [ -f "$aiff_file" ]; then
        echo "[$i/22] Atlandı (zaten var): $aiff_file"
        continue
    fi

    echo "[$i/22] İşleniyor: bolum_${i}.txt → $aiff_file"

    say -f "$chapter_file" -o "$aiff_file" -v "$VOICE" -r "$RATE"

    echo "[$i/22] ✓ Oluşturuldu: $aiff_file"
done

echo
echo "========================================"
echo "  Tamamlandı!"
echo "  AIFF dosyaları: $OUTPUT_DIR"
echo "========================================"