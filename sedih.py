import time
import sys

def ketik_pelan(teks, jeda=0.04):
    """Fungsi untuk membuat efek ketikan mesin tik"""
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(jeda)
    print()

def tampilkan_perpisahan():
    # Judul
    print("=" * 60)
    ketik_pelan("          JEJAK LANGKAH DAN MAAF DARI KAMI, ANGKATAN 6", 0.05)
    print("=" * 60)
    time.sleep(1)

    # Isi Teks Perpisahan
    paragraf = [
        "\nAssalamualaikum Warahmatullahi Wabarakatuh,",
        "Selamat pagi/siang/malam, dan salam sejahtera untuk kita semua.\n",
        "Kepada Bapak/Ibu guru yang kami hormati, teman-teman seperjuangan, \nserta adik-adik tingkat yang kami sayangi.\n",
        "Hari ini, udara rasanya sedikit lebih berat dari biasanya. Waktu yang dulu terasa",
        "berjalan begitu lambat saat kami pertama kali melangkahkan kaki di sini, nyatanya",
        "kini telah sampai di penghujung jalan. Rasanya baru kemarin kami datang dengan wajah",
        "lugu dan penuh tanda tanya, tapi hari ini, kami harus berdiri di sini untuk",
        "mengucapkan satu kata yang paling kami benci: Selamat tinggal.\n",
        "Di tempat ini, kami tidak hanya belajar tentang buku dan teori, tapi juga tentang",
        "tawa, tangis, persahabatan, dan arti dari sebuah keluarga. Setiap sudut tempat ini",
        "telah merekam ribuan cerita yang akan selalu menjadi bagian dari detak jantung kami.",
        "Namun, seiring dengan tawa yang pernah kita bagi, kami sadar bahwa ada luka yang",
        "mungkin tak sengaja kami torehkan.\n",
        "Oleh karena itu, di hari yang berat ini, di hadapan Bapak, Ibu, dan teman-teman semua...",
        "Izinkan kami, Angkatan 6, menundukkan kepala.\n",
    ]

    poin_maaf = [
        "[*] Kami meminta maaf yang sebesar-besarnya. Untuk setiap kata yang mungkin terlalu \n    keras terucap, untuk setiap candaan yang melewati batas, dan untuk setiap \n    tingkah laku kami yang mungkin pernah mengecewakan Bapak dan Ibu.",
        "[*] Kami meminta maaf karena belum bisa menjadi sempurna. Untuk janji yang mungkin \n    belum sempat kami tepati, dan untuk ekspektasi yang belum mampu kami capai.",
        "[*] Kepada adik-adik kelas, kami juga meminta maaf. Jika selama ini kami belum bisa \n    menjadi teladan yang baik. Percayalah, itu semua karena kami peduli dan ingin \n    kalian menjadi jauh lebih hebat dari kami.\n"
    ]

    penutup = [
        "Kami sadar, ribuan kata maaf tidak akan bisa menghapus setiap kesalahan kami.",
        "Tapi kami berharap, pintu maaf itu masih terbuka untuk kami, Angkatan 6.\n",
        "Bapak, Ibu, dan teman-teman semua...",
        "Terima kasih telah menerima kami apa adanya. Terima kasih telah mendidik kami",
        "dengan sabar. Jasamu tidak akan pernah bisa kami balas dengan apa pun, selain",
        "dengan doa agar Tuhan selalu menjaga Bapak dan Ibu di mana pun berada.\n",
        "Kini, tiba saatnya Angkatan 6 harus pamit. Langkah kami mungkin akan membawa kami",
        "menjauh dari gerbang ini, tapi percayalah, hati kami akan selalu tertinggal di sini.\n",
        "\"Perpisahan hanya untuk mereka yang mencintai dengan mata.",
        " Bagi mereka yang mencintai dengan hati dan jiwa, tidak ada yang namanya perpisahan.\"\n",
        "Terima kasih untuk segalanya.",
        "Maafkan kami atas segalanya.",
        "Kami, Angkatan 6, pamit undur diri.\n",
        "Wassalamualaikum Warahmatullahi Wabarakatuh."
    ]

    # Menjalankan paragraf awal
    for teks in paragraf:
        ketik_pelan(teks)
        time.sleep(0.5)

    # Menjalankan poin permohonan maaf (lebih lambat / jeda lebih lama)
    time.sleep(1)
    for teks in poin_maaf:
        ketik_pelan(teks, 0.05)
        time.sleep(1.2) # Jeda ekstra untuk memberikan kesan emosional

    # Menjalankan penutup
    for teks in penutup:
        ketik_pelan(teks)
        time.sleep(0.8)

    print("=" * 60)
    print("                    [ PROGRAM SELESAI ]")
    print("=" * 60)

# Menjalankan fungsi utama
if __name__ == "__main__":
    tampilkan_perpisahan()
