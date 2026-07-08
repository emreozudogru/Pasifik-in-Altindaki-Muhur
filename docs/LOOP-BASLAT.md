# Sonsuz gece loop — anlamlı büyütme

Master: `docs/PROMPT-gece-loop-edebi-mukemmellestirme.md`

## Kurallar (özet)
- Her tur **önce tüm romanı düşün**, sonra planla, sonra yaz  
- **Cümle dolandırma yok**  
- Yeni sahne / anı / ara çağ / gerekirse **yeni bölüm** OK  
- Her yeni hikâyecik **başı–sonu kapalı**  
- `+~%10` yön (anlamlı); **−10% kısaltma yok**  
- Aklına iyi fikir gelirse yap; eski kısaltma loop’u durdurmasın  

## /loop (kopyala)

```
/loop 25m docs/PROMPT-gece-loop-edebi-mukemmellestirme.md MASTER: 1 tur DUR. (1) Tüm bolumler'i tarayıp bütün-roman düşün; plan max 3 madde. (2) Anlamlı büyüt: yeni kapalı hikâyecik/anı/ara çağ/sahne; gerekirse yeni bölüm; cümle dolandırma YASAK. (3) +%10 yön: target_delta=max(0.10×dokunulan,400); −10% yok. (4) DNA bozma; açık uçlu vignette yok. (5) metinler senkron; STATE+LOG; commit; push YOK; ses YOK. İçeride tur 2 yok.
```

İptal: `scheduler_delete <job-id>`
