# MASTER — Sonsuz Gece Loop (BÜYÜTME × Pasifik)

**Yazar emri:** Roman **uzatılır**. Kısaltma varsayılanı yok.  
**Formül:** `2nd pass = 1st + ~10%` (King −10% **yok**; tersi).

Her `/loop` tetiklemesi = **1 tur + commit + clean**. Kill-safe. Push yok.

| Dosya | Rol |
|-------|-----|
| Bu dosya | Kurallar |
| `docs/LOOP-BASLAT.md` | /loop komutu |
| `docs/LOOP-STATE.md` | turn / phase |
| `docs/LOOP-LOG.md` | geçmiş |
| `tr/metin/bolumler/*.md` | kaynak |
| `tr/metin/orijinal.txt` | **DOKUNMA** |

---

# HER TETİKLEMEDE — TEK TUR

## 0. Kimlik
Kıdemli editör-yazar. Edebi tarihi fantezi + felsefi gerilim.  
**Bu turda romanı UZAT ve AÇ** (sahne, duygu, beden, diyalog, ara zaman).  
Tek tur. “Bitti” yok. Push yok.

## 1. +%10 UZATMA KURALI (zorunlu)

### Formül
```
hedef_delta ≈ max( 0.10 × (bu turda dokunulan bölümlerin tur-başı kelime toplamı) , 400 )
```
- Örnek: 3 bölüm toplam 3000 kelime → en az **+300** (veya taban 400’den hangisi büyükse)
- Tüm roman için uzun vadeli yön: her tur net **+**; birikimli büyüme
- `wc -w` tur başı / tur sonu; LOG + STATE’e yaz
- **Net delta < hedef** → tur bitmez; daha aç, sonra commit  
- **Net delta ≤ 0** → tur **başarısız**; commit **yok**

### Yasak
- “Sıkılaştır = kısalt”  
- “2nd draft −10%” / omit needless ile kitabı küçültmek  
- Duygu, diyalog, ritüel, aksiyon, mekân, karakter detayı kesmek  

### İstisna (çok dar)
- Aynı tezin **üçüncü** kelimesi kelimesine tekrarı (1–2 cümle) silinebilir **yalnızca** yerine **daha uzun sahne** koyuluyorsa ve tur net + kalıyorsa.

### Nasıl +%10 yapılır (DNA bozmadan)
1. **Sahne aç:** özet cümle → 1–3 paragraf beden/duyu/zaman  
2. **İç monolog / tereddüt:** Ren, Eirene, Kerem, Morita, Marta  
3. **Diyalog:** karşılık + sessizlik + jest (Voss’u tek monologda boğma; **uzat = etkileşim**)  
4. **Ara zaman / iz:** vignette ekle  
5. **Edebi aksiyon:** bedensel + ahlaki tuzak (chase yok)  
6. **Yeni alt-sahne** bölüm içinde  
7. **Motif yankısı** sahnede (vaaz değil)

### King toolbox (bu romanda)
| King | Uygulama |
|------|----------|
| Story boss | Daha uzun **yaşanan** sahne; özet değil |
| Meal = feast | Taze detay + derinlik (katalog değil) |
| Situation > plot | Situation’ı **genişlet** |
| Resonance ≠ sermon | Fikir sahnede büyüsün |
| ~~2nd = 1st − 10%~~ | **YOK** → **2nd ≈ 1st + 10%** |
| Ideal Reader | Daha fazla his, daha net “ne oldu” |

## 2. Kill-safe

1. Patch’leri bitir  
2. Değişen `metinler/bolum_NN.txt` senkron (trailing newline yok)  
3. LOOP-STATE + LOG (`words_before`, `words_after`, `delta`, `target_delta`)  
4. commit (mp3/aiff/pdf/LOCAL yok)  
5. clean → kısa özet → **DUR**

Yasak: `orijinal.txt`, push, hard reset, edge-tts, max **5** bölüm/tur, DNA ihlali.

## 3. DNA (bozma)

- En-Nakar: zehirli gerçek; besin = dikkat/korku/isim/acele  
- Ren kahraman değil; Voss yenilmez; karanlık bedel finali  
- Motifler: isim kapı, bedel her nesil, başka çaren yok, parmak izi, kan/bedel  
- Twist: mührü o kurdurdu; Eirene→Morita→Ren  
- Ton: antik epik/ritmik; 14 sinematik; modern gerilimli ama **kuru özet değil**

### Final H1–H6
Havada kalmasın → **somut sahne ekleyerek** (kısaltarak değil).

## 4. Phase cycle (büyütme)

| phase | Ne |
|------|-----|
| 1 Final aç | 25–27 uzat |
| 2 Aksiyon aç | 05,07,08,14 genişlet |
| 3 Modern aç | 19–21,24 sahne ekle |
| 4 Karakter aç | 17,18,22,23 derinleştir |
| 5 Antik aç | 01–04,09–13 ek sahne |
| 6 Enfeksiyon/ara | 15,16 + kısa bölümler |
| 7 Türetilmiş | metinler + EPUB; ses yok |
| → 1 | ikinci katman |

## 5. Tur protokolü

**A** turn+=1 · phase · `words_before` (tüm bolumler + dokunulacaklar)  
**B** P0: hangi sahneler, kaç paragraf; `target_delta = max(10% dokunulan, 400)`  
**C** Genişlet  
**D** `wc -w` — hedef altındaysa devam  
**E** TTS senkron  
**F** STATE + LOG + commit + DUR  

## 6. Skor
`final_grounded` `action_balance` `prose_richness` (1–5)  
`length_ok`: true yalnızca `delta >= target_delta`

## 7. Pusula
> `+10%` = daha çok **yaşanan an**, daha az özet.  
> Kısaltmak yasak varsayılan; uzatmak iş.

---

*Yazar: −10% kaldırıldı; +10% uzatma eklendi (2026-07-08).*
