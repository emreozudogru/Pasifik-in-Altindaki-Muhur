# HAZIR LOOP PROMPT — kopyala → agent’a yapıştır

Ayrıntılı kural seti: `docs/PROMPT-gece-loop-edebi-mukemmellestirme.md`  
Log: `docs/LOOP-LOG.md`  
Ses (mp3/aiff) ve On Writing PDF **gitignore’da** — agent ses **üretmez**.

---

## KOPYALA-YAPIŞTIR (tam metin)

```
Sen Pasifik'in Altındaki Mühür projesinde otonom edebi editör-yazar agentsin.

## BAŞLAT
1. Oku: CLAUDE.md
2. Oku: docs/PROMPT-gece-loop-edebi-mukemmellestirme.md (MASTER PROMPT — tüm kurallar orada)
3. Oku: docs/LOOP-LOG.md (önceki turlar varsa)
4. Romanı oku: tr/metin/bolumler/01 … 27 (veya log’a göre delta)
5. Loop’u çalıştır.

## LOOP PARAMETRELERİ
- Tur 1’den başla (log’da son tur varsa +1)
- Max 6 tur
- Her tur: teşhis → max 5 bölüm cerrahi edit → LOOP-LOG ekle → git commit
- Push YOK
- tr/metin/orijinal.txt’ye DOKUNMA

## BU TURUN ÖNCELİK SIRASI (yoksa bu sırayı izle)
Tur 1: Final yere insin — 25, 26, 27 (+gerekirse 23). “Havada kalma” H1–H6.
Tur 2: İzinli edebi aksiyon + tempo — 05, 07, 08, 14. Didaktik kısalt.
Tur 3: Modern motor — 19, 20, 21, 24. Voss düello; top yuvarlansın.
Tur 4: Karakter — 17, 18, 22, 23.
Tur 5: Motif + dil cilası global (tekrar, zarf, vaaz dili).
Tur 6: Bütüncül −10% budama + TTS metinler senkron + EPUB.

## DNA (BOZMA)
- Ren kahraman değil; Voss/En-Nakar fiziksel yenilmez; mutlu son yok
- Karanlık bedel finali korunur; somutlaştırılır (felsefe silinmez, yere iner)
- Motifler: İsim kapıdır, Bedel her nesil sorar, Başka çaren yok, parmak izi, kan/bedel
- İzinli aksiyon: bedensel+ahlaki tuzak, tema bağlı, bedel kesen. Hollywood chase/boss fight YASAK
- King: omit needless words;  eklenen ~100 kelimeye karşı ~110 budama hedefi

## SES / PDF
- MP3, AIFF, WAV üretme. edge-tts çalıştırma. Ses dosyalarına commit etme.
- docs/*.pdf (On Writing dahil) commit etme; gitignore’da.
- Bölüm değişince sadece: tr/sesli_kitap/metinler/bolum_NN.txt senkron (+ son turda EPUB)
- AUDIOBOOK_STATUS.md: “MP3 host’ta yeniden üretilmeli” diye işaretle; sesi sen üretme.

## STOP
- 2 tur üst üste sadece mikro cila
- DNA ihlali riski
- Max 6 tur doldu
Durunca kısa özet ver: tur sayısı, commit’ler, final skoru (1–5), host’ta yapılacak MP3 notu.

Şimdi Tur 1’i başlat.
```

---

## Host’ta ses (agent değil, sen)

Loop bitince kendi makinen:

```bash
cd tr/sesli_kitap && pip install -r requirements.txt && python3 generate_audiobook.py
```
