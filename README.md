# Pasifik’in Altındaki Mühür

**The Seal Beneath the Pacific**

Edebi tarihi fantezi romanı / Literary historical fantasy novel

Yazar: Emre Ozudogru  
Lisans: CC BY 4.0

---

## İçindekiler / Contents

- [Türkçe](#türkçe)
- [English](#english)

---

## Türkçe

### Roman

Roman, 217 BCE'den 2026'ya uzanan bir hikâye. Antik çağda En-Nakar adlı varlığın hapsedilmesi, 1945'te mührün atom bombasıyla çatlaması ve 2026'da Sato Ren'in bu varlıkla yüzleşmesi anlatılıyor.

**Dosya yapısı:**
- `tr/metin/orijinal.txt` — Orijinal metin (değiştirilmez)
- `tr/metin/bolumler/` — 27 bölüm (geliştirilen versiyon)
- `tr/sesli_kitap/` — Sesli kitap scriptleri ve metinleri

### Sesli Kitap

Sesli kitap için iki seçenek vardır:

1. **edge-tts** (önerilen): `tr/sesli_kitap/generate_audiobook.py`
2. **macOS native**: `tr/sesli_kitap/generate_audiobook_mac.sh`

Detaylı kullanım için: [tr/sesli_kitap/README_scripts.md](tr/sesli_kitap/README_scripts.md)

### eBook / EPUB

EPUB oluşturmak için:

```bash
cd tr/ebook
pip install ebooklib
python generate_ebook.py
```

Çıktı: `pasifik_muhur.epub`

---

## English

### The Novel

The novel spans from 217 BCE to 2026. It tells the story of an entity called En-Nakar imprisoned in ancient times, the cracking of its seal by the atomic bomb in 1945, and Sato Ren's confrontation with it in 2026.

**File structure:**
- `tr/metin/orijinal.txt` — Original text (never modify)
- `tr/metin/bolumler/` — 27 chapters (expanded version)
- `tr/sesli_kitap/` — Audiobook scripts and texts

### Audiobook

There are two options for the audiobook:

1. **edge-tts** (recommended): `tr/sesli_kitap/generate_audiobook.py`
2. **macOS native**: `tr/sesli_kitap/generate_audiobook_mac.sh`

For detailed usage instructions, see: [tr/sesli_kitap/README_scripts.md](tr/sesli_kitap/README_scripts.md)

---

## Lisans / License

Bu eser [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) lisansı ile lisanslanmıştır.

This work is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).

Yazar adı belirtilerek ticari kullanım dahil her türlü kullanım serbesttir.

Attribution to the author is required. Commercial use is permitted.