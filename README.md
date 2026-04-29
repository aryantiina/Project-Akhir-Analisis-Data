# Proyek Analisis Data: E-Commerce Public Dataset

# Deskripsi Proyek
Proyek ini bertujuan untuk menganalisis dataset e-commerce publik guna memahami pola transaksi, performa pengiriman, dan tingkat kepuasan pelanggan. Fokus utama analisis adalah mengidentifikasi keterlambatan pengiriman serta hubungannya dengan rating pelanggan.

# Dataset
Dataset yang digunakan meliputi:
- `orders_dataset.csv`: Informasi utama pesanan.
- `order_items_dataset.csv`: Detail item dalam setiap pesanan.
- `order_payments_dataset.csv`: Informasi pembayaran pesanan.
- `order_reviews_dataset.csv`: Ulasan pelanggan untuk pesanan.

## Persyaratan (Requirements)
Untuk menjalankan analisis ini, Anda memerlukan pustaka Python berikut:
- `python`
- `pandas`
- `numpy`
- `matplotlib`
- `seaborn`
- `datetime`
  

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

## Cara Menjalankan Analisis (Jupyter/Colab Notebook)
1.  **Unduh Dataset**: Pastikan Anda memiliki semua file CSV dataset (`orders_dataset.csv`, `order_items_dataset.csv`, `order_payments_dataset.csv`, `order_reviews_dataset.csv`) di direktori yang sama dengan notebook ini atau sesuaikan path di kode.
2.  **Buka Notebook**: Buka file `.ipynb` ini di lingkungan Jupyter Notebook atau Google Colab.
3.  **Jalankan Sel**: Jalankan setiap sel kode secara berurutan. Notebook ini telah dirancang untuk memandu Anda melalui langkah-langkah:
    -   Pemuatan Pustaka
    -   Data Wrangling (Gathering, Assessing, Cleaning)
    -   Exploratory Data Analysis (EDA)
    -   Visualization & Explanatory Analysis (Menjawab Pertanyaan Bisnis)
    -   Analisis Lanjutan (Opsional)
    -   Pembuatan `main_data.csv`
    -   Kesimpulan
  
Output dari proses data wrangling akan menghasilkan file `main_data.csv` yang berisi gabungan dari semua dataset relevan untuk analisis.

# Setup Virtual Environment
1.  **Clone Repository**
2.  **uat Virtual Environment `python -m venv venv`**
3.  **ktifkan Virtual Environment**

Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate

# Instalasi Dependencies

Gunakan file requirements.txt agar versi library konsisten:
 ```
pip install -r requirements.txt
  ```

# Cara Menjalankan Dashboard
 ```
streamlit run Dashboard/dashboard.py
 ```

Buka di browser:
 ```
http://localhost:8501
 ```

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
-   **Keterlambatan pengiriman masih menjadi masalah utama**
-   **Waktu pengiriman mempengaruhi kepuasan pelanggan**
-   **rdapat pola musiman pada keterlambatan**

# Rekomendasi
-   **optimalkan logistik pada bulan dengan delay tinggi**
-   **Tingkatkan akurasi estimasi pengiriman**
-   **Berikan transparansi status pengiriman**

