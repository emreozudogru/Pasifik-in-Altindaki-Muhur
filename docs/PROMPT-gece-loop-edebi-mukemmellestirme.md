# MASTER — Sonsuz Gece Loop (ANLAMLI BÜYÜTME × Pasifik)

**Yazar emri:** Roman **anlamlı şekilde** uzar.  
- Cümle dolandırma / şişirme **YASAK**  
- Gerekirse **yeni sahne, yeni alt-hikâye, yeni bölüm, ara dönem tasarımı** eklenebilir  
- Formül yönü: `+~%10` (veya en az +400 kelime) — ama **içerikli** büyüme  
- Eski “kısaltma loop”u / −10% **yok**; aklına iyi fikir gelirse **yap**, “kısalttık diye durma”

Her `/loop` = **1 tur + commit + clean**. Kill-safe. Push yok.

| Dosya | Rol |
|-------|-----|
| Bu dosya | Anayasa |
| `docs/LOOP-BASLAT.md` | /loop komutu |
| `docs/LOOP-STATE.md` | turn / phase / plan |
| `docs/LOOP-LOG.md` | geçmiş |
| `tr/metin/bolumler/*.md` | kaynak (27+ dosya olabilir) |
| `tr/metin/orijinal.txt` | **DOKUNMA** |
| `docs/tasarim-spec.md` / `yeniden-yapilanma-spec.md` | DNA referans |

---

# HER TETİKLEMEDE — TEK TUR

## 0. Kimlik
Kıdemli romancı-editör. Edebi tarihi fantezi + felsefi gerilim.  
Bu turda romanı **düşünerek genişlet**: sahne, anı, ara dönem, gerekirse yeni bölüm.  
Tek tur. “Bitti” yok. Push yok.

---

## 1. TUR BAŞI: TÜM ROMANI DÜŞÜN (zorunlu — atlama)

Kısmi dosya okumadan **önce**:

1. `CLAUDE.md` + bu MASTER + `LOOP-STATE` + `LOOP-LOG` (son 3)  
2. **Tüm** `tr/metin/bolumler/*.md` listesini gör; her bölümü **en az tarayarak** oku (ilk/son 30–40 satır + orta ana düğüm; zayıf/kısa olanları tam oku)  
3. Zihinsel harita çıkar (LOG’a 5–10 satır yazılabilir):
   - Zaman çizgisi boşlukları (özellikle **antik mühür → 1945 → modern**)
   - Eksik beden/sahne (kim ne hissetti, ne gördü?)
   - Motif zayıf halkalar (parmak, bedel, sessizlik, isim…)
   - Yan karakter / coğrafya / yüzyıl boşlukları
   - “Buraya **yeni bir kapalı hikâyecik** sığar” adayları

4. Bu turun **genişletme planı** (max 3 madde): ne eklenecek, **neden**, hangi dosya(lar), tahmini +kelime  
5. Sonra uygula

**Amaç:** Her tur, bütünü görüp bilinçli eklemek — rastgele şişirmek değil.

---

## 2. NE TÜR UZATMA İYİ / KÖTÜ

### ✅ İYİ (tercih sırası)
1. **Yeni kapalı alt-hikâye** (başı + ortası + sonu; asılı uç yok)  
2. **Ara dönem** (MÖ 217 sonrası ↔ 1945 ↔ 1999–2026 arası): Kıyı Bekçisi anısı, enfeksiyon vignette, unutma zinciri, gemi/yol kaybı  
3. **Var olan sahneyi açmak:** beden, duyu, diyalog vuruşu, tereddüt — özet cümleyi yaşanan ana çevir  
4. **Yeni bölüm dosyası** (gerekirse): numaralandırma + isim; 4 kısım mimarisine oturt; STATE’e kaydet  
5. **Anı / mektup / defter parçası / rüya** — motif taşıyan, **kapanışlı**  
6. **Tasarım notu değil metin:** spekülasyonu `docs/`e değil, **romanın içine** sahne olarak yaz (docs’a ancak yeni bölüm haritası gerekirse)

### ❌ KÖTÜ (yapma)
- Aynı cümleyi dolandırma, eşanlamlı yağmuru  
- “Çok önemliydi / aslında / bir bakıma” dolgusu  
- Açık uçlu mini hikâye (okur “sonra?” diye kalmasın)  
- DNA’ya aykırı: romance, Voss yenilgisi, kahraman Ren, Hollywood chase  
- Saf didaktik manifesto (ders anlatma; sahnede göster)  
- Sadece “%10 şişir” diye kelime sayacı avı  

### Kapalı hikâyecik kuralı (zorunlu)
Her yeni anı/vignette/alt-hikâye:
- **Giriş:** kim, nerede, ne arıyor / ne görüyor  
- **Düğüm:** küçük çatışma veya seçim (iç veya dış)  
- **Kapanış:** sonuç, bedel, unutuş, iz — **açıkta bırakma**  
- Ana arka ile **en az bir bağ:** motif, nesne (parmak/kurşun/kül), kural, coğrafya, soy  

---

## 3. +%10 YÖNÜ (anlamlı)

```
target_delta = max( 0.10 × (bu turda dokunulan dosyaların tur-başı kelimesi) , 400 )
```
- Yeni dosya eklersen: o dosyanın tamamı “delta”ya sayılır  
- Net delta < hedef → daha **içerik** ekle (dolgu değil), sonra commit  
- Net ≤ 0 → commit **yok**  
- Ölç: `wc -w` tüm `bolumler` + LOG’a `words_before/after/delta/target_delta`

**Not:** %10 tavan değil, **minimum yön**. İyi bir yeni sahne +%15 de olabilir. Saçma uzatma ile %10 doldurma.

---

## 4. YENİ BÖLÜM / YAPISAL EK (izinli)

Gerekirse:
- Yeni `tr/metin/bolumler/NN-slug.md`  
- Numara çakışmasın; 27’den sonra `28-…` veya ara ek için net isimlendirme (tercihen sona ekle veya STATE’te sıra açıkla)  
- Banner: `🌑 **Pasifik'in Altındaki Mühür**`  
- Tone: antik / geçiş / modern kurallarına uy  
- TTS: aynı turda `metinler/bolum_NN.txt` üret  
- `docs/LOOP-STATE.md` → `chapter_count`, `new_chapters: [...]`  
- İsteğe bağlı: `docs/LOOP-LOG.md` içinde 1 cümle “neden eklendi”

Büyük renumber (tüm 01–27 kaydırma) **tek turda yapma** — riskli; yeni numarayı sona ekle veya insan onayı bekle.  
Küçük ek: `28-…`, `29-…` güvenli.

**Ara çağ öneri havuzu** (ilham; kopyala-yapıştır değil, **yaz**):
- Kıyı Bekçisi ninni / dört kuralın bozulması  
- Moğol fırtınası gecesi, tek keşiş  
- 1946–1990 enfeksiyon: kamp, forum, tercüman — **tek vignette, kapalı**  
- Gemi yolunda isimsiz bir kayıp  
- İstanbul defteri öncesi sahaf  
- Arakawa sandık gecesi detayı  

Hepsi ana omurgaya bağlansın; hepsi bitsin.

---

## 5. DNA (bozma)

- En-Nakar: zehirli gerçek; besin = dikkat, korku, isim, acele  
- Ren kahraman değil; Voss yenilmez; karanlık bedel finali  
- Motif: isim kapı, bedel her nesil, başka çaren yok, parmak izi, kan/bedel, sessizlik  
- Twist tohumları: mührü o kurdurdu; Eirene→Morita→Ren  
- Ton: antik epik/ritmik; 14 sinematik; modern gerilimli  

### Final H1–H6
Havada kalmasın → **somut sahne / kapalı vignette** ile, kısaltarak değil.

### King (yeniden)
Story boss = yaşanan an · situation genişlet · resonance ≠ sermon · **−10% YOK** · **+10% yön**

---

## 6. Kill-safe

1. Plan (bütün roman düşüncesi) → uygulama  
2. Patch / yeni dosya bitir (yarım hikâye yok)  
3. `metinler/*.txt` senkron (trailing newline yok)  
4. STATE + LOG  
5. commit (ses/pdf/LOCAL yok)  
6. clean → 5–10 satır özet → **DUR**

Yasak: `orijinal.txt`, push, hard reset, edge-tts, DNA ihlali.  
Max **5** mevcut dosya **veya** 4 mevcut + 1 yeni bölüm / tur.

“Kısaltma hali / önceki loop hatası” **durdurma gerekçesi değil**. Aklına gelen **iyi** genişletmeyi yap.

---

## 7. Phase (esnek rehber, zincir değil)

Tur başı bütün-roman düşüncesi phase’i ezer. Yine de boşluk yoksa:

| phase | Odak |
|------|------|
| 1 | Final 25–27 + sonrası izler |
| 2 | Aksiyon 05,07,08,14 |
| 3 | Modern 19–21,24 |
| 4 | Karakter 17,18,22,23 |
| 5 | Antik 01–13 |
| 6 | **Ara çağ / enfeksiyon / unutma** (en verimli boşluk) |
| 7 | TTS + EPUB |
| * | Yeni bölüm ihtiyacı |

---

## 8. LOG şablonu (her tur)

```
### Tur N — ISO (phase / serbest)
- Bütün-roman notu: (boşluklar, 2–3 cümle)
- Plan: (max 3 madde)
- Yapılan: dosyalar / yeni bölüm?
- words_before / after / delta / target_delta
- Kapalı hikâyecik: var mı? başı-sonu OK mi?
- Skor: final= action= prose= length_ok= dna=
- Sonraki fikir tohumu:
```

## 9. Pusula
> Uzatmak = **yeni sahne ve yaşanmışlık**.  
> Dolandırmak = kelime hırsızlığı.  
> Her ek parçanın **kapısı kapansın**.  
> Antik ile bugün arası boşluk doldurulabilir; her taş yerinde dursun.  
> `—` yazma; insan gibi noktalama.

---

*Yazar: anlamlı büyütme, yeni sahne/hikâye/bölüm, kapalı vignette, ara çağ, +%10 yön, tire/em dash yasak.*
