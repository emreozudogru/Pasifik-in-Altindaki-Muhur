# Sonsuz gece loop — başlat / durdur

Master (King × Pasifik): `docs/PROMPT-gece-loop-edebi-mukemmellestirme.md`  
State: `docs/LOOP-STATE.md` · Log: `docs/LOOP-LOG.md`

Her `/loop` ateşi = **1 tur + 1 commit + clean tree**.  
Sen gelince loop’u iptal et; repo bozulmaz, progress dosyada kalır.

---

## KOPYALA → sohbete yapıştır (önerilen)

```
/loop 25m docs/PROMPT-gece-loop-edebi-mukemmellestirme.md MASTER’ını uygula: tam 1 tur, sonra DUR. Oku sırayla CLAUDE.md + MASTER + docs/LOOP-STATE.md + docs/LOOP-LOG.md (son 2) + next_chapters. turn+=1; max 5 bölüm cerrahi; King süzgeci (omit needless, adverb, meal=feast, story boss, situation>plot, resonance≠sermon, 2nd≈−10%); DNA bozma (Ren kahraman değil, Voss yenilmez, karanlık bedel, final H1–H6 yere bassın, izinli edebi aksiyon). metinler/*.txt senkron. LOOP-STATE+LOG güncelle. git commit. push YOK. orijinal.txt/mp3/aiff/pdf/LOCAL YOK. edge-tts YOK. İçeride tur 2 yok; “bitti” yok. Kill-safe: her tur clean bitir.
```

| | |
|--|--|
| Interval | `25m` (edebi tur için güvenli). Alternatif: `15m` / `40m` |
| Bitiş | Yok — sen iptal edene kadar |
| İptal | Loop/scheduler job’u sil veya sohbeti bırak |

---

## TİK (MASTER özeti — agent unutursa)

```
1) CLAUDE.md + MASTER + LOOP-STATE + LOG son 2 + hedef bölümler
2) 1 tur A→F (MASTER §6)
3) Commit + clean
4) 5–8 satır özet, DUR
```

Phase cycle: `1 final → 2 aksiyon → 3 modern → 4 karakter → 5 dil → 6 budama → 7 epub-txt → 1…`

---

## Sen gelince

```bash
git log --oneline -25
cat docs/LOOP-STATE.md
tail -50 docs/LOOP-LOG.md
```

MP3 (agent değil, host):

```bash
cd tr/sesli_kitap && pip install -r requirements.txt && python3 generate_audiobook.py
```
