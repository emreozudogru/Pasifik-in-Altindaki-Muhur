# Pasifik’in Altındaki Mühür

Edebi tarihi/fantastik roman.

## Lisans

Bu roman **Creative Commons Attribution 4.0 International (CC BY 4.0)** lisansı ile lisanslanmıştır.

- Herkes eseri **kopyalayabilir, dağıtabilir, uyarlayabilir** ve **ticari amaçlarla** kullanabilir.
- Örnek: e-kitap yapma, basım, yayınlama, çeviri, remix.
- **Zorunlu koşul:** Yazar adı olarak **Emre Ozudogru** belirtilmelidir.

Önerilen atıf:
> "Pasifik’in Altındaki Mühür" © 2026 Emre Ozudogru  
> Licensed under CC BY 4.0  
> https://creativecommons.org/licenses/by/4.0/

Tam lisans metni: [LICENSE](LICENSE) dosyasında veya  
https://creativecommons.org/licenses/by/4.0/deed.tr

## Durum
- Ana dal (`main`) üzerinde çalışılmaktadır.
- Orijinal metin: `Pasifikin Altindaki Muhur.txt`

## Workflow
- Her anlamlı değişiklikte **commit + push** yapılıyor.
- Remote: https://github.com/emreozudogru/Pasifik-in-Altindaki-Muhur.git

## Klasör Yapısı
- `LICENSE` — CC BY 4.0 lisansı
- `Pasifikin Altindaki Muhur.txt` — Roman metni (orijinal)
- `Pasifikin_Altindaki_Muhur_Genisletilmis.md` — Tüm bölümler bir arada (genişletilmiş)
- `bolumler/` — 22 ayrı bölüm (genişletilmiş versiyon)
- `sesli_kitap/` — Sesli kitap hazırlığı (temiz metinler + Python script)
- `README.md` — Bu dosya
- `docs/` — Ek dokümantasyon

## Sesli Kitap

`sesli_kitap/` klasöründe romanın sesli kitap haline getirilmesi için gerekli dosyalar var:

- Her bölümün temiz metin hali
- `generate_audiobook.py` → Ücretsiz, yüksek kaliteli Türkçe ses ile MP3 üreten script (edge-tts)
- Detaylı kullanım talimatı `sesli_kitap/README.md` içinde

Kurulum ve kullanım için `sesli_kitap/README.md` dosyasına bak.

Başlangıç: 2026
Yazar: Emre Ozudogru
