import streamlit as st
import time

def ketik_pelan_st(teks, jeda=0.04):
    """Fungsi efek ketikan untuk Streamlit"""
    placeholder = st.empty()
    isi = ""
    for karakter in teks:
        isi += karakter
        placeholder.markdown(isi)
        time.sleep(jeda)

def tampilkan_perpisahan():
    st.title("JEJAK LANGKAH DAN MAAF DARI KAMI, ANGKATAN 6")
    st.divider()

    paragraf = [
        "Assalamualaikum Warahmatullahi Wabarakatuh,",
        "Selamat pagi/siang/malam, dan salam sejahtera untuk kita semua.",
        "Kepada Bapak/Ibu guru yang kami hormati, teman-teman seperjuangan, serta adik-adik tingkat yang kami sayangi.",
        "Hari ini, udara rasanya sedikit lebih berat dari biasanya...",
        "Izinkan kami, Angkatan 6, menundukkan kepala dan meminta maaf atas segala salah."
    ]

    for teks in paragraf:
        ketik_pelan_st(teks)
        time.sleep(0.5)
    
    st.success("Kami, Angkatan 6, pamit undur diri. Wassalamualaikum Warahmatullahi Wabarakatuh.")

if __name__ == "__main__":
    tampilkan_perpisahan()
