# Sonsuz gece loop — +%10 UZATMA

Master: `docs/PROMPT-gece-loop-edebi-mukemmellestirme.md`

**Formül:** `2nd ≈ 1st + 10%` (dokunulan bölümler).  
**−10% kısaltma YOK.**

## /loop (kopyala)

```
/loop 25m docs/PROMPT-gece-loop-edebi-mukemmellestirme.md MASTER: 1 tur DUR. +%10 UZATMA zorunlu (target_delta = max(0.10×dokunulan_kelime, 400)). −10% yok. Oku CLAUDE + MASTER + LOOP-STATE + LOG + next_chapters. turn+=1; max 5 bölüm AÇ/GENİŞLET. DNA bozma. metinler senkron. STATE+LOG (words_before/after/delta/target_delta). commit. push YOK. ses/pdf YOK. İçeride tur 2 yok.
```

İptal: `scheduler_delete <job-id>`
