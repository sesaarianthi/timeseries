import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit UI
st.title('Try to analyze!')

# Upload file CSV
uploaded_file = st.file_uploader("Upload your data (CSV)", type=["csv"])

if uploaded_file is not None:
    # Membaca data CSV
    df = pd.read_csv(uploaded_file, parse_dates=['DATE'], dayfirst=True, index_col='DATE')
    
    # Menampilkan beberapa baris data
    st.write(df.tail())

    # Menentukan nilai maksimum dan minimum serta tanggalnya
    max_value = df['Value'].max()
    min_value = df['Value'].min()
    max_date = df['Value'].idxmax()
    min_date = df['Value'].idxmin()

    # Plot data time series
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, df['Value'], label='Electricity Consumption', color='blue')
    plt.title('Electricity Consumption Over Time')
    plt.xlabel('Date')
    plt.ylabel('Consumption (in kWh or unit)')
    plt.legend()

    # Menambahkan informasi tentang max dan min pada plot
    plt.scatter(max_date, max_value, color='red', label=f'Max Value: {max_value} on {max_date.strftime("%Y-%m-%d")}')
    plt.scatter(min_date, min_value, color='green', label=f'Min Value: {min_value} on {min_date.strftime("%Y-%m-%d")}')
    
    # Tampilkan plot di Streamlit
    st.pyplot(plt)

    # Menampilkan informasi nilai maksimum dan minimum
    st.subheader(f"Maximum Value: {max_value} on {max_date.strftime('%Y-%m-%d')}")
    st.subheader(f"Minimum Value: {min_value} on {min_date.strftime('%Y-%m-%d')}")

    # Menambahkan kalimat promosi di bawah grafik
    st.markdown("""
        ---
        ## Ingin mengeksplorasi data bisnis Anda lebih lanjut?
        **Konsultasikan dengan [Data Sketch Business Analysis](https://www.datasketch.com)!**
        Kami siap membantu menganalisis data Anda untuk pengambilan keputusan yang lebih baik dan lebih cepat.
    """)
