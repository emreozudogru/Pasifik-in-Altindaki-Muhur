# Pasifik’in Altındaki Mühür — Implementation Plan

**Tarih:** 2026-06-17  
**Dal:** main  
**Durum:** Design approved by user. Proceeding to expansion.

## Genel Yaklaşım

- Orijinal metin (`Pasifikin Altindaki Muhur.txt`) korunacak (baseline).
- Yeni versiyon `bolumler/` klasöründe 22 ayrı .md dosyası olarak geliştirilecek.
- Her bölüm ayrı commit + push yapılacak.
- Hedef uzunluk: 20.000 – 25.000+ kelime.
- Tüm genişletmeler tasarım spec’ine sadık kalacak.

## Bölüm Yapısı (22 Bölüm)

**Kısım I – Antik Mühür** (yaklaşık %42)
1. Prolog + Dünyanın Ucu (orijinal + genişletme)
2. İlk Savaş (En-Nakar’ın doğası)
3. Mühürcüler’in Toplanması (Eirene vurgusu)
4. En-Nakar’ın Yakalanması (yeni, epik sahne)
5. Yolculuk 1: Kara ve Nehirler
6. Yolculuk 2: Deniz ve Fırtınalar
7. Yolculuk 3: Son Yaklaşım ve Rüyalar
8. Kuroshima’ya Varış ve Hapishanenin İnşası
9. Mühürlerin Tartışması ve İnşası
10. Yedi Mühür (ritüel + Eirene’nin parmak izi)

**Kısım II – Unutma ve Kırılma** (%15)
11. Yüzyıllar Boyu Unutma (yoğun)
12. 1945 – Morita Genzo (büyük genişletme)
13. 1946-2010: Somut Enfeksiyon Örnekleri (3 yeni vaka)

**Kısım III – Keşif ve Dağılan Ağ** (%23)
14. Arakawa ve Ren’in Girişi
15. Arşiv’in Oluşumu
16. Dijital Çağ ve Şüphe
17. Voss ile İlk Karşılaşma (konferans)
18. Arşiv’in Parçalanması + Kerem’in Mesajı

**Kısım IV – Karşılaşma, Bedel ve Sekizinci Mühür** (%20)
19. Voss ile Çay Evi ve Teklif
20. Yalnız Kalan Ren + Annenin Bedeli
21. Son Yüzleşme
22. Sekizinci Mühür’ün Dağıtılması + Kapanış (Eirene’nin sorusu)

## Genişletme Öncelikleri

1. **Karakterler**
   - Ren: Annelik bağı + yalnızlık bedeli güçlendirilecek.
   - Eirene: Antik sahnelerde daha fazla yer.
   - Kerem: Daha sıcak, duygusal kayboluş.
   - Voss: 3 güçlü karşılaşma.

2. **Temalar**
   - AI ve dikkat ekonomisi detaylı işlenecek (Bölüm 4).
   - "Bedel her nesil sorar" modern bağlamda tekrarlanacak.
   - Sekizinci Mühür pratik kurallarla gösterilecek.

3. **Üslup**
   - Orijinal edebi ton korunacak.
   - Antik kısımlar daha epik ve ritmik.
   - Modern kısımlar daha kesik ve gerilimli.

4. **Yeni İçerikler**
   - En-Nakar yakalama sahnesi
   - Yolculukta kırılma anları
   - 1945 Morita gecesi genişletmesi
   - 3 modern enfeksiyon vakası
   - Ren’in annesi üzerinden bedel
   - Voss’un AI danışmanlığı ipuçları

## Uygulama Sırası (Önerilen)

**Aşama 1: Yapı ve Temel**
- bolumler/ klasörünü 22 dosya ile kur
- Orijinal metni ilgili bölümlere dağıt
- İlk commit’ler: Yapı

**Aşama 2: Antik Kısım (1-10)**
- En çok genişletme burada
- Önce 4,5,6,7,8,9,10 bölümleri derinleştir

**Aşama 3: Kırılma (11-13)**
- 1945 sahnesi kitaptaki en güçlü sahnelerden biri olacak

**Aşama 4: Modern (14-22)**
- AI teması entegre et
- Voss karşılaşmaları
- Final

**Aşama 5: Revizyon**
- Tüm dosyalarda motif tutarlılığı
- Üslup kontrolü
- Final polish

## Teknik Kurallar

- Her anlamlı değişiklik → ayrı commit + push
- Commit mesajları: `feat: 04 - En-Nakar’ın yakalanması genişletildi` gibi
- Orijinal .txt asla değiştirilmeyecek (sadece yeni versiyon)
- Tasarım spec’i referans alınacak

## Riskler ve Notlar

- Uzunluk kontrolü: 22 bölümde 20-25k kelime hedefi
- Felsefi denge: Voss’un argümanları güçlü kalacak, kolay zafer yok
- Duygusal zirve: Ren’in annesiyle vedalaşması ve final dağıtım

---

**Sonraki Adım:** bolumler/ klasör yapısını kur ve ilk bölümleri oluşturmaya başla.