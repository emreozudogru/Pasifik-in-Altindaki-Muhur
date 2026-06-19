# Sesli Kitap Script Kullanım Kılavuzu / Audiobook Script Guide

## edge-tts (Tüm Platformlar - Önerilen)

`generate_audiobook.py` scripti **edge-tts** kullanır. En iyi Türkçe ses kalitesini verir ve Linux, macOS, Windows'ta çalışır.

### Kurulum

```bash
pip install edge-tts
```

### Çalıştırma

```bash
cd tr/sesli_kitap
python generate_audiobook.py
```

**Çıktı:** `mp3/` klasöründe `bolum_01.mp3` ... `bolum_22.mp3`

---

## macOS Native (`say` komutu)

`generate_audiobook_mac.sh` scripti macOS'un yerleşik `say` komutunu kullanır.

### Çalıştırma

```bash
cd tr/sesli_kitap
chmod +x generate_audiobook_mac.sh
./generate_audiobook_mac.sh
```

**Çıktı:** `aiff/` klasöründe `bolum_01.aiff` ... `bolum_22.aiff`

> Not: Bu script sadece macOS'ta çalışır.

---

## Özet / Summary

| Script | Platform | Ses Motoru | Çıktı Formatı |
|--------|----------|------------|---------------|
| `generate_audiobook.py` | Linux / macOS / Windows | edge-tts | `.mp3` |
| `generate_audiobook_mac.sh` | Sadece macOS | macOS `say` | `.aiff` |

**Tavsiye:** Çoğu kullanıcı için `generate_audiobook.py` yeterlidir.