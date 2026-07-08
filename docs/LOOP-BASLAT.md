# Sonsuz gece loop — nasıl bırakılır

Master kurallar: `docs/PROMPT-gece-loop-edebi-mukemmellestirme.md`  
Durum (kaldığın yer): `docs/LOOP-STATE.md`  
Log: `docs/LOOP-LOG.md`

## Neden bozulmaz / kaybolmaz

| Risk | Koruma |
|------|--------|
| Ortada kill | Her tetikleme = **1 tur + 1 commit**; yarım tur commit’siz bitmez |
| “Nerede kaldım?” | `LOOP-STATE.md` + `LOOP-LOG.md` repoda |
| Yanlış dosya | `orijinal.txt` yasak; max 5 bölüm/tur |
| Ses/PDF şişmesi | gitignore; agent üretmez/commit etmez |
| Push kazası | push yasak |
| Loop metni kaybı | Bu dosya + master prompt **commit’li** |

Sen gelince: sohbeti/loop’u durdur. Repo son commit’te sağlam kalır. İstersen aynı `/loop` ile devam.

**Ses:** Agent MP3 üretmez. Sen host’ta:
`cd tr/sesli_kitap && pip install -r requirements.txt && python3 generate_audiobook.py`

---

## 1) Grok’ta başlat (önerilen)

Sohbete **tek satır** (veya alttaki blok):

```
/loop 25m docs/LOOP-BASLAT.md içindeki TİK PROMPT’unu uygula. Master: docs/PROMPT-gece-loop-edebi-mukemmellestirme.md. Sonsuz; ben durdurana kadar. Her tetiklemede tam 1 tur + commit. Push yok.
```

Interval: `25m` ≈ bir edebi tur için güvenli. Daha agresif: `15m`. Daha yavaş: `45m`.

İptal: Grok scheduler / loop iptali (job ID oluşunca not et) veya sohbeti bırakıp task’ı sil.

---

## 2) TİK PROMPT (her /loop ateşlemesinde agent bunu çalıştırır)

Aşağıdaki bloğu master ile birlikte kullanır; gerekirse yapıştır:

```
TEK TUR — Pasifik'in Altındaki Mühür sonsuz gece loop

1) Oku: CLAUDE.md
2) Oku: docs/PROMPT-gece-loop-edebi-mukemmellestirme.md (MASTER — tüm kurallar)
3) Oku: docs/LOOP-STATE.md (turn/phase/next_chapters)
4) Oku: docs/LOOP-LOG.md (son 2 tur)
5) MASTER’daki “TEK TUR İŞ AKIŞI A→F” uygula:
   - turn += 1
   - max 5 bölüm cerrahi edit (phase’e göre)
   - metinler/*.txt senkron (değişenler)
   - LOOP-STATE + LOOP-LOG güncelle
   - git commit (push YOK)
   - working tree clean
6) 5–8 satır özet yaz, DUR.
   İçeride tur 2’ye geçme. Sonsuz iç döngü yok. “Bitti” / completion promise YOK.
7) ASLA: orijinal.txt, push, mp3/aiff/pdf, edge-tts, reset --hard, Voss yenilgisi, mutlu son

Kill gelirse sorun değil: bir sonraki /loop LOOP-STATE’ten devam eder.
```

---

## 3) Phase sırası (sonsuz cycle)

`1 final → 2 aksiyon → 3 modern → 4 karakter → 5 dil → 6 budama → 7 epub-txt → 1 …`

Phase 1: 25–27 (final yere bas)  
Phase 2: 05, 07, 08, 14  
Phase 3: 19–21, 24  
Phase 4: 17, 18, 22, 23  
…

---

## 4) Sen gelince kontrol

```bash
git log --oneline -20
cat docs/LOOP-STATE.md
tail -40 docs/LOOP-LOG.md
```

Beğenmediğin tur: `git log` + ilgili commit’i revert (agent’a “şu commit’i geri al” de).
