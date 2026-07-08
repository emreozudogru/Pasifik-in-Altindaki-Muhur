# MASTER — Sonsuz Gece Loop (BÜYÜTME × Pasifik)

**Öncelik değişti (yazar emri):** Bu roman **kısaltılmak için değil, uzatılmak ve derinleştirilmek için** loop’a girer.  
Önceki turlarda King “−10%” yanlış uygulandı → **varsayılan artık net kelime artışı**.

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

## 1. BÜYÜTME KURALI (zorunlu — kısaltma yasağı)

### Her tur
- **Net kelime delta: POZİTİF** (hedef **+500 … +1500** kelime / tur, tüm dokunulan dosyalar toplamı)
- `wc -w` ile tur başı/sonu ölç; LOG’a yaz
- Negatif net delta = **tur başarısız** → commit etme; genişlet, sonra commit

### Nasıl uzatılır (DNA bozmadan)
1. **Sahne aç:** tek cümlelik olay → 1–2 paragraf beden/duyu/zaman
2. **İç monolog / tereddüt:** Ren, Eirene, Kerem, Morita, Marta
3. **Diyalog vuruşu:** Voss’u kısaltma; **karşılık + sessizlik + jest** ekle (monolog değil düello)
4. **Ara zaman / iz:** “yıllar geçti” yerine 2–4 somut vignette
5. **Edebi aksiyon:** bedensel + ahlaki tuzak (chase yok)
6. **Yeni alt-sahne** (bölüm içinde): yolculuk kaybı, inşa yarası, Arşiv gece mesajı, hastane koridoru vb.
7. **Motif yankısı:** parmak, bedel, sessizlik — sahne içinde, vaaz değil

### Ne KESİLİR (sadece bu)
- Aynı tezin **üçüncü** tekrarı (kelimesi kelimesine)
- Boş dolgu (“çok önemliydi ki…”)
- **ASLA:** duygu, diyalog zenginliği, ritüel, aksiyon, karakter detayı, mekân dokusu

### King toolbox (YENİDEN YORUM)
| King | Bu romanda |
|------|------------|
| Story boss | Top yuvarlansın — **daha uzun sahne** ile, özetle değil |
| Meal = feast | Az ama **taze** detay; katalog değil, **derinlik** |
| Situation > plot | Var olan situation’ı **genişlet**, jackhammer plan ekleme |
| Resonance ≠ sermon | Fikir **sahnede** büyüsün; makale paragrafı ekleme |
| 2nd draft −10% | **Yalnızca** yeni yazdığın pasajın kendi şişkinliği için; kitabı küçültme lisansı **değil** |
| Ideal Reader | Daha fazla his / daha net “ne oldu” — daha az özet |

## 2. Kill-safe

1. Patch’leri bitir  
2. Değişen `metinler/bolum_NN.txt` senkron (trailing newline yok)  
3. LOOP-STATE + LOG  
4. commit (mp3/aiff/pdf/LOCAL yok)  
5. clean → kısa özet → **DUR**

Yasak: `orijinal.txt`, push, hard reset, edge-tts, max **5** bölüm/tur, DNA ihlali.

## 3. DNA (bozma)

- En-Nakar: zehirli gerçek; besin = dikkat/korku/isim/acele  
- Ren kahraman değil; Voss yenilmez; karanlık bedel finali  
- Motifler: isim kapı, bedel her nesil, başka çaren yok, parmak izi, kan/bedel  
- Twist tohumları: mührü o kurdurdu; Eirene→Morita→Ren  
- Ton: antik epik/ritmik; 14 sinematik; modern sıkışık ama **kuru özet değil**

### Final H1–H6
Havada kalmasın: somut iz, Ren imgesi, ara halka vignette, karanlık bedel **görülsün** — bunu **kısaltarak değil, somut sahne ekleyerek** yap.

## 4. Phase cycle (büyütme odaklı)

| phase | İsim | Ne yap |
|------|------|--------|
| 1 | Final aç | 25–27: ara yıllar, bedel sahneleri, Ren son günleri **uzat** |
| 2 | Aksiyon aç | 05,07,08,14: beden, ritim, kayıp anları **genişlet** |
| 3 | Modern aç | 19–21,24: Voss düello, dijital gerilim **sahne** ekle |
| 4 | Karakter aç | 17,18,22,23: iç dünya, ilişki, korku **derinleştir** |
| 5 | Antik aç | 01–04,09–13: yolculuk/inşa/mühür **ek sahne** |
| 6 | Enfeksiyon/ara | 15,16 + zayıf kısa bölümler: vignette **ekle** |
| 7 | Türetilmiş | metinler + EPUB; ses **yok** |
| → | 1’e dön | daha derin ikinci katman |

`phase_turns` 2–3 tur aynı phase’te kalabilir (büyütme yetersizse).

## 5. Tur protokolü

**A** turn+=1 · phase oku  
**B** P0: “hangi sahneleri **kaç paragraf** açacağım?” (max 5 dosya)  
**C** Yaz / genişlet (net +kelime)  
**D** `wc -w` kontrol — negatifse devam et  
**E** TTS senkron  
**F** STATE (kelime delta!) + LOG + commit + DUR  

### STATE alanları
`turn` `phase` `phase_turns` `next_chapters` `words_before` `words_after` `delta` skorlar `dna_ok` `last_commit` `notes`

## 6. Skor
`final_grounded` `action_balance` `prose_richness` (1–5; **prose_tight yerine prose_richness** — zenginlik)  
`length_ok`: true yalnızca `delta > 0`

## 7. Pusula
> Bu roman **novella’dan romana** giden yolda: daha çok **yaşanan an**, daha az **özet cümle**.  
> Kısaltmak kolay; **doğru yerde uzatmak** iş.

---

*Yazar düzeltmesi 2026-07-08: loop kısaltmayı bıraksın, uzatsın.*
