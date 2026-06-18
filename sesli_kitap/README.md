# Pasifik’in Altındaki Mühür - Sesli Kitap

Bu klasör, romanın **sesli kitap** haline getirilmesi için hazırlanmıştır.

## Dosyalar

- `bolum_01.txt`, `bolum_02.txt`, ... → Her bölümün temiz metin hali (TTS için optimize edilmiş)
- `tam_roman.txt` → Tüm romanın tek parça temiz metin hali
- `generate_audiobook.py` → Otomatik sesli kitap üretici script
- `requirements.txt` → Gerekli Python paketleri

## Nasıl Kullanılır (En Kolay Yöntem)

### 1. Kurulum (bir kere yapılır)

```bash
cd sesli_kitap
pip install -r requirements.txt
```

### 2. Sesli Kitabı Oluştur

```bash
python generate_audiobook.py
```

Script çalışınca `mp3/` klasörünün içine her bölüm için ayrı MP3 dosyası üretecek ve bir `playlist.m3u` oluşturacak.

### Önerilen Ses (Türkçe)

Script içinde şu an `tr-TR-EmelNeural` kullanılıyor (çok doğal kadın sesi).

Başka ses istersen `generate_audiobook.py` dosyasındaki şu satırı değiştir:

```python
VOICE = "tr-TR-EmelNeural"   # Kadın
# VOICE = "tr-TR-AhmetNeural"  # Erkek
```

Tüm mevcut Türkçe sesleri görmek için:
```bash
edge-tts --list-voices | findstr tr-TR
```

## Dinleme

- VLC Media Player (ücretsiz, en iyisi)
- Windows Media Player
- Telefonlarda VLC veya herhangi bir müzik çalar

`playlist.m3u` dosyasını açman yeterli. Bölümler otomatik sırayla çalınır.

## İpuçları

- **Daha yavaş okuma** istersen scriptteki `RATE = "-10%"` değerini `-15%` veya `-20%` yapabilirsin.
- **Tam romanı tek dosya** olarak dinlemek istersen `tam_roman.txt` dosyasını doğrudan edge-tts ile dönüştürebilirsin.
- Toplam süre yaklaşık 4-6 saat civarı olur (hıza göre değişir).

## Lisans

Roman: © 2026 Emre Ozudogru  
Creative Commons Attribution 4.0 International (CC BY 4.0)

Ses dosyalarını üretirken lütfen yazar adını (Emre Ozudogru) belirtmeyi unutma.

---

İyi dinlemeler!
