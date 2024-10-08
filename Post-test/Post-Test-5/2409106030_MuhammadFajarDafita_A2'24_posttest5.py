pengguna = [
    [1, 'fajar', 'fajarisme', 'admin'],
    [2, 'rasyid', 'mboten', 'pengguna']
]

produk = [
    [1, 'Membership Bulanan', 300000, 'membership'],
    [2, 'Air Mineral', 10000, 'addons'],
    [3, 'Steroid', 500000, 'addons'],
    [4, 'Protein Powder', 150000, 'addons']
]

while True:
    print("||==============================||")
    print("Selamat Datang di Manajemen Gym \n1. Login \n2. Register \n3. Keluar")
    print("||==============================||")
    pilihan = input("Pilih Menu: ")

    if pilihan == '1':
        print("ANDA MEMILIH FITUR LOGIN \nSILAHKAN MASUKKAN USERNAME DAN PASSWORD ANDA ")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        user = None
        for u in pengguna:
            if u[1] == username and u[2] == password:
                user = u
                break

        if user:
            print(f"\nLogin berhasil sebagai {user[1]} ({user[3]})\n")
            if user[3] == 'admin':
                while True:
                    print("Menu Admin:")
                    print("1. Tambah Produk")
                    print("2. Lihat Produk")
                    print("3. Edit Produk")
                    print("4. Hapus Produk")
                    print("5. Logout")
                    pilihan_admin = input("Pilih Menu: ")

                    if pilihan_admin == '1':                   
                        id_baru = len(produk) + 1
                        nama_baru = input("Masukkan nama produk: ")
                        harga_baru = input("Masukkan harga produk: ")

                        if harga_baru.isdigit():
                            kategori_baru = input("Masukkan kategori (membership/addons): ").lower()

                            if kategori_baru == 'membership' or kategori_baru == 'addons':
                                produk.append([id_baru, nama_baru, int(harga_baru), kategori_baru])
                                print("Produk berhasil ditambahkan!\n")
                            else:
                                print("Kategori tidak valid! Harus 'membership' atau 'addons'.\n")
                        else:
                            print("Harga harus berupa angka!\n")

                    elif pilihan_admin == '2':
                        print("\nDaftar Produk:")
                        for p in produk:
                            print(f"ID: {p[0]}, Nama: {p[1]}, Harga: {p[2]}, Kategori: {p[3]}")
                        print()

                    elif pilihan_admin == '3':
                        id_edit = input("Masukkan ID produk yang akan diedit: ")

                        if id_edit.isdigit():
                            id_edit = int(id_edit)
                            for p in produk:
                                if p[0] == id_edit:
                                    nama_edit = input("Masukkan nama baru: ")
                                    harga_edit = input("Masukkan harga baru: ")

                                    if harga_edit.isdigit():
                                        kategori_edit = input("Masukkan kategori baru (membership/addons): ").lower()

                                        if kategori_edit == 'membership' or kategori_edit == 'addons':
                                            p[1], p[2], p[3] = nama_edit, int(harga_edit), kategori_edit
                                            print("Produk berhasil diupdate!\n")
                                        else:
                                            print("Kategori tidak valid! Harus 'membership' atau 'addons'.\n")
                                    else:
                                        print("Harga harus berupa angka!\n")
                                    break
                            else:
                                print("Produk tidak ditemukan!\n")
                        else:
                            print("ID produk harus berupa angka!\n")

                    elif pilihan_admin == '4':
                        id_hapus = input("Masukkan ID produk yang akan dihapus: ")

                        if id_hapus.isdigit():
                            id_hapus = int(id_hapus)
                            for p in produk:
                                if p[0] == id_hapus:
                                    produk.remove(p)
                                    print("Produk berhasil dihapus!\n")
                                    break
                            else:
                                print("Produk tidak ditemukan!\n")
                        else:
                            print("ID produk harus berupa angka!\n") 

                    elif pilihan_admin == '5':
                        print("Logout berhasil!\n")
                        break

                    else:
                        print("Pilihan tidak valid!\n")

            elif user[3] == 'pengguna':
                while True:
                    print("Menu Pengguna:")
                    print("1. Lihat Produk")
                    print("2. Beli Membership")
                    print("3. Beli Addons")
                    print("4. Logout")
                    pilihan_pengguna = input("Pilih Menu: ")

                    if pilihan_pengguna == '1':
                        print("\nDaftar Produk:")
                        for p in produk:
                            print(f"ID: {p[0]}, Nama: {p[1]}, Harga: {p[2]}, Kategori: {p[3]}")
                        print()

                    elif pilihan_pengguna == '2':
                        print("\nDaftar Membership:")
                        for p in produk:
                            if p[3] == 'membership':
                                print(f"ID: {p[0]}, Nama: {p[1]}, Harga: {p[2]}")
                        id_beli = input("Masukkan ID membership yang ingin dibeli: ")

                        if id_beli.isdigit():
                            id_beli = int(id_beli)
                            for p in produk:
                                if p[0] == id_beli and p[3] == 'membership':
                                    print(f"Anda telah membeli {p[1]} seharga {p[2]}\n")
                                    break
                            else:
                                print("Membership tidak ditemukan!\n")
                        else:
                            print("ID harus berupa angka!\n")

                    elif pilihan_pengguna == '3':
                        print("\nDaftar Addons:")
                        for p in produk:
                            if p[3] == 'addons':
                                print(f"ID: {p[0]}, Nama: {p[1]}, Harga: {p[2]}")
                        id_beli = input("Masukkan ID addons yang ingin dibeli: ")

                        if id_beli.isdigit():
                            id_beli = int(id_beli)
                            for p in produk:
                                if p[0] == id_beli and p[3] == 'addons':
                                    print(f"Anda telah membeli {p[1]} seharga {p[2]}\n")
                                    break
                            else:
                                print("Addons tidak ditemukan!\n")
                        else:
                            print("ID harus berupa angka!\n")

                    elif pilihan_pengguna == '4':
                        print("Logout berhasil!\n")
                        break

                    else:
                        print("Pilihan tidak valid!\n")
        else:
            print("Login gagal! Username atau password salah.\n")

    elif pilihan == '2':
        id_baru = len(pengguna) + 1
        username_baru = input("Masukkan username baru: ")

        checkusername = False
        for u in pengguna:
            if u[1] == username_baru:
                checkusername = True
                break
        if checkusername:
            print("Username telah digunakan, silahkan login menggunakan username tersebut atau register menggunakan username yang lain!\n")
        else:
            password_baru = input("Masukkan password baru: ")
            pilihanakun = input("Masukkan pilihan anda\n1. Untuk akun user\n2. Untuk admin: ")

            if pilihanakun == '1':
                pengguna.append([id_baru, username_baru, password_baru, 'pengguna'])
                print("Registrasi berhasil!\n")
            elif pilihanakun == '2':
                pengguna.append([id_baru, username_baru, password_baru, 'admin'])
                print("Registrasi berhasil!\n")
            else:
                print("Pilihan akun tidak valid!\n")

    elif pilihan == '3':
        print("Anda memilih untuk keluar, terimakasih telah mengakses GYM kami!")
        break

    else:
        print("Pilihan tidak valid!\n")
