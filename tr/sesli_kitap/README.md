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

---

## Lisans / License

Bu eser ve ondan üretilen sesli kitap, Creative Commons Atıf 4.0 Uluslararası
(CC BY 4.0) lisansı altındadır. Sesli kitabı özgürce dağıtabilir, paylaşabilir
ve ticari olarak kullanabilirsiniz — tek koşul, yazar **Emre Ozudogru** adının
belirtilmesidir. Yazarlık silinemez.

This work and any audiobook produced from it are licensed under Creative Commons
Attribution 4.0 International (CC BY 4.0). You may freely distribute, share and
use the audiobook commercially — provided the author **Emre Ozudogru** is
attributed. Authorship may not be removed.

https://creativecommons.org/licenses/by/4.0/