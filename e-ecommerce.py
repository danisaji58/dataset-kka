import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')
print(df.head())

df.info()
print(df.isnull().sum())
df = df[df['Price'] > 0]
df['Order_Date'] = pd.to_datetime(df['Order_Date'])

df['Month'] = df['Order_Date'].dt.to_period('M').astype(str)
monthly_sales = df.groupby('Month')['Total_Sales'].sum()

plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o', color='b')
plt.title('Tren Penjualan Bulanan')
plt.xticks(rotation=45)
plt.show()

correlation = df[['Total_Sales', 'Ad_Budget', 'Price']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Peta Korelasi Antar Variabel')
plt.show()

# =============================
# TUGAS 1 - UNDERPERFORMER
# =============================
print("\n=== TUGAS 1: UNDERPERFORMER ===")

avg_price = df['Price'].mean()

underperformer = df[df['Price'] > avg_price] \
    .sort_values('Quantity', ascending=True) \
    .head(10)

print(underperformer[['Product_Category', 'Price', 'Quantity']])

plt.figure(figsize=(8,5))
plt.scatter(df['Price'], df['Quantity'])
plt.xlabel('Price')
plt.ylabel('Quantity')
plt.title('Produk Underperformer')
plt.grid(True)
plt.show()


# =============================
# TUGAS 2 - RFM ANALYSIS
# =============================
print("\n=== TUGAS 2: RFM ANALYSIS ===")

import datetime as dt

# hapus data sales kosong
df = df.dropna(subset=['Total_Sales'])

snapshot_date = df['Order_Date'].max() + dt.timedelta(days=1)

rfm = df.groupby('CustomerID').agg({
    'Order_Date': lambda x: (snapshot_date - x.max()).days,
    'Order_ID': 'count',
    'Total_Sales': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

print(rfm.head())


# =============================
# TUGAS 3 - EFISIENSI KATEGORI
# =============================
print("\n=== TUGAS 3: EFISIENSI KATEGORI ===")

category_eff = df.groupby('Product_Category').agg({
    'Total_Sales': 'sum',
    'Ad_Budget': 'sum'
})

category_eff = category_eff[category_eff['Ad_Budget'] > 0]

category_eff['Efficiency'] = (
    category_eff['Total_Sales'] /
    category_eff['Ad_Budget']
)

category_eff = category_eff.sort_values('Efficiency')

print(category_eff)

plt.figure(figsize=(10,5))
plt.barh(category_eff.index, category_eff['Efficiency'])
plt.xlabel('Efficiency')
plt.ylabel('Product Category')
plt.title('Efisiensi Kategori Produk')
plt.show()


# =============================
# TUGAS 4 - UJI HIPOTESIS
# =============================
print("\n=== TUGAS 4: UJI HIPOTESIS ===")

median_ad = df['Ad_Budget'].median()

high_ad = df[df['Ad_Budget'] > median_ad]['Total_Sales']
low_ad = df[df['Ad_Budget'] <= median_ad]['Total_Sales']

print("Rata-rata sales iklan tinggi:", high_ad.mean())
print("Rata-rata sales iklan rendah:", low_ad.mean())

if high_ad.mean() > low_ad.mean():
    print("Kesimpulan: Iklan tinggi meningkatkan penjualan")
else:
    print("Kesimpulan: Iklan tidak terlalu berpengaruh")