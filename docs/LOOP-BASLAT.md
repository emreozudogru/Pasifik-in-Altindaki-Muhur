# Sonsuz gece loop — anlamlı büyütme

Master: `docs/PROMPT-gece-loop-edebi-mukemmellestirme.md`

## Özet
- Her tur: **tüm romanı düşün** → plan → yaz  
- **Yeni sahneler** / anılar / ara çağ / gerekirse yeni bölüm **OK**  
- Yan ip: **tohum → dans → bağ** (başka bölümde ana hikâyeye oturabilir) veya tek vuruşta kapanış  
- Unutulmuş açık uç **yok**; `open_threads` STATE’te  
- Cümle dolandırma **yok**  
- `+~%10` yön; **−10% yok**  
- **`—` / `–` tire kullanma**

## /loop (kopyala)

```
/loop 5m docs/PROMPT-gece-loop-edebi-mukemmellestirme.md MASTER: 1 tur DUR. (1) Tüm bolumler tarayıp bütün-roman düşün; open_threads oku; plan max 3 (tohum/dans/bağ/yeni sahne). (2) Anlamlı büyüt: YENİ SAHNE; yan ip ana çizgiyle dans edebilir, sonra bağlanır; unutulmuş açık uç YOK. (3) Em dash — – KULLANMA. (4) +%10 yön. (5) DNA. (6) metinler senkron; STATE+LOG+open_threads; commit; push YOK; ses YOK.
```

İptal: `scheduler_delete <job-id>`
