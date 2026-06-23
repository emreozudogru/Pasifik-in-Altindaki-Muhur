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


mkdir -p "$OUTPUT_DIR"

echo "========================================"
echo "  Pasifik’in Altındaki Mühür - macOS"

echo "  Çıktı: .aiff"
echo "========================================"
echo

# Bölümler dinamik bulunur (sabit sayı yok — roman büyüdükçe otomatik uyum sağlar)
chapter_files=("$CHAPTER_DIR"/bolum_*.txt)
total=${#chapter_files[@]}

if [ "$total" -eq 0 ] || [ ! -f "${chapter_files[0]}" ]; then
    echo "HATA: $CHAPTER_DIR içinde bolum_*.txt bulunamadı!"
    exit 1
fi

echo "Toplam $total bölüm bulundu."
echo

idx=0
for chapter_file in "${chapter_files[@]}"; do
    idx=$((idx + 1))
    base="$(basename "$chapter_file" .txt)"      # bolum_NN
    aiff_file="$OUTPUT_DIR/${base}.aiff"

    # Dosya varsa ve metin daha eski ise atla
    if [ -f "$aiff_file" ]; then
        chapter_mtime=$(stat -f %m "$chapter_file")
        aiff_mtime=$(stat -f %m "$aiff_file")
        if [ "$chapter_mtime" -le "$aiff_mtime" ]; then
            echo "[$idx/$total] Atlandı (güncel): $aiff_file"
            continue
        else
            echo "[$idx/$total] Yeniden oluşturuluyor (metin güncellendi): $aiff_file"
        fi
    fi

    echo "[$idx/$total] İşleniyor: ${base}.txt → $aiff_file"

    say -f "$chapter_file" -o "$aiff_file"

    echo "[$idx/$total] ✓ Oluşturuldu: $aiff_file"
done

echo
echo "========================================"
echo "  Tamamlandı!"
echo "  AIFF dosyaları: $OUTPUT_DIR"
echo "========================================"