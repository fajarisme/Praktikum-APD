print("""
||------------------------------------------------------------------------------------||
                Selamat datang di program pinjaman online bank Fajar
||------------------------------------------------------------------------------------||
""")

print("""
||------------------------------------------------------------------------||
                Silahkan masukkan username dan password anda
                        maksimal percobaan hanya 3 kali
||------------------------------------------------------------------------||
""")

nama = "fajar"
password = 30
count = 1

while count < 4:
    username = input("Masukkan username anda: ")
    password_akun = int(input("Masukkan password anda: "))
    if username == nama and password_akun == password:
        print("Anda berhasil login")
        
    else:
        print("Username atau password salah")
        count += 1

if count < 4:
    while True:
        pinjaman = int(input("Masukkan banyak pinjaman yang ingin diajukan: "))
        print("""
    ||----------------------------------------------------------------------------||
                    Silahkan masukkan data diri anda
    ||----------------------------------------------------------------------------||
        """)
        name = input("Masukkan nama anda : ")
        NIM = input("Masukkan NIM anda : ")
        print("""
    ||-------------------------------------------------------------------||
                Bunga cicilan bank Fajar
                    1 tahun = 7%
                    2 tahun = 13%
                    3 tahun = 19%
    ||-------------------------------------------------------------------||
        """)

        lama_cicilan = int(input("Masukkan lama cicilan (Dalam tahun): "))
        bunga1 = 0.07
        bunga2 = 0.13
        bunga3 = 0.19         
        bulan = lama_cicilan * 12

        if lama_cicilan == 1:
            bunga_bulan = (bunga1 / 12) * pinjaman
        elif lama_cicilan == 2:
            bunga_bulan = (bunga2 / 12) * pinjaman
        elif lama_cicilan == 3:
            bunga_bulan = (bunga3 / 12) * pinjaman
            
        cicilan_bulan = (pinjaman + (bunga_bulan * bulan)) / bulan

        print(f"""
    ||-------------------------------------------------------------------------------------------------------------------------------||
    Total pinjaman yang {name} ajukan adalah sebesar Rp. {pinjaman:,.0f}
    {lama_cicilan} tahun adalah lama cicilan yang ingin diajukan
    Total cicilan per bulan yang harus dibayarkan setelah mendapatkan bunga adalah sebesar Rp. {cicilan_bulan:,.0f}
    ||-------------------------------------------------------------------------------------------------------------------------------||
    """)

        print("""
    ||-----------------------------------------------------------------||
                    Menu:
                1. Menu pinjaman
                2. Keluar
    ||-----------------------------------------------------------------||
    """)
        menu = int(input("Masukkan pilihan (1/2): "))

        if menu == 1:
            pass
        elif menu == 2: 
            print("Anda memilih untuk keluar")
            break

if count == 4:
        print("Anda sudah melebihi batas input")
