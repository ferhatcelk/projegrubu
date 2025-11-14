# Hava Durumu Veri Analizi Projesi (Münih, 2024)
Bu proje, bir hava durumu veri setini kullanarak kısa vadeli mevsimsel kalıpları, yağış eğilimlerini ve aykırı hava olaylarını incelemek amacıyla hazırlanmıştır.

⚠️ Veri Seti ve Kısıtlamalar
Bu analiz, talep edilen 10 yıllık İstanbul verisi yerine, Münih şehrine ait 2024 yılının Mart-Temmuz ayları arasındaki kısıtlı bir veri seti (munich.csv) kullanılarak yapılmıştır.
- Zaman Aralığı: 5 aylık kısa bir dönemi kapsar. Uzun vadeli iklimsel trendler (10 yıl) incelenememiştir.
- Metrikler: Sadece Yağış (mm) ve Kar (cm) verisi mevcuttur. Sıcaklık trendleri analiz edilememiştir.

🛠️ Kullanılan Kütüphaneler
- Pandas: Veri manipülasyonu ve EDA.
- NumPy: Sayısal hesaplamalar.
- Matplotlib: Veri görselleştirme.

📊 Analiz Bulguları ve Görselleştirme
1. Aylık Mevsimsel Kalıplar
   - Analiz sonuçlarına göre 2024 yılındaki en yağışlı dönem Mayıs-Haziran aylarıdır. Kar yağışı ise yalnızca Mart ve Nisan aylarında çok düşük miktarlarda gözlemlenmiştir.
   - Grafik, aylık toplam Yağış ve Kar yağışının dağılımını net bir şekilde göstermektedir.

### 3 yıllık yağış miktarı

![Yağışı Kalıpları Grafiği](https://raw.githubusercontent.com/ferhatcelk/projegrubu/5a9be05f74acd9b439574a8cc753f13475a74537/3_yillik_yagis_miktari.png)