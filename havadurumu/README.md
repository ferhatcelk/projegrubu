# ☁️ Hava Durumu Veri Analizi Projesi (Münih, 2024)

Bu proje, bir hava durumu veri setini kullanarak mevsimsel kalıpları, yağış eğilimlerini ve aykırı hava olaylarını incelemek amacıyla hazırlanmıştır.

---



Belirlenen bir bölgenin günlük hava durumu verilerini (yağış ve kar) analiz ederek **kısa vadeli mevsimsel kalıpları** ve **aşırı hava olaylarını** tespit etmek ve bu bulgular ışığında bir rapor sunmaktır.

---

## ⚠️ Veri Seti ve Kısıtlamalar

Bu analiz, orijinal talepte belirtilen $10$ yıllık İstanbul verisi yerine, **Münih** şehrine ait, **2024 yılının Mart-Temmuz** ayları arasını kapsayan kısıtlı bir veri seti ($`munich.csv`$) kullanılarak yapılmıştır.

| Özellik | Veri Kapsamı | Kısıtlama |
| :--- | :--- | :--- |
| **Coğrafya** | Münih (Almanya) | İstanbul analizi yapılamamıştır. |
| **Zaman Aralığı** | 2024 (5 Ay) | Uzun vadeli iklimsel trendler (`10 yıl`) incelenememiştir. |
| **Metrikler** | Yağış ve Kar | Sıcaklık verisi (`Max/Min Sıcaklık`) eksiktir. |

---

## 🛠️ Kullanılan Kütüphaneler

* **`Pandas`**: Veri yükleme, temizleme, hazırlık ve analiz işlemleri için.
* **`NumPy`**: Sayısal işlemler ve temel istatistikler için.
* **`Matplotlib`**: Veri görselleştirmesi (grafikler) için.

---

## 📊 Analiz Aşamaları

Proje, dört ana aşamada ilerlemiştir:

1.  **Veri Yükleme ve Hazırlık:** `$munich.csv$` dosyası ``;`$` ayırıcı ile yüklendi, `$Tarih$` sütunu `datetime` formatına dönüştürüldü ve eksik (`NaN`) değerler $0$ ile dolduruldu.
2.  **Keşifsel Veri Analizi (EDA):** Aylık toplam yağış ve kar miktarları hesaplandı, en yüksek günlük yağış ve kar kayıtları (anomaliler) belirlendi.
3.  **Veri Görselleştirme:** Aylık yağış ve kar dağılımını gösteren çift eksenli çubuk/çizgi grafiği oluşturuldu.
4.  **Raporlama:** Elde edilen bulgular ve veri kısıtlamaları özetlenerek sunuldu.

---

## 💡 Temel Bulgular (2024 Verisine Göre)

Analiz sonuçlarına göre Münih'te $2024$ yılının ilgili dönemindeki hava durumu kalıpları:

* **Yağış Zirvesi:** En yağışlı dönem, **Mayıs-Haziran** aylarıdır. Mayıs ayı, $180.6$ mm ile en yüksek toplam yağış miktarını kaydetmiştir.
* **Aykırı Yağış Olayı:** En yüksek günlük yağış miktarı, $2024$ yılı **Haziran ayının 1'inde $78.4$ mm** olarak kaydedilmiştir. Bu, sel riskini artıran önemli bir aşırı hava olayıdır.
* **Kar Mevsimi:** Kar yağışı, sadece **Mart ve Nisan** aylarında (toplam $\sim 2.5$ cm) gözlemlenmiş ve ardından tamamen sona ermiştir.

---

## 📂 Dosya Yapısı ve Çalıştırma

| Dosya Adı | Türü | Açıklama |
| :--- | :--- | :--- |
| `$munich.csv$` | Girdi Verisi | Analizde kullanılan günlük hava durumu verisi. |
| `$analysis.py$` | Ana Kod | Tüm veri yükleme, analiz ve görselleştirme adımlarını içeren Python betiği. |
| `$aylik\_yagis\_ve\_kar\_kalibi\_GUNCEL.png$` | Çıktı Grafiği | Aylık Yağış ve Kar Yağışı dağılımını gösteren görselleştirme. |

### Nasıl Çalıştırılır?

1.  Gerekli kütüphanelerin (Pandas, NumPy, Matplotlib) kurulu olduğundan emin olun (`pip install pandas numpy matplotlib`).
2.  `$munich.csv$` dosyasını Python betiği ile aynı dizine ($klasöre$) yerleştirin.
3.  Python betiğini çalıştırın.

```bash
python analysis.py