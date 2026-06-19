# Pasifik’in Altındaki Mühür - Sesli Kitap

Bu klasör, romanın **sesli kitap** haline getirilmesi için hazırlanmıştır.

## Hangi Scripti Kullanmalısın?

| Platform     | Önerilen Script                        | Notlar                              |
|--------------|----------------------------------------|-------------------------------------|
| **Tüm sistemler** | `generate_audiobook.py`            | **En iyi kalite** (edge-tts)        |
| **macOS**    | `generate_audiobook_mac.sh`            | Native `say` komutu (aiff)          |
| **Linux**    | `generate_audiobook_linux.sh`          | edge-tts çağırır                    |
| **Windows**  | `generate_audiobook_windows.ps1`       | edge-tts çağırır                    |

**Tavsiye:** Çoğu kullanıcı için `generate_audiobook.py` (edge-tts) en iyi sonucu verir.

---

## edge-tts ile (Tüm Platformlar - Önerilen)

### Adım 1: Kurulum

```bash
pip install edge-tts
```

### Adım 2: Çalıştır

```bash
cd tr/sesli_kitap
python generate_audiobook.py
```

---

## macOS (Native `say` komutu)

```bash
cd tr/sesli_kitap
chmod +x generate_audiobook_mac.sh
./generate_audiobook_mac.sh
```

Çıktı: `aiff/` klasöründe `.aiff` dosyaları

---

## Linux

```bash
cd tr/sesli_kitap
chmod +x generate_audiobook_linux.sh
./generate_audiobook_linux.sh
```

---

## Windows (PowerShell)

```powershell
cd tr/sesli_kitap
.\generate_audiobook_windows.ps1
```

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