# Pasifik’in Altındaki Mühür - Sesli Kitap (Windows)

Bu klasör, romanın **sesli kitap** haline getirilmesi için hazırlanmıştır.

## Windows'ta Kolay Kullanım (Önerilen)

### Adım 1: Python Kurulumu (Eğer yoksa)

1. Şu adrese gidin: https://www.python.org/downloads/
2. **"Download Python"** butonuna tıklayın (en son sürüm).
3. İndirdiğiniz `.exe` dosyasını çalıştırın.
4. **Önemli:** Kurulum ekranında **"Add Python to PATH"** kutucuğunu işaretleyin.
5. Install Now'a tıklayın.

### Adım 2: Sesli Kitabı Oluştur

1. Bu klasöre (`sesli_kitap`) girin.
2. `run_audiobook.bat` dosyasına **çift tıklayın**.
3. Komut penceresi açılacak, gerekli paketleri otomatik kuracak ve MP3'leri üretecek.

İlk çalıştırmada biraz zaman alabilir (internet hızınıza göre 10-20 dakika).

### Oluşan Dosyalar

- `mp3/` klasörü içinde `bolum_01.mp3`, `bolum_02.mp3` ... dosyaları
- `playlist.m3u` → VLC ile açınca tüm bölümleri sırayla çalar

---

## Manuel Kurulum (İsterseniz)

Komut İstemi'ni açıp şu komutları yazabilirsiniz:

```cmd
cd sesli_kitap
pip install -r requirements.txt
python generate_audiobook.py
```

---

## Ayarlar

Ses türünü ve hızını değiştirmek isterseniz `generate_audiobook.py` dosyasını Not Defteri ile açın ve şu satırları düzenleyin:

```python
VOICE = "tr-TR-EmelNeural"   # Kadın sesi (tavsiye)
# VOICE = "tr-TR-AhmetNeural"  # Erkek sesi

RATE = "-12%"                # Okuma hızı (daha yavaş için -15% veya -20%)
```

---

## Dinleme

En iyi sonuç için **VLC Media Player** kullanın:

1. VLC'yi indirin: https://www.videolan.org/vlc/
2. `playlist.m3u` dosyasına çift tıklayın.

---

## Lisans

© 2026 Emre Ozudogru  
Creative Commons Attribution 4.0 (CC BY 4.0)

Sesli kitabı başkalarıyla paylaşırken lütfen yazar adını (Emre Ozudogru) belirtin.

İyi dinlemeler!