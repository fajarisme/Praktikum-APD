print("""
||------------------------------------------------------------------------------------||
                Selamat datang di program pinjaman online bank Fajar
||------------------------------------------------------------------------------------||
""")
nama = input("Masukkan nama anda = ")
NIM = int(input("Masukkan NIM anda = "))
pinjaman = int(input("Masukkan total pinjaman yang ingin anda ajukan  = "))
print("""
||-------------------------------------------------------------------||
                        Bunga cicilan bank Fajar
                            1 tahun = 7%
                            2 tahun = 13%
                            3 tahun = 19%
||-------------------------------------------------------------------||
""")
lama_cicilan = int(input("Masukkan lama cicilan (Dalam tahun) = "))

bunga1 = 0.7
bunga2 = 0.13
bunga3 = 0.19 
bulan = lama_cicilan * 12

if lama_cicilan == 1:
    bunga_bulan = (bunga1/12) * pinjaman
    cicilan_bulan = (pinjaman + bunga_bulan) / bulan
elif lama_cicilan == 2:
    bunga_bulan = (bunga1/12) * pinjaman
    cicilan_bulan = (pinjaman + bunga_bulan) / bulan
elif lama_cicilan == 3:
    bunga_bulan = (bunga1/12) * pinjaman
    cicilan_bulan = (pinjaman + bunga_bulan) / bulan

print(f"""
||------------------------------------------------------------------------------------------------------------------------||
Total pinjaman yang {nama} ajukan adalah sebesar Rp. {pinjaman:,.0f}
{lama_cicilan} tahun adalah lama cicilan yang ingin diajukan
Total cicilan perbulan yang harus dibayarkan setelah mendapatkan bunga adalah sebesar Rp.{cicilan_bulan:,.0f}
||------------------------------------------------------------------------------------------------------------------------||
""")