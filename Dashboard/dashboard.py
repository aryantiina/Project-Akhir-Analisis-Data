import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

st.set_page_config(layout="wide", page_title="E-Commerce Data Analysis Dashboard")

st.title("E-Commerce Public Dataset Analysis")
st.write("Dashboard ini menyajikan analisis performa pengiriman dan rating pelanggan.")

@st.cache_data
def load_data():
    df = pd.read_csv('Dashboard/main_data.csv')
    
    date_cols = [
        'order_purchase_timestamp',
        'order_delivered_customer_date',
        'order_estimated_delivery_date',
        'review_creation_date',
        'review_answer_timestamp',
        'shipping_limit_date'
    ]
    for col in date_cols:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    df = df.dropna(subset=['order_purchase_timestamp'])
    
    return df

df_all_merged = load_data()

st.sidebar.header("Pengaturan & Informasi")
st.sidebar.info("Dashboard ini menampilkan insight dari analisis data E-Commerce Olist.")

min_date = df_all_merged['order_purchase_timestamp'].min()
max_date = df_all_merged['order_purchase_timestamp'].max()

date_range = st.sidebar.date_input(
    label="Filter Tanggal Pembelian",
    min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
)

if isinstance(date_range, (list, tuple)) and len(date_range) == 2:
    start_date, end_date = date_range
else:
    start_date = end_date = date_range

df_filtered = df_all_merged[
    (df_all_merged['order_purchase_timestamp'] >= pd.to_datetime(start_date)) &
    (df_all_merged['order_purchase_timestamp'] <= pd.to_datetime(end_date))
].copy()

st.header("1. Keterlambatan Pengiriman Tahun 2018")

if 'is_delayed' not in df_filtered.columns:
    df_filtered['is_delayed'] = df_filtered['order_delivered_customer_date'] > df_filtered['order_estimated_delivery_date']

orders_2018 = df_filtered[df_filtered['order_purchase_timestamp'].dt.year == 2018]
total_orders_2018 = len(orders_2018.drop_duplicates(subset=['order_id'])) 
delayed_orders_2018 = orders_2018.drop_duplicates(subset=['order_id'])['is_delayed'].sum()

if total_orders_2018 > 0:
    percentage_delayed_2018 = (delayed_orders_2018 / total_orders_2018) * 100
    st.metric(label="Persentase Keterlambatan Pengiriman (2018)", value=f"{percentage_delayed_2018:.2f}%")

    fig1, ax1 = plt.subplots(figsize=(8, 6))
    ax1.bar(['Keterlambatan Pengiriman'], [percentage_delayed_2018], color='darkred', width=0.5)
    ax1.set_ylim(0, 100)
    ax1.set_ylabel('Persentase (%)')
    ax1.set_title('Persentase Keterlambatan Pengiriman di Tahun 2018')
    ax1.text('Keterlambatan Pengiriman', percentage_delayed_2018 + 1, f'{percentage_delayed_2018:.2f}%', ha='center')
    ax1.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig1)
else:
    st.write("Tidak ada data pesanan untuk tahun 2018.")

st.header("2. Hubungan Rating Pelanggan dan Waktu Pengiriman")

df_q2_2017 = df_filtered[
    (df_filtered['order_purchase_timestamp'].dt.year == 2017) &
    (df_filtered['order_purchase_timestamp'].dt.month <= 6)
]

if not df_q2_2017.empty:
    correlation = df_q2_2017['delivery_time'].corr(df_q2_2017['review_score'])
    st.write(f"Korelasi antara waktu pengiriman dan rating pelanggan: **{correlation:.2f}**")

    fig2, ax2 = plt.subplots(figsize=(12, 7))
    sns.regplot(
        x='delivery_time',
        y='review_score',
        data=df_q2_2017,
        scatter_kws={'alpha':0.3},
        line_kws={'color':'red'},
        ax=ax2
    )
    ax2.set_title('Hubungan Waktu Pengiriman dan Rating Pelanggan')
    ax2.set_xlabel('Waktu Pengiriman (Hari)')
    ax2.set_ylabel('Rating Pelanggan')
    st.pyplot(fig2)
else:
    st.write("Tidak ada data untuk periode ini.")

st.header("3. Keterlambatan Pengiriman Berdasarkan Bulan Pembelian")

df_filtered['purchase_month'] = df_filtered['order_purchase_timestamp'].dt.month

monthly_delay_unique_orders = df_filtered.drop_duplicates(subset=['order_id']).groupby('purchase_month')['is_delayed'].agg(
    total_orders='count',
    delayed_orders='sum'
).reset_index()

monthly_delay_unique_orders['delay_percentage'] = (
    monthly_delay_unique_orders['delayed_orders'] /
    monthly_delay_unique_orders['total_orders']
) * 100

monthly_delay_unique_orders = monthly_delay_unique_orders.sort_values('purchase_month')

if not monthly_delay_unique_orders.empty:
    fig3, ax3 = plt.subplots(figsize=(12, 7))

    top_3 = monthly_delay_unique_orders.nlargest(3, 'delay_percentage')['purchase_month'].tolist()
    colors = ['darkblue' if m in top_3 else 'lightgrey' for m in monthly_delay_unique_orders['purchase_month']]

    sns.barplot(
        x='purchase_month',
        y='delay_percentage',
        data=monthly_delay_unique_orders,
        palette=colors,
        ax=ax3
    )

    ax3.set_title('Persentase Keterlambatan Berdasarkan Bulan')
    ax3.set_xlabel('Bulan')
    ax3.set_ylabel('Persentase (%)')
    ax3.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(fig3)
else:
    st.write("Tidak ada data untuk analisis bulanan.")

if st.sidebar.checkbox("Tampilkan Data Mentah"): 
    st.subheader("Data Mentah")
    st.write(df_filtered.head())
