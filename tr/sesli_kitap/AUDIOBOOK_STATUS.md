# Sesli Kitap Durumu

**Son guncelleme:** 2026-06-18 00:02

## Basarili Bolumler (MP3 var)
bolum_04
bolum_05
bolum_06
bolum_10
bolum_11
bolum_15
bolum_17
bolum_18
bolum_19
bolum_20
bolum_22

## Toplam
Basarili: 11 / 22

**Not:** MP3 dosyaları .gitignore kapsamındadır ve repo'ya eklenmez. Yerel olarak sesli_kitap/mp3/ klasorunde bulunur.

Playlist: playlist.m3u (sadece basarili bolumler ile guncellendi)

## UYARI: metinler/ yeniden senkronlandi (2026-06-22)

`metinler/bolum_*.txt` dosyalari `metin/bolumler/*.md` ile yeniden esitlendi
(bolum 01,02,04,05,07,11-18,20,21,22 guncellendi). Onceki TTS metinleri
genisletme/duzeltme oncesi eski metni iceriyordu.

Bu nedenle mevcut tum MP3'ler artik metinle TUTARSIZ olabilir; bir sonraki
firsatta `generate_audiobook.py` ile yeniden uretilmelidir. (MP3 uretimi bu
ortamda yapilamadi: TTS/ses araci ve ag erisimi yok.)
