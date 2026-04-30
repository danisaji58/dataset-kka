# 📊 Laporan Praktikum Analisis Performa Penjualan E-Commerce

## 👨‍💻 Identitas Praktikum
**Mata Pelajaran:** Analisis dan Visualisasi Data  
**Topik:** Analisis Performa Penjualan E-Commerce  
**Tools:** Python, Pandas, Matplotlib, Seaborn  

---

## 1. Business Question
Pada praktikum ini, pertanyaan bisnis yang ingin dijawab adalah:

- Kategori produk mana yang memiliki performa penjualan terbaik?
- Apakah anggaran iklan (`Ad_Budget`) berpengaruh terhadap total penjualan (`Total_Sales`)?
- Siapa pelanggan yang paling sering melakukan transaksi?
- Kategori produk mana yang paling efisien berdasarkan biaya iklan?

Tujuan dari analisis ini adalah membantu perusahaan dalam mengambil keputusan pemasaran dan strategi penjualan yang lebih efektif.

---

## 2. Data Wrangling
Tahap ini dilakukan untuk membersihkan dan menyiapkan data sebelum dianalisis.

### Langkah yang dilakukan
- Membaca dataset dari file `data.csv`
- Mengecek struktur data menggunakan `df.info()`
- Mengecek data kosong menggunakan `df.isnull().sum()`
- Menghapus data dengan harga tidak valid (`Price <= 0`)
- Menghapus data yang memiliki nilai `Total_Sales` kosong
- Mengubah kolom `Order_Date` ke format datetime
- Menambahkan kolom `Month` untuk analisis bulanan

### Contoh Kode
```python
df = pd.read_csv('data.csv')

df = df[df['Price'] > 0]
df = df.dropna(subset=['Total_Sales'])

df['Order_Date'] = pd.to_datetime(df['Order_Date'])
df['Month'] = df['Order_Date'].dt.to_period('M').astype(str)