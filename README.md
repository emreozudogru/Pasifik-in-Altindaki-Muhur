# Pasifik'in Altındaki Mühür

Edebi tarihi/fantastik roman.

## Lisans

Bu roman **Creative Commons Attribution 4.0 International (CC BY 4.0)** lisansı ile lisanslanmıştır.

- Herkes eseri **kopyalayabilir, dağıtabilir, uyarlayabilir** ve **ticari amaçlarla** kullanabilir.
- Örnek: e-kitap yapma, basım, yayınlama, çeviri, remix.
- **Zorunlu koşul:** Yazar adı olarak **Emre Ozudogru** belirtilmelidir.

Önerilen atıf:
> "Pasifik'in Altındaki Mühür" © 2026 Emre Ozudogru  
> Licensed under CC BY 4.0  
> https://creativecommons.org/licenses/by/4.0/

Tam lisans metni: [LICENSE](LICENSE) dosyasında veya  
https://creativecommons.org/licenses/by/4.0/deed.tr

## Durum

- Ana dal (`main`) üzerinde çalışılmaktadır.

## Workflow

- Her anlamlı değişiklikte **commit + push** yapılıyor.
- Remote: https://github.com/emreozudogru/Pasifik-in-Altindaki-Muhur.git

## Klasör Yapısı

```
Roman/
├── README.md
├── LICENSE
├── .gitignore
├── metin/
│   ├── orijinal.txt          — Roman metni (orijinal, değiştirilmez)
│   └── bolumler/             — 22 ayrı bölüm (geliştirilmiş versiyon)
│       ├── 01-prolog-dunyanin-ucu.md
│       ├── 02-ilk-savas.md
│       └── ... (22 bölüm)
├── sesli_kitap/
│   ├── README.md             — Sesli kitap kullanım talimatları
│   ├── metinler/             — Her bölüm için temiz metin (TTS için)
│   ├── mp3/                  — Üretilen ses dosyaları
│   ├── generate_audiobook.py — Ses üretim scripti
│   ├── requirements.txt
│   └── run_audiobook.bat     — Windows'ta çift tıkla çalıştır
├── docs/
│   ├── implementation-plan.md — Geliştirme planı
│   └── tasarim-spec.md        — Roman tasarım spesifikasyonu
└── mcps/                      — AI araçları (MCP şemaları)
```

## Sesli Kitap

`sesli_kitap/` klasöründe romanın **sesli kitap** haline getirilmesi için hazır paket var.

### Windows'ta En Kolay Kullanım:
1. `sesli_kitap` klasörüne girin.
2. `run_audiobook.bat` dosyasına **çift tıklayın**.

Script otomatik olarak gerekli paketleri kuracak ve her bölüm için MP3 üretecektir.

Detaylı talimatlar için `sesli_kitap/README.md` dosyasına bakın.

---

Başlangıç: 2026  
Yazar: Emre Ozudogru
