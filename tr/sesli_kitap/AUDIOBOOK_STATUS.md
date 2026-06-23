# Sesli Kitap Durumu

**Son guncelleme:** 2026-06-23

## Roman yapisi degisti: 22 -> 27 bolum

Roman, novella uzunlugundan (~13k kelime) tam roman uzunluguna (~26.5k kelime)
genisletildi. Bolum sayisi 22'den 27'ye cikti, bolumler yeniden numaralandirildi.
`metinler/bolum_01.txt` ... `metinler/bolum_27.txt` guncel metinle yeniden uretildi.

## MP3 durumu

**TUM MP3'ler yeniden uretilmelidir.** Mevcut eski MP3'ler (varsa) hem eski
numaralandirmaya hem de eski/kisa metne ait; artik gecersiz.

`generate_audiobook.py` ile yeniden uretim gerekli. Bu islem bu ortamda (Airlock
sandbox) yapilamaz: edge-tts Azure agina erisim ister, ag yok. Kullanici kendi
makinesinde calistirmali.

## Toplam
Metin (metinler/): 27 / 27 hazir
MP3: 0 / 27 (yeniden uretim bekliyor)

**Not:** MP3 ve AIFF dosyalari .gitignore kapsamindadir, repoya eklenmez.
Playlist: playlist.m3u (27 bolum ile guncellendi)
