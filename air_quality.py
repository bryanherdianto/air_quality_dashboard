import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

st.header('Air Quality Dashboard :sparkle:')

df = pd.read_csv(r'C:\Users\ACER\Documents\Python\streamlit_dashboard\air_quality_dataset.csv')

st.subheader('Facts')
 
col1, col2 = st.columns(2)
 
with col1:
    total_orders = len(df['station'].unique())
    st.metric("Jumlah Statiun", value=total_orders)
 
with col2:
    total_revenue = df[df['station'] == 'Gucheng']['O3'].max()
    st.metric("Konsentrasi O3 Terbesar di Gucheng", value=total_revenue)

st.subheader("Konsentrasi SO2 pada Stasiun") 

# Assuming you already have the grouped and sorted data
grouped_so2 = df.groupby(by="station")['SO2'].sum().sort_values(ascending=False)

# Create a new DataFrame
so2_summary_df = pd.DataFrame({'station': grouped_so2.index, 'SO2': grouped_so2.values})

fig, ax = plt.subplots(figsize=(16, 8))
ax.bar(
    so2_summary_df['station'],
    so2_summary_df['SO2'],
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15, rotation=90)
 
st.pyplot(fig)

st.subheader("Perkembangan Konsentrasi SO2 per Tahun di Statiun Aotizhongxin") 

# Ubah kolom "year", "month", "day", dan "hour" menjadi "datetime"
df['datetime'] = df[['year', 'month', 'day', 'hour']].apply(lambda s: datetime.datetime(*s), axis=1)

# Drop kolom "year", "month", "day", dan "hour" dari dataset
df.drop(['No', 'year', 'month', 'day', 'hour'], axis=1, inplace=True)

# Ubah posisi dari kolom "datetime"
col = df.pop('datetime')
df.insert(0, 'datetime', col)

# Ambil data pada stasiun Aotizhongxin
air_aotizhongxin = df[df['station'] == 'Aotizhongxin']

# Ambil year dari kolom "datetime"
air_aotizhongxin['year'] = air_aotizhongxin['datetime'].dt.year

# Dapatkan rata-rata konsentrasi SO2
average_so2_by_year = air_aotizhongxin.groupby('year')['SO2'].mean()

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    average_so2_by_year.index,
    average_so2_by_year,
    marker='o', 
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
 
st.pyplot(fig)