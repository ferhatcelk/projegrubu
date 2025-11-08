import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


file_name = "basket_details.csv"
df = pd.read_csv(file_name)

print("--- Aşama 1: Veri Yükleme ve Hazırlık ---")
print("Veri Setinin İlk 5 Satırı:")
print(df.head())
print("\nVeri Seti Bilgi Özeti (Önce):")
df.info()

# 'basket_date' sütununu datetime formatına dönüştür
df['basket_date'] = pd.to_datetime(df['basket_date'])

print("\nVeri Seti Bilgi Özeti (Sonra):")
df.info()


# *****************************************
# Aşama 2: Keşifsel Veri Analizi (EDA)
# *****************************************

print("\n--- Aşama 2: Keşifsel Veri Analizi (EDA) ---")

# 1. Temel Metrikler
total_quantity_sold = df['basket_count'].sum()
unique_customers = df['customer_id'].nunique()
unique_products = df['product_id'].nunique()
data_period_start = df['basket_date'].min().strftime('%Y-%m-%d')
data_period_end = df['basket_date'].max().strftime('%Y-%m-%d')

print(f"Toplam Satılan Ürün Miktarı: {total_quantity_sold}")
print(f"Benzersiz Müşteri Sayısı: {unique_customers}")
print(f"Benzersiz Ürün Sayısı: {unique_products}")
print(f"Veri Periyodu: {data_period_start} ile {data_period_end} arası")

# 2. Zaman İçinde Satış Performansı (Günlük)
daily_sales = df.groupby('basket_date')['basket_count'].sum().reset_index()
daily_sales.columns = ['basket_date', 'quantity_sold']
print("\nGünlük Satış Verilerinin İlk 5 Satırı (Miktar Bazında):")
print(daily_sales.head())

# 3. Popüler Ürünler
# Ürün bazında toplam satılan miktarı hesapla
product_sales = df.groupby('product_id')['basket_count'].sum().reset_index()
product_sales.columns = ['product_id', 'total_quantity_sold']

# En çok satılan ilk 10 ürünü bul ve kaydet
top_10_products = product_sales.sort_values(by='total_quantity_sold', ascending=False).head(10)
print("\nEn Çok Satan İlk 10 Ürün (Miktar Bazında):")
print(top_10_products)

# (İsteğe bağlı: CSV olarak kaydetme - raporda kullanmak için)
top_10_products.to_csv('top_10_products.csv', index=False)


# *****************************************
# Aşama 3: Veri Görselleştirme
# *****************************************

print("\n--- Aşama 3: Veri Görselleştirme ---")

# 1. Zaman İçinde Satış Performansı (Günlük Çizgi Grafiği)
plt.figure(figsize=(12, 6))
plt.plot(daily_sales['basket_date'], daily_sales['quantity_sold'], marker='o', linestyle='-')
plt.title('Zaman İçinde Günlük Satılan Ürün Miktarı', fontsize=16)
plt.xlabel('Tarih', fontsize=12)
plt.ylabel('Satılan Ürün Miktarı (Adet)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('daily_sales_performance.png')
plt.close()
print("Günlük satış performansı grafiği 'daily_sales_performance.png' olarak kaydedildi.")


# 2. Popüler Ürünler (İlk 10 Çubuk Grafiği)
products = top_10_products['product_id'].astype(str) # ID'leri stringe çevir
quantities = top_10_products['total_quantity_sold']

plt.figure(figsize=(12, 6))
plt.bar(products, quantities, color='skyblue')
plt.title('En Çok Satan İlk 10 Ürün (Miktar Bazında)', fontsize=16)
plt.xlabel('Ürün ID', fontsize=12)
plt.ylabel('Toplam Satılan Miktar (Adet)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('top_10_products_bar_chart.png')
plt.close()
print("En çok satan ilk 10 ürün grafiği 'top_10_products_bar_chart.png' olarak kaydedildi.")

print("\nAnaliz tamamlandı. Sonuçlar ve grafikler bulunduğunuz dizine kaydedilmiştir.")