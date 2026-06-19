# Pasifik’in Altındaki Mühür - Sesli Kitap

Bu klasör, romanın **sesli kitap** haline getirilmesi için hazırlanmıştır.

## Önerilen Scriptler

| Platform          | Script                          | Açıklama                              |
|-------------------|----------------------------------|---------------------------------------|
| **Tüm sistemler** | `generate_audiobook.py`         | **edge-tts** (en iyi Türkçe kalite)   |
| **macOS**         | `generate_audiobook_mac.sh`     | Native `say` komutu (aiff)            |

**Tavsiye:** Çoğu kullanıcı için `generate_audiobook.py` (edge-tts) yeterlidir.

---

## edge-tts (Tüm Platformlar - Önerilen)

### Kurulum

```bash
pip install edge-tts
```

### Çalıştır

```bash
cd tr/sesli_kitap
python generate_audiobook.py
```

---

## macOS Native (`say` komutu)

```bash
cd tr/sesli_kitap
chmod +x generate_audiobook_mac.sh
./generate_audiobook_mac.sh
```

Çıktı: `aiff/` klasöründe `.aiff` dosyaları