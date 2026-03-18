import streamlit as st
import time

st.set_page_config(page_title="DANA Kaget - Klaim Saldo", page_icon="💰")

st.markdown("""
    <style>
    .stApp { background-color: #008CEE; color: white; }
    .stButton>button { 
        width: 100%; background-color: #FFD700; color: #008CEE; 
        font-weight: bold; border-radius: 15px; height: 3.5em;
    }
    </style>
    """, unsafe_allow_html=True)

st.image("https://upload.wikimedia.org", width=150)
st.title("🎁 DANA Kaget Hari Ini!")
st.subheader("Selamat! Kamu berhak klaim saldo gratis hingga Rp500.000")
st.warning("⚠️ Sisa Kuota: 7/100 Orang")

if st.button("BUKA AMPLOP SEKARANG"):
    with st.spinner('Menghubungkan ke Server DANA...'):
        time.sleep(4)
    st.balloons()
    st.error("WKWK KENA DEH! 😂")
    st.write("Ciee yang langsung gercep pengen saldo gratis! Jangan lupa kerja ya! 🙏😜")
    st.image("https://media.giphy.com")
