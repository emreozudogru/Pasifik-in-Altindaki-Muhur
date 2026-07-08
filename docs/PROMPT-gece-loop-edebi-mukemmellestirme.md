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
1. **Yeni sahne** (mevcut bölüm içine: mekân, beden, diyalog, sonuç; tam sahne)  
2. **Yeni kapalı alt-hikâye** (başı + ortası + sonu; asılı uç yok)  
3. **Ara dönem** (antik ile 1945 ile modern arası): bekçi anısı, enfeksiyon, unutma, yol kaybı  
4. **Var olan sahneyi açmak:** beden, duyu, diyalog, tereddüt (özeti yaşanan ana çevir)  
5. **Yeni bölüm dosyası** (gerekirse): `28-…` vb.; 4 kısım mimarisine oturt; STATE’e kaydet  
6. **Anı / mektup / defter / rüya:** motifli ve **kapanışlı**  
7. Metni `docs/`e değil **romana** yaz  

### ❌ KÖTÜ (yapma)
- Aynı cümleyi dolandırma, eşanlamlı yağmuru  
- “Çok önemliydi / aslında / bir bakıma” dolgusu  
- Açık uçlu mini hikâye  
- DNA’ya aykırı: romance, Voss yenilgisi, kahraman Ren, Hollywood chase  
- Saf didaktik manifesto  
- Sadece “%10 şişir” kelime avı  
- **Uzun tire / em dash `—` ve `–`:** AI kokusu; klasik romanda neredeyse yok. **Yeni metinde kullanma.**  

### Noktalama (Türkçe roman sesi)
- Nokta, virgül, noktalı virgül, soru, tırnak  
- Ara söz: virgül veya **ayrı cümle** (tire yığını yok)  
- Diyalog: tırnak; `dedi` sade  
- **Yeni yazdığın her pasajda `—` / `–` yasak**  
- Eski metindeki tireleri bu turda zorla silme zorunluluğu yok; dokunduğun dosyada istersen virgül/noktaya çevir (net +kelime bozulmasın)

### Yan hikâye / vignette: iki geçerli biçim

Roman **tek vuruşta kapanan** parçalar da ister, **bölümler arası dans eden** yan ipler de. İkisi de iyi; ikincisi çoğu zaman daha edebi.

#### A) Tek bölümde kapalı vignette
Aynı dosyada:
- Giriş (kim, nerede)  
- Düğüm (seçim / gerilim)  
- Kapanış (sonuç, bedel, iz)  
Okur o bölüm bitince “sonra?” diye asılı kalmaz.

#### B) Tohum → dans → bağ (çok bölümlü yan iplik) — **tercih edilebilir**
1. **Tohum (bölüm N):** Küçük hikâye **başlar**. Tam ana arka ile “açıkla”mak zorunda değil. Merak, imge, isim, nesne, ses bırak.  
2. **Dans (N…M arası, isteğe bağlı):** Yan ip ara sıra görünür; ana çizgiyle **ritim tutar** (aynı motif, zıt seçim, yankı) ama henüz çözülmez.  
3. **Bağ / kapanış (bölüm M veya sonrası):** Ana hikâye ile **net bağlanır** (nesne, soy, karar, tekrarlanan cümle, aynı kıyı, aynı iz). Okur “aa, o buydu” der. Yan ip **mutlaka bir yerde kapanır veya ana omurgaya oturur.**

**Örnek mantık (uydurma şablon, kopyalama):**  
Ch.13’te bir keşiş pencereyi kapatır (tohum). Ch.14 Morita aynı tedirginliği hisseder (dans). Ch.25 Ren “cevap verme”yi hatırlar / aynı soydan iz (bağ).

#### C) Yasak olan “açık”
- Tohum atıp **hiç planlamadan** unutmak  
- Sonsuza açık uç (“belki bir gün…” ve bir daha yok)  
- Yan ipin ana DNA ile **hiç** ilişkisi olmaması  

#### D) STATE takibi (zorunlu, B tipi için)
`LOOP-STATE.md` içinde `open_threads:` listesi tut:

```yaml
open_threads:
  - id: keşiş-pencere
    planted: "13"
    status: open   # open | dancing | closed
    payoff_target: "14 veya 25-27"
    hook: "pencere/örtü, denize bakmama, abinin sesi yalanı"
```

- Yeni tohum = `open` ekle  
- Dans sahnesi = `dancing`  
- Bağ = `closed` + hangi bölümde kapandığı  
- Tur başı: açık ipleri oku; uygunsa **bu turda bağla veya dans ettir**; açık ipler birikmesin (tercihen ≤ 5 açık)

#### E) Bu turda ne seçilir?
- Bütün-roman düşüncesinde: “tohum mu, dans mı, bağ mı, tek vuruş mu?” planla  
- Açık ip varsa ve payoff yeri geldiyse: **bağ öncelikli** (yarım bırakma disiplini)  
- Yeni tohum atarken: en az bir cümleyle “nerede bağlanabilir” STATE’e yaz  

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
> Yan ip **dans edebilir**; ama bir yerde **ana hikâyeye bağlansın**.  
> Tek vuruş da olur, tohum-bağ da olur; unutulmuş açık uç olmaz.  
> `—` yazma; insan gibi noktalama.

---

*Yazar: anlamlı büyütme; yeni sahne; tohum→dans→bağ yan iplik; kapalı vignette; ara çağ; +%10; tire yasak.*
