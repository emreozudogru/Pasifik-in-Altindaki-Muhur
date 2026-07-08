# Sonsuz gece loop — anlamlı büyütme

Master: `docs/PROMPT-gece-loop-edebi-mukemmellestirme.md`

## Özet
- Her tur: **tüm romanı düşün** → plan → yaz  
- **Yeni sahneler** / anılar / ara çağ / gerekirse yeni bölüm **OK**  
- Cümle dolandırma **yok**  
- Her ek hikâye **başı-sonu kapalı**  
- `+~%10` yön; **−10% yok**  
- **`—` / `–` tire kullanma** (AI duruyor; nokta/virgül)

## /loop (kopyala)

```
/loop 5m docs/PROMPT-gece-loop-edebi-mukemmellestirme.md MASTER: 1 tur DUR. (1) Tüm bolumler tarayıp bütün-roman düşün; plan max 3. (2) Anlamlı büyüt: YENİ SAHNE, kapalı hikâyecik, anı, ara çağ; gerekirse yeni bölüm; cümle dolandırma YASAK. (3) Em dash/tire — ve – KULLANMA; nokta virgül. (4) +%10 yön target_delta=max(0.10×dokunulan,400). (5) DNA; açık uç yok. (6) metinler senkron; STATE+LOG; commit; push YOK; ses YOK.
```

İptal: `scheduler_delete <job-id>`
