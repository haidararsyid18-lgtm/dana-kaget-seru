import streamlit as st
import time

st.set_page_config(page_title="Pesan Terakhir (Haidar Arsyid Al-Faaruuq) Untukmu...", page_icon="🥀")

st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #E0E0E0; font-family: 'serif'; }
    .stButton>button { 
        width: 100%; background-color: #B22222; color: white; 
        border-radius: 30px; height: 3.5em; border: none; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Sejujurnya... Aku Menyerah 🥀")
st.write("Mungkin ini saatnya aku mengatakannya sebelum terlambat.")

st.markdown("""
---
Kita sudah melewati banyak hal. Tawa, tangis, dan semua rahasia yang kita simpan sendiri. 
Tapi akhir-akhir ini aku merasa ada yang hilang. Aku nggak tahu harus mulai dari mana, 
tapi aku sudah menyiapkan ini khusus untukmu. Terima kasih untuk semuanya...
""")

st.info("⚠️ Mohon baca sampai akhir sebelum membalas.")

if st.button("BUKA PESAN TERAKHIR"):
    with st.spinner('Membuka memori kita yang tersimpan...'):
        time.sleep(5) 
    
    st.balloons()
    st.snow()
    st.success("🎉 Yah Kena Tipu Lagi Kalian...PRANK!!! 🎉")
    st.markdown("### Cieee yang udah mau nangis! 😂")
    st.write("Selamat ya! Jangan baper dulu, ini cuma prank biar kamu kaget!")
    st.image("https://media.giphy.com")
