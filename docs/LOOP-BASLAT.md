# Sonsuz gece loop — anlamlı büyütme

Master: `docs/PROMPT-gece-loop-edebi-mukemmellestirme.md`  
State: `docs/LOOP-STATE.md`  
Log: `docs/LOOP-LOG.md`

## Özet
- Her tur: **tüm romanı düşün** → plan → yaz  
- **Yeni sahneler** / anılar / ara çağ / gerekirse yeni bölüm OK  
- Yan ip: **tohum → dans → bağ** (veya tek vuruş kapanış)  
- `open_threads` STATE’te; unutulmuş açık uç yok  
- Cümle dolandırma yok  
- `+~%10` yön; **−10% kısaltma yok**  
- Uzun tire (em dash) **kullanma**; nokta/virgül  

## /loop (kopyala-yapıştır)

```
/loop 5m docs/PROMPT-gece-loop-edebi-mukemmellestirme.md MASTER uygula: tam 1 tur, sonra DUR. (1) CLAUDE + MASTER + LOOP-STATE + LOOP-LOG oku; tum tr/metin/bolumler tarayip butun-roman dusun; open_threads oku; plan max 3 madde (tohum/dans/bag/yeni sahne). (2) Anlamli buyut: YENI SAHNE, yani hikaye, ani, ara cag; gerekirse yeni bolum; cumle dolandirma YASAK. Yan ip ana cizgiyle dans edebilir, sonra baglanir; unutulmus acik uc YOK. (3) Em dash ve en dash KULLANMA (Unicode U+2014 U+2013 yok); nokta ve virgul kullan. (4) +%10 yon: target_delta=max(0.10*dokunulan_kelime, 400); net delta hedef altindaysa commit etme, daha ac. (5) DNA bozma (Ren kahraman degil, Voss yenilmez, karanlik bedel). (6) metinler/*.txt senkron; STATE+LOG+open_threads guncelle; git commit; push YOK; mp3/aiff/pdf YOK; orijinal.txt DOKUNMA. Iceride tur 2 yok.
```

## İptal
Job ID oluşunca not et; iptal: `scheduler_delete <job-id>`

## Sen gelince
```bash
git log --oneline -15
cat docs/LOOP-STATE.md
tail -40 docs/LOOP-LOG.md
wc -w tr/metin/bolumler/*.md | tail -1
```
