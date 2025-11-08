import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# *****************************************
# Aşama 1: Veri Yükleme ve Hazırlık
# *****************************************

print("--- Aşama 1: Veri Yükleme ve Hazırlık ---")

file_name = "munich.csv"
# Veri setini noktalı virgül (;) ayırıcı ile yükle
df = pd.read_csv(file_name, delimiter=';')

# Sütun isimlerini yeniden adlandır
df.columns = ['Tarih', 'Yagis_mm', 'Kar_cm']

# 'Tarih' sütununu datetime formatına dönüştür
df['Tarih'] = pd.to_datetime(df['Tarih'])

# Eksik değerleri kontrol et ve 0 ile doldur (Yağış ve Kar için NaN değerleri 0 olarak kabul edilir)
# Veri seti sadece 2024 yılının bir kısmını içerdiği için uzun vadeli trend analizi yapılamayacaktır.
df['Yagis_mm'] = df['Yagis_mm'].fillna(0)
df['Kar_cm'] = df['Kar_cm'].fillna(0)

# Yıl ve Ay sütunlarını oluştur (EDA ve Görselleştirme için gerekli)
df['Yil'] = df['Tarih'].dt.year
df['Ay'] = df['Tarih'].dt.month

print(f"Veri aralığı: {df['Tarih'].min().strftime('%Y-%m-%d')} - {df['Tarih'].max().strftime('%Y-%m-%d')}")
print("\nVeri Hazırlığı Sonrası İlk 5 Satır:")
print(df.head())
print("\nVeri Hazırlığı Sonrası Bilgi Özeti:")
df.info()


# *****************************************
# Aşama 2: Keşifsel Veri Analizi (EDA)
# *****************************************

print("\n--- Aşama 2: Keşifsel Veri Analizi (EDA) ---")

# 1. Temel İstatistikler
print("\nYağış ve Kar Temel İstatistikleri (Tüm Dönem):")
print(df[['Yagis_mm', 'Kar_cm']].describe().round(2))

# 2. Aykırı Hava Olayları (Anomaliler)
max_yagis_day = df.loc[df['Yagis_mm'].idxmax()]
max_kar_day = df.loc[df['Kar_cm'].idxmax()]

print("\nEn Yüksek Günlük Yağış Kaydı:")
print(f"Tarih: {max_yagis_day['Tarih'].strftime('%Y-%m-%d')}, Miktar: {max_yagis_day['Yagis_mm']} mm")

print("\nEn Yüksek Günlük Kar Yağışı Kaydı:")
print(f"Tarih: {max_kar_day['Tarih'].strftime('%Y-%m-%d')}, Miktar: {max_kar_day['Kar_cm']} cm")

# 3. Mevsimsel Kalıplar (Aylık Toplamlar)
monthly_totals = df.groupby('Ay')[['Yagis_mm', 'Kar_cm']].sum().reset_index()
print("\nAylık Toplam Yağış (mm) ve Kar (cm) Miktarları:")
print(monthly_totals.round(2))


# *****************************************
# Aşama 3: Veri Görselleştirme
# *****************************************

print("\n--- Aşama 3: Veri Görselleştirme ---")

# Matplotlib için ayarlar
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['figure.dpi'] = 100

# Ayları etiketler için hazırlayalım (Verideki aylara göre)
month_names = ['Ock', 'Şbt', 'Mrt', 'Nis', 'May', 'Haz', 'Tem', 'Ağu', 'Eyl', 'Eki', 'Ksm', 'Arlk']
x_labels = [month_names[i-1] for i in monthly_totals['Ay']]
x_positions = monthly_totals['Ay']

fig, ax1 = plt.subplots(figsize=(10, 6))

# Yağış grafiği (Sol Eksen - Çubuk)
color_yagis = 'tab:blue'
ax1.set_xlabel('Ay (2024)', fontsize=12)
ax1.set_ylabel('Toplam Yağış (mm)', color=color_yagis, fontsize=12)
ax1.bar(x_positions, monthly_totals['Yagis_mm'], color=color_yagis, alpha=0.6, label='Toplam Yağış (mm)')
ax1.tick_params(axis='y', labelcolor=color_yagis)
ax1.set_xticks(x_positions)
ax1.set_xticklabels(x_labels, rotation=45, ha='right')

# Kar grafiği (Sağ Eksen - Çizgi)
ax2 = ax1.twinx()
color_kar = 'tab:gray'
ax2.set_ylabel('Toplam Kar Yağışı (cm)', color=color_kar, fontsize=12)
ax2.plot(x_positions, monthly_totals['Kar_cm'], color=color_kar, marker='o', linestyle='-', linewidth=2, label='Toplam Kar Yağışı (cm)')
ax2.tick_params(axis='y', labelcolor=color_kar)

# Başlık ve layout
plt.title('2024 Yılı Aylık Yağış ve Kar Yağışı Kalıpları (Münih)', fontsize=14)
fig.tight_layout()
plt.savefig('aylik_yagis_ve_kar_kalibi.png')
plt.close()

print("Grafik: 'aylik_yagis_ve_kar_kalibi.png' kaydedildi.")


# *****************************************
# Aşama 4: Raporlama İçin Özet
# *****************************************

print("\n--- Aşama 4: Raporlama ve İçgörüler ---")

print("\n### İklimsel Kalıplar (2024, Mart-Temmuz) ###")

# Yağış İçgörüsü
yagis_zirvesi = monthly_totals.loc[monthly_totals['Yagis_mm'].idxmax()]
print(f"1. Mevsimsel Kalıp (Yağış): Mayıs ({month_names[yagis_zirvesi['Ay']-1]}) ayı, {yagis_zirvesi['Yagis_mm']:.1f} mm ile en yağışlı aydır. İlkbahar sonu, en yoğun yağış dönemidir.")

# Kar İçgörüsü
kar_toplami = monthly_totals['Kar_cm'].sum()
print(f"2. Mevsimsel Kalıp (Kar): Kar yağışı, sadece Mart ve Nisan aylarında (Toplam: {kar_toplami:.2f} cm) gözlemlenmiştir. Nisan'dan sonra kar riski sona ermiştir.")

# Aykırı Olay İçgörüsü
print(f"3. Aykırı Hava Olayı: En yüksek günlük yağış {max_yagis_day['Yagis_mm']} mm olarak {max_yagis_day['Tarih'].strftime('%Y-%m-%d')} tarihinde kaydedilmiştir. Bu tür aşırı olaylar sel riskini artırır.")

print("\nAnaliz tamamlandı. Sonuçlar terminalde gösterilmiş ve 'aylik_yagis_ve_kar_kalibi.png' grafiği bulunduğunuz dizine kaydedilmiştir.")