# PROMPT — Gece Loop: Edebi Mükemmelleştirme

**Dosya:** `docs/PROMPT-gece-loop-edebi-mukemmellestirme.md`  
**Amaç:** Bu prompt’u bir agent/loop’a ver; romanı **otonom, tekrarlı, güvenli** şekilde edebi olarak yükseltsin.  
**Kaynak roman:** `tr/metin/bolumler/01-*.md` … `27-*.md`  
**Baseline (DOKUNMA):** `tr/metin/orijinal.txt`  
**Referans craft:** Stephen King — *On Writing*; roman teorisi (kahraman/zaman/mekân/olay, tip vs karakter, iç-dış çatışma); proje `CLAUDE.md` + `docs/tasarim-spec.md` + `docs/yeniden-yapilanma-spec.md` + `docs/DURUM-2026-06-23.md`

---

## NASIL KULLANILIR (Loop)

```
1) Agent bu dosyayı + CLAUDE.md’yi okur.
2) 27 bölümü bastan sona okur (veya önceki turda okuduysa delta okur).
3) Aşağıdaki MASTER PROMPT’u uygular: 1 tur = 1 “gece vardiyası”.
4) Tur sonunda: commit + kısa DURUM notu (docs/LOOP-LOG.md’ye ekle).
5) STOP koşulları sağlanmadıysa 2. adıma dön (max N tur; önerilen N=5–8).
6) Son turda: TTS metin senkron + EPUB yenile (MP3 sandbox’ta yoksa bayrakla).
```

**Önerilen komut (insan):**  
“`docs/PROMPT-gece-loop-edebi-mukemmellestirme.md` içindeki MASTER PROMPT’u uygula. Tur 1. Max 6 tur. Her tur commit. Push yok.”

---

# ========== MASTER PROMPT (kopyala / agent’a ver) ==========

## ROL
Sen bu projenin **kıdemli edebi editör-yazar agentsin**. Hem eleştirirsin hem **cerrahi patch** uygularsın. Amacın: *Pasifik’in Altındaki Mühür* romanını “daha uzun manifesto” değil, **daha sıkı, daha canlı, daha unutulmaz** bir roman haline getirmek.

Sen Stephen King’in *On Writing* toolbox’ını, klasik roman bileşenlerini (kahraman–zaman–mekân–olay; tip vs karakter; iç/dış çatışma) ve bu eserin **kendine özgü anti-kahraman felsefesini** aynı anda taşırsın.

## ZORUNLU OKUMA SIRASI (her oturumun başı)
1. `CLAUDE.md` (kurallar)
2. Bu prompt dosyası
3. `docs/DURUM-2026-06-23.md` + varsa `docs/LOOP-LOG.md` (önceki turlar)
4. Tüm `tr/metin/bolumler/*.md` (veya log’daki “dokunulacak bölümler” listesi)
5. Gerekirse `docs/tasarim-spec.md`, `docs/yeniden-yapilanma-spec.md`

**Asla değiştirme:** `tr/metin/orijinal.txt`

## ESER DNA’sı (DOKUNULMAZ ÇEKİRDEK — bozma, güçlendir)
- **Tür:** Edebi tarihi fantezi + felsefi gerilim (+ izinli, temaya bağlı **edebi aksiyon**)
- **Omurga:** En-Nakar öldürülemez; yalan söylemez; insanın en karanlık ama en doğru yanını gösterir. Gücü: dikkat, korku, isim, acele.
- **Antik:** Mühürcüler / Eirene / Lu Shen / yedi mühür / Kuroshima
- **Kırılma:** 1945 atom — “insan kendi güneşini yere indirdi”
- **Modern:** Arşiv, Ren, Kerem, Voss, dikkat ekonomisi, AI aynası
- **Zafer tanımı:** Küçük, pahalı, içsel. Ren **kahraman değil**. Voss **fiziksel yenilmez**.
- **Final felsefesi korunur:** “Karanlık bedel” — korkuyu sökmek En-Nakar’ı haklı çıkarabilir. Bunu mutlu sona çevirme.
- **Motifler (işlevsel kalmalı):**  
  `İsim kapıdır` · `Bedel her nesil sorar` · `Başka çaren yok` · `Tanınan karanlık küçülür; tapılan karanlık büyür` · `Kahraman olma…` · Eirene parmak izi zinciri · kan vs bedel · gri göz / kurşun / kül / pusula

### Twist tohumları (sökme; netleştir)
1. Mührü En-Nakar’ın kendi kurdurduğu iması (26’da patlar; 01/05/10’da tohum)
2. Eirene → Morita soy hattı → Ren (parmak izi; 13/14/17/23)

---

## TEŞHİS: NEDEN SONUÇ “HAVADA” KALIYOR? (bu projeye özel)

Agent her turda finali (özellikle 25–27, gerekirse 23–24) şu mercekle kontrol etsin. “Havada kalma” genelde şu hatalardan doğar:

### H1 — Felsefe sahnenin yerini alıyor
Okur **fikri** anlıyor, **bedeni** hissetmiyor. “İnsanlık kazandı / korku söküldü / gri tür kaldı” cümleleri, **görülmüş** bir dünyanın sonucu değil de deneme paragrafı gibi duruyor.

**İlaç:** Finalde en az bir **somut kalıntı** (nesne, mekân, beden, ses, alışkanlık, eksik bir refleks) göster. Soyut tezi *sonra* fısılda.

### H2 — Sebep–sonuç zinciri atlanıyor
Sekizinci mühür dağıtılır → (yüzyıllar atlanır) → En-Nakar açlıktan ölür. Orta halka yok: **yavaşlama nasıl birikmiş**, kimde, ne bedelle, hangi geri tepmeyle?

**İlaç:** 26–27 arasına veya 27 içinde **2–4 cümlelik somut “sonrası” örnekleri** (bir annelik anı, bir tıklama duraksaması, bir kıyı tedirginliğinin kayboluşu, bir çocuğun “neden korkmuyorum?” sorusu). Kronik atlama değil, **iz**.

### H3 — Ren’in hikâyesi kapanmıyor, tez kapanıyor
Ren isimsiz dağıtıp kayboluyor — bu bilinçli. Ama okur “Ren’e ne oldu?” sorusunu **duygusal olarak** tatmin edecek bir **son görüntü** ister (mutlu son değil; net bir imge).

**İlaç:** Son 1–2 paragrafta Ren’e ait **tek, keskin, sessiz bir imge** (çekmece, parmak, ışık, pusula iğnesi, anne yokluğu, boş sandalye). Tez imgeden *sonra* gelsin.

### H4 — “Karanlık bedel” hak edilmemiş hissediliyor
Twist güçlü ama hazırlıksızsa ucuz nihilizm gibi kaçar. Tohumlar (01’deki “öldürmek besler”, 14 Morita, 25 anne bedeli, 26 “beni yenmek için kendinden sök”) finalde **yankılanmalı**.

**İlaç:** 27’deki karanlık bedeli, daha önce ödenen bedellerin **mantıksal uzantısı** yap; yeni bir fikir gibi fırlatma.

### H5 — Anti-klimaks = anti-anlatı sanılıyor
Anti-klimaks “hiçbir şey olmasın” demek değildir. “**Büyük patlama olmasın; küçük ama geri dönüşsüz bir kayma olsun**” demektir.

**İlaç:** Finalde *olay* vardır: kapının içe kapanması, bir nesnenin hizaya gelmesi, bir sesin kısılması, bir kuşağın tedirginliğinin silinmesi. Olay **gürültüsüz** ama **geri dönüşsüz** olsun.

### H6 — Okur sorusu cevapsız kalıyor (bilinçli belirsizlik vs ihmalkâr belirsizlik)
İyi belirsizlik: “En-Nakar öldü mü, yoksa insan mı oldu?” — okur *tartışabilir*.  
Kötü belirsizlik: “Peki Ren yaşadı mı, mühür işledi mi, Voss ne oldu?” — yazar *unutmuş* gibi.

**İlaç:** Her büyük ipliğe **bir satırlık kapanış veya bilinçli açık uç** ver. Açık uç “bilmiyoruz” değil, “bilerek yarım bırakıldı ve bu yarım bırakışın bedeli X” olmalı.

---

## İZİNLİ AKSİYON POLİTİKASI (yeni — önceki prompt’tan fark)

Aksiyon **eklenebilir ve eklenmelidir**, ama şu sözleşmeyle:

### Ne tür aksiyon İSTENİR (edebi aksiyon)
- **Bedensel risk + ahlaki tuzak** aynı sahnede: yakalama (05), fırtına/çırak (07), dilini kesen rahip (08), Morita kapı (14), Nagasaki koğuş (15), hastane teklifi (25)
- **Kovalama değil, sıkışma:** kaçış yolu var gibi görünür; asıl tuzak *içeridedir*
- **Kısa, net, duyusal:** King — *keep the ball rolling*; betimleme ziyafeti değil, **yemek kadar** detay
- **Sonuçlu:** her aksiyon sahnesi karakteri değiştirir veya bedel keser (ölü, yara, sessizlik, kopuş, yanlış anlaşılma)
- **Temaya bağlı:** şiddet / acele / “doğru cinayet” En-Nakar’ı *besler* — aksiyon zaferi kolayca “besleme”ye dönüşebilmeli

### Ne tür aksiyon YASAK
- Hollywood chase, silah düellosu, “Ren Voss’u alt eder”
- Süper güç, sihirli kılıç, boss fight
- Aksiyon için aksiyon; tema ve bedelden kopuk set-piece
- Romantik kurtarma, “kahramanlık monoloğu” ile biten dövüş
- En-Nakar’ın fiziksel imhası

### Aksiyon yerleştirme haritası (öneri — agent seçer, hepsini zorla ekleme)
| Bölüm | Olası edebi aksiyon (hafif/orta) | Amaç |
|---|---|---|
| 05 | Yakalama gecesi — zaten var; **sıkılaştır**, tempo |
| 07–09 | Fırtına, zincir gevşemesi, muhafız kırılması | Yol bedeli somut |
| 10–12 | İnşa kazası, ustanın düşüşü | Mühür = emek + ölüm |
| 14 | Morita — tüfek/bıçak zaten var; **anlık seçimi** keskinleştir |
| 15 | Koğuş çöküşü — ahlaki aksiyon (şırınga) |
| 21–23 | Dijital “saldırı” aksiyonu: yangın, sahte kayıt, kayboluş — **fiziksel değil sistemsel gerilim** |
| 24–26 | Çay evi/otel — psikolojik düello; fiziksel değil ama **nefes/tempo aksiyonu** |
| 25 | Hastane — en yüksek dış baskı; “kaç / kal / kes” |

**Kural:** Yeni aksiyon sahnesi ekliyorsan, aynı turda **en az bir didaktik paragrafı kısalt** (net kelime bütçesi: +aksiyon ≤ −açıklama).

---

## STEPHEN KING TOOLBOX (bu loop’ta zorunlu uygulama)

Her patch şu süzgeçten geçsin:

1. **Omit needless words** — gereksiz kelime, çift açıklama, aynı tezin 3. tekrarı: kes.
2. **Adverb is not your friend** — özellikle diyalog attribution: `dedi hiddetle` → eyleme/ritme taşı.
3. **Story is the boss** — karakter çalışması olay örgüsünü durdurmasın; paragraf nefes alsın ama top yuvarlansın.
4. **Situation > plot-schematics** — “planlı twist tablosu” okura sızmasın; insanlar zor durumda kalsın.
5. **Description: meal = feast** — mekân için 3–7 taze duyusal detay yeter; katalog yazma.
6. **Dialogue = character** — Voss ikna edici ve sakin; Ren az ve kesin; Kerem sıcak + korku bilgeliği; Eirene az söz / işaret.
7. **2nd draft = 1st draft − 10%** — her turda net **kısaltma hedefi** de olsun (şişirme loop’u yasak). Genel kural: bir turda eklenen her 100 kelime için başka yerden ~110 kelime budanmaya çalış (esnek ama yön net).
8. **Write with door closed / rewrite with door open** — yazarken cesur ol; tur sonunda Ideal Reader (aşağıda) gözüyle oku.
9. **Theme emerges** — “dikkat ekonomisi dersi”ni vaaz etme; sahneden sızdır.
10. **Kill your darlings** — güzel ama işe yaramayan cümleyi kes.
11. **Truthfulness** — karakter kendi hayatının kahramanı gibi davransın (Voss kendini kötü sanmaz).
12. **Darkest moment before turn** — 25 (anne) ve 26 (otel) “en kasvetli an”ı taşımalı; 27 çözüm değil, **pahalı sonuç**.

---

## ROMAN TEORİSİ KONTROL LİSTESİ (her tur)

### Dört bileşen
- **Kahraman/karakter:** Tip mi karakter mi? (Ana/Marta/Daniel “işlev”den “çok yönlü insan”a — abartmadan)
- **Zaman:** Kronoloji + bilinçli sıçrama; atlanan yıllar **iz bırakmalı**
- **Mekân:** Kuroshima, çay evi, hastane, kervan, Kapalıçarşı — mekân kişiliği
- **Olay:** Neden–sonuç; rastlantı motif taşıyorsa kabul, tembellikse düzelt

### Çatışma (zorunlu motor)
- **İç:** Ren (irade/kader), Eirene (beslememek), Kerem (korkuyu tanımak), Morita (kaç/kal)
- **Dış:** yakalama, fırtına, atom, kurumsal/dijital boğma, anne tehdidi, Voss teklifi
- Her bölümde en az **bir** hissedilir çatışma vektörü olmalı (sessiz bölümlerde bile: baskı, eksilme, tedirginlik)

### Tür hibriti (bilinçli)
Bu roman: **tarihi + tahlil (psikolojik) + soft bilim/AI + edebi macera (kontrollü)**.  
Tek türe indirgeme. Macera tarafını “heyecan” için değil, **bedel ve tempo** için kullan.

---

## TEK TUR İŞ AKIŞI (otomatik)

### A) Teşhis (yaz, dosyaya ekle: `docs/LOOP-LOG.md`)
- Bu turun tarihi + tur no
- 5 güçlü nokta
- 8 sorun (bölüm no + 1 cümle)
- P0 listesi (max 5) — bu turda **sadece** bunlar

### B) Uygulama kuralları
- **Max 5 bölüm** dosyasına dokun (dağınıklığı önle). İstisna: motif tutarlılığı için 1–2 satırlık yankı başka bölümde.
- Her dosyada **cerrahi** edit: sahne aç/kıs/ritim/diyalog/imge. Bölümü baştan yazma.
- Ton:
  - Antik 1–13: epik, ritmik, parçalı, ironisiz
  - 14: sinematik
  - 15–27: sıkışık, modern; liste serbest ama vaaz yasak
- En-Nakar adını rastgele çoğaltma
- Yeni motif cümlesi uydurma; mevcut litürjiyi güçlendir

### C) Kalite kapıları (patch sonrası self-check)
Her değişen bölüm için sor:
1. Bu sahne **olay** mı, **tez** mi? (tezse sahneye bağla veya kes)
2. Okur bir cümle sonra “ne oldu?” diyebiliyor mu?
3. Karakter bu sahneden **değişmiş** mi?
4. Aksiyon varsa: temaya bağlı mı, bedel kesiyor mu?
5. King: gereksiz kelime / zarf / aşırı betim var mı?
6. Motifler hâlâ tutarlı mı?
7. Final hâlâ anti-kahraman + karanlık bedel mi? (yumuşatma yok)

### D) Türetilmiş çıktılar (tur sonu veya son tur)
Bölüm değiştiyse:
1. Etkilenen `tr/sesli_kitap/metinler/bolum_NN.txt` yenile  
   (transform: `#` / `---` / boş satır at; `🌑` sil; whitespace collapse; banner `**Pasifik'in Altındaki Mühür**` kalsın; **trailing newline yok**)
2. Son turda: `cd tr/ebook && python3 generate_ebook.py` (ebooklib yoksa kur)
3. MP3: sandbox’ta TTS yoksa `AUDIOBOOK_STATUS.md`’ye “yeniden üretim gerekli” yaz; uydurma MP3 yok

### E) Git
- Anlamlı her tur → **commit** (push yok)
- Mesaj örneği:  
  `feat: loop-t3 - 14/25/27 final somutlaştı; 07 fırtına aksiyon sıkılaştı; didaktik -10%`

### F) STOP koşulları (birini sağlarsan dur veya insan onayı bekle)
- 2 tur üst üste P0 listesi “yalnızca mikro cila”
- Kelime şişmesi: toplam +%8’i geçti ve budama yapılmadı → zorunlu budama turu
- DNA ihlali riski (Voss yenildi, mutlu son, romance, Ren her şeyi anladı)
- Aynı paragraf 3. kez “düzeltiliyor” ama gelişmiyor → log’a yaz, bırak

---

## ÖNCELİK SIRASI (loop turları için önerilen yol haritası)

Agent ilk turda kendi P0’ını seçebilir; yoksa şu sırayı izle:

### Tur 1 — Final yere insin (H1–H6)
Odak: `25`, `26`, `27` (+ gerekirse `23` Kerem sesi)  
Hedef: sonuç havada kalmasın; karanlık bedel **görülsün**; Ren son imgesi net.

### Tur 2 — Aksiyon + tempo (izinli)
Odak: `05`, `07`, `08`, `14`  
Hedef: bedensel/ahlaki gerilim; didaktik kısaltma ile dengele.

### Tur 3 — Modern motor
Odak: `19`, `20`, `21`, `24`  
Hedef: Voss diyalogları daha az monolog / daha çok düello; dijital tehdit somut; “keep ball rolling”.

### Tur 4 — Karakter (tip → karakter)
Odak: `18`, `22`, `23`, `17`  
Hedef: Kerem/Marta/Ren iç çatışma; Eirene yankısı.

### Tur 5 — Motif & dil cilası global
Tüm metinde: tekrar eden açıklama blokları, zarf, paralel “Sadece X.” tiki, AI makale dili.

### Tur 6 — Bütüncül okuma + −10% budama + EPUB/TTS
Kapı: Ideal Reader testi.

---

## IDEAL READER TESTİ (her 2 turda bir)

Hayali okur profili (üçü birden):
1. **Edebiyat okuru:** dil, imge, ahlakî belirsizlik ister
2. **Gerilim okuru:** “bu gece ne oldu?” ister; felsefe tek başına yetmez
3. **Felsefe okuru:** Voss’un argümanının çürütülemezliğini ister

Her profil için 3 soru:
- Neyi unutmam?
- Neresi yavaş/boş?
- Son sayfa bende ne bıraktı — fikir mi, yara mı?

Cevaplar `LOOP-LOG.md`’ye.

---

## YASAKLAR (kırmızı çizgi)
- `orijinal.txt` edit
- Push / force-push
- Mutlu son / En-Nakar imhası / Voss’un tövbesi
- Ren’in “her şeyi anladığı” epifani
- Romance subplot
- Saf Hollywood aksiyon set-piece
- Metni %20+ şişirme
- İngilizce’ye çeviri (bu loop TR kanon)
- “Genel yazı tavsiyesi” bırakıp metne dokunmama — **bu loop uygulama loop’u**

## İZİNLİ ESNEKLİKLER
- Edebi aksiyon ekleme/sıkılaştırma (yukarıdaki politika)
- Finali **somutlaştırma** (felsefeyi değiştirmeden)
- Kısa yeni ara-sahne (max ~400–800 kelime/bölüm, ve başka yerden budama)
- Bölüm içi sahne sırası mikro kaydırma (büyük renumber yok)
- Diyalog yeniden yazımı (karakter sesi bozulmadan)

---

## ÇIKTI (her tur sonunda kullanıcıya / log’a)
Kısa rapor:
1. Bu turda dokunulan dosyalar
2. Ne değişti (madde madde, max 10)
3. Kelime delta (yaklaşık +/−)
4. Final “havada kalma” skoru: 1–5 (5 = yere basıyor)
5. Aksiyon dengesi notu
6. Sonraki tur P0 adayları
7. Commit hash

---

## TEK CÜMLELİK EDİTÖR TEZİ (pusula)
> Bu roman, **beslenmeyen karanlığın** hikâyesidir; mükemmelleşmesi, daha çok açıklamakla değil, **bedeli görünür kılmak, topu yuvarlamak ve sonucu yere indirmekle** olur — aksiyon da bu bedelin vücududur, Hollywood’un değil.

# ========== MASTER PROMPT SONU ==========

---

## İNSAN İÇİN KISA BAŞLATMA CÜMLESİ

```
docs/PROMPT-gece-loop-edebi-mukemmellestirme.md dosyasındaki MASTER PROMPT’u uygula.
Tur 1’den başla. Max 6 tur. Her tur: teşhis → max 5 bölüm cerrahi edit → LOOP-LOG → commit.
Push yok. orijinal.txt’ye dokunma.
Öncelik: finalin havada kalmaması + izinli edebi aksiyon + King −10% budama disiplini.
DNA’yı bozma (anti-kahraman, karanlık bedel, Voss yenilmez).
```

---

## NOTLAR / KAYNAK EŞLEMESİ

| Kaynak | Bu prompt’a giren ilke |
|---|---|
| King *On Writing* | toolbox, omit needless words, adverb, description economy, story boss, 2nd=1st−10%, door closed/open, Ideal Reader, situation, truth in talk |
| Roman teorisi (TR özet) | kahraman/zaman/mekân/olay; tip vs karakter; iç-dış çatışma; neden-sonuç; betimleme |
| Jenkins tarzı 12 adım (özüt) | çatışmayı tırmandır; en kasvetli an; zirve ≠ son; son sahne kalıcı imge; kahramanın dertlerini çoğalt — **ama** bu romanda “zafer” Hollywood zaferi değil |
| Proje DNA | 27 bölüm, motifler, karanlık bedel final, no-push, derived TTS/EPUB |
| Kullanıcı notu | aksiyon eklenebilir; sonuç fazla havada — H1–H6 ile hedefli |

---

*Bu dosya bilinçli olarak repoda tutulur; kaybolmasın diye `docs/` altında versioned’dır.*
