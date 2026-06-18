# Pasifik’in Altındaki Mühür - Sesli Kitap (Windows)

Bu klasör, romanın **sesli kitap** haline getirilmesi için hazırlanmıştır.

## Windows'ta En Kolay Kullanım (Tavsiye Edilen)

### Adım 1: Python Kurulumu (İlk defa yapacaksan)

1. https://www.python.org/downloads/ adresine git.
2. "Download Python" butonuna tıkla.
3. İndirdiğin `.exe` dosyasını çalıştır.
4. **Kurulum sırasında mutlaka** "Add Python to PATH" kutusunu işaretle.
5. "Install Now" de.

### Adım 2: Sesli Kitabı Oluştur

1. `sesli_kitap` klasörüne gir.
2. `run_audiobook.bat` dosyasına **çift tıkla**.

Script otomatik olarak:
- Gerekli kütüphaneleri kurar
- Her bölümü yüksek kaliteli Türkçe sesle MP3'e çevirir
- Hata olursa aynı bölümü birkaç kez dener (retry özelliği)

İlk çalıştırmada 15-40 dakika sürebilir (internet hızına göre).

---

## Oluşan Dosyalar

- `mp3/bolum_01.mp3`, `bolum_02.mp3` ... → Sesli bölümler
- `playlist.m3u` → VLC ile açınca hepsini sırayla çalar

---

## Sık Karşılaşılan Sorunlar ve Çözümleri

### "Cannot connect to host speech.platform.bing.com" hatası
Bu Microsoft'un TTS sunucusuna bağlanamama hatasıdır. Script artık otomatik yeniden deniyor. 

Yine de oluyorsa:
- İnternet bağlantını kontrol et
- Antivirüs / güvenlik duvarını geçici olarak kapatıp dene
- Birkaç dakika bekleyip tekrar çalıştır

### Python bulunamadı hatası
`run_audiobook.bat` sana Python indirme linkini verecektir. Yukarıdaki "Adım 1"i takip et.

---

## Ses Ayarlarını Değiştirmek İstersen

`generate_audiobook.py` dosyasını Not Defteri ile aç ve şu satırları değiştir:

```python
VOICE = "tr-TR-EmelNeural"   # Kadın sesi (tavsiye edilir)
# VOICE = "tr-TR-AhmetNeural"  # Erkek sesi

RATE = "-12%"                # Daha yavaş okumak için: -15% veya -20%
```

---

## Dinleme Önerisi

**VLC Media Player** kullan (ücretsiz):
- https://www.videolan.org/vlc/
- `playlist.m3u` dosyasına çift tıkla.

---

## Lisans

© 2026 Emre Ozudogru  
Creative Commons Attribution 4.0 International (CC BY 4.0)

Sesli kitabı paylaşırken lütfen yazar adını (Emre Ozudogru) belirt.

İyi dinlemeler!