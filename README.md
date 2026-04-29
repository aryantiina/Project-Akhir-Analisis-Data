# Proyek Analisis Data: E-Commerce Public Dataset

# Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis dataset e-commerce publik guna memahami pola transaksi, performa pengiriman, dan tingkat kepuasan pelanggan. Fokus utama analisis adalah mengidentifikasi keterlambatan pengiriman serta hubungannya dengan rating pelanggan.

# Dataset

Dataset yang digunakan meliputi:

orders_dataset.csv → Informasi utama pesanan
order_items_dataset.csv → Detail item dalam pesanan
order_payments_dataset.csv → Informasi pembayaran
order_reviews_dataset.csv → Ulasan pelanggan

 🔹 Hasil Data Wrangling
main_data.csv → Dataset utama untuk analisis dan dashboard

# Teknologi yang Digunakan
Python
Pandas
NumPy
Matplotlib
Seaborn
Streamlit

# Struktur Proyek
Project-Akhir-Analisis-Data/
│
├── Dashboard/
│   ├── dashboard.py
│   └── main_data.csv
│
├── Data/
│   ├── orders_dataset.csv
│   └── order_items_dataset.csv
│   └── order_payments_dataset.csv
│   └── order_reviews_dataset.csv
├── Proyek_Analisis_Data_Aryanti_Nagela.ipynb
├── requirements.txt
└── README.md

# Setup Virtual Environment
🔹 1. Clone Repository
git clone https://github.com/aryantiina/Project-Akhir-Analisis-Data.git
cd Project-Akhir-Analisis-Data
🔹 2. Buat Virtual Environment
python -m venv venv
🔹 3. Aktifkan Virtual Environment

Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate

# Instalasi Dependencies

Gunakan file requirements.txt agar versi library konsisten:

pip install -r requirements.txt

# Cara Menjalankan Dashboard
streamlit run Dashboard/dashboard.py

Buka di browser:

http://localhost:8501

# Hasil & Insight Utama
## Keterlambatan Pengiriman
Sekitar 9.37% pesanan tahun 2018 mengalami keterlambatan
Bulan dengan keterlambatan tertinggi:
Maret (17.15%)
Februari (13.42%)
November (14.31%)
## Rating Pelanggan
Korelasi negatif lemah (-0.22) antara waktu pengiriman dan rating
Pengiriman lebih lama → rating cenderung menurun

# Kesimpulan
1. Keterlambatan pengiriman masih menjadi masalah utama
2. Waktu pengiriman mempengaruhi kepuasan pelanggan
3. Terdapat pola musiman pada keterlambatan

# Rekomendasi
1. Optimalkan logistik pada bulan dengan delay tinggi
2. Tingkatkan akurasi estimasi pengiriman
3. Berikan transparansi status pengiriman

