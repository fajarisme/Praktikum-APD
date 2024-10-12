pengguna = {}

produk = {
    1: {'nama': 'Membership Bulanan', 'harga': 300000, 'kategori': 'membership'},
    2: {'nama': 'Air Mineral', 'harga': 10000, 'kategori': 'addons'},
    3: {'nama': 'Steroid', 'harga': 500000, 'kategori': 'addons'},
    4: {'nama': 'Protein Powder', 'harga': 150000, 'kategori': 'addons'}
}

while True:
    print("||==============================================================||")
    print("                 Selamat Datang di Manajemen Gym                  ")
    print("||==============================================================||")
    print("                          1. Register")
    print("                          2. Login")
    print("                          3. Keluar")
    print("||==============================================================||")
    pilihan = input("Pilih Menu: ")

    if pilihan == '1':
        username_baru = input("Masukkan username baru: ")

        if username_baru in pengguna:
            print("Username sudah terdaftar, silakan login atau gunakan username lain!\n")
        else:
            password_baru = input("Masukkan password baru: ")
            pilihan_akun = input("Pilih akun\n1. Untuk akun pengguna\n2. Untuk admin: ")

            if pilihan_akun == '1':
                pengguna[username_baru] = {'password': password_baru, 'role': 'pengguna'}
                print("Registrasi pengguna berhasil!\n")
            elif pilihan_akun == '2':
                pengguna[username_baru] = {'password': password_baru, 'role': 'admin'}
                print("Registrasi admin berhasil!\n")
            else:
                print("Pilihan tidak valid!\n")

    elif pilihan == '2':
        print("ANDA MEMILIH FITUR LOGIN \nSILAHKAN MASUKKAN USERNAME DAN PASSWORD ANDA ")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if username in pengguna and pengguna[username]['password'] == password:
            print(f"\nLogin berhasil sebagai {username} ({pengguna[username]['role']})\n")
            
            if pengguna[username]['role'] == 'admin':
                while True:
                    print("Menu Admin: \n1. Tambah Produk \n2. Lihat Produk \n3. Edit Produk \n4. Hapus Produk \n5. Logout")
                    pilihan_admin = input("Pilih Menu: ")

                    if pilihan_admin == '1':
                        id_baru = len(produk) + 1
                        nama_baru = input("Masukkan nama produk: ")
                        harga_baru = input("Masukkan harga produk: ")

                        if harga_baru.isdigit():
                            kategori_baru = input("Masukkan kategori (membership/addons): ").lower()
                            if kategori_baru in ['membership', 'addons']:
                                produk[id_baru] = {'nama': nama_baru, 'harga': int(harga_baru), 'kategori': kategori_baru}
                                print("Produk berhasil ditambahkan!\n")
                            else:
                                print("Kategori tidak valid! Harus 'membership' atau 'addons'.\n")
                        else:
                            print("Harga harus berupa angka!\n")

                    elif pilihan_admin == '2':
                        print("\nDaftar Produk:")
                        for p_id, p in produk.items():
                            print(f"ID: {p_id}, Nama: {p['nama']}, Harga: {p['harga']}, Kategori: {p['kategori']}")
                        print()

                    elif pilihan_admin == '3':
                        id_edit = input("Masukkan ID produk yang akan diedit: ")

                        if id_edit.isdigit():
                            id_edit = int(id_edit)
                            if id_edit in produk:
                                nama_edit = input("Masukkan nama baru: ")
                                harga_edit = input("Masukkan harga baru: ")

                                if harga_edit.isdigit():
                                    kategori_edit = input("Masukkan kategori baru (membership/addons): ").lower()

                                    if kategori_edit in ['membership', 'addons']:
                                        produk[id_edit] = {'nama': nama_edit, 'harga': int(harga_edit), 'kategori': kategori_edit}
                                        print("Produk berhasil diupdate!\n")
                                    else:
                                        print("Kategori tidak valid! Harus 'membership' atau 'addons'.\n")
                                else:
                                    print("Harga harus berupa angka!\n")
                            else:
                                print("Produk tidak ditemukan!\n")
                        else:
                            print("ID produk harus berupa angka!\n")

                    elif pilihan_admin == '4':
                        id_hapus = input("Masukkan ID produk yang akan dihapus: ")

                        if id_hapus.isdigit():
                            id_hapus = int(id_hapus)
                            if id_hapus in produk:
                                del produk[id_hapus]
                                print("Produk berhasil dihapus!\n")
                            else:
                                print("Produk tidak ditemukan!\n")
                        else:
                            print("ID produk harus berupa angka!\n") 

                    elif pilihan_admin == '5':
                        print("Logout berhasil!\n")
                        break

                    else:
                        print("Pilihan tidak valid!\n")

            elif pengguna[username]['role'] == 'pengguna':
                while True:
                    print("Menu Pengguna:")
                    print("1. Lihat Produk")
                    print("2. Beli Membership")
                    print("3. Beli Addons")
                    print("4. Logout")
                    pilihan_pengguna = input("Pilih Menu: ")

                    if pilihan_pengguna == '1':
                        print("\nDaftar Produk:")
                        for p_id, p in produk.items():
                            print(f"ID: {p_id}, Nama: {p['nama']}, Harga: {p['harga']}, Kategori: {p['kategori']}")
                        print()

                    elif pilihan_pengguna == '2':
                        print("\nDaftar Membership:")
                        for p_id, p in produk.items():
                            if p['kategori'] == 'membership':
                                print(f"ID: {p_id}, Nama: {p['nama']}, Harga: {p['harga']}")
                        id_beli = input("Masukkan ID membership yang ingin dibeli: ")

                        if id_beli.isdigit():
                            id_beli = int(id_beli)
                            if id_beli in produk and produk[id_beli]['kategori'] == 'membership':
                                print(f"Anda telah membeli {produk[id_beli]['nama']} seharga {produk[id_beli]['harga']}\n")
                            else:
                                print("Membership tidak ditemukan!\n")
                        else:
                            print("ID harus berupa angka!\n")

                    elif pilihan_pengguna == '3':
                        print("\nDaftar Addons:")
                        for p_id, p in produk.items():
                            if p['kategori'] == 'addons':
                                print(f"ID: {p_id}, Nama: {p['nama']}, Harga: {p['harga']}")
                        id_beli = input("Masukkan ID addons yang ingin dibeli: ")

                        if id_beli.isdigit():
                            id_beli = int(id_beli)
                            if id_beli in produk and produk[id_beli]['kategori'] == 'addons':
                                print(f"Anda telah membeli {produk[id_beli]['nama']} seharga {produk[id_beli]['harga']}\n")
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

    elif pilihan == '3':
        print("Anda memilih untuk keluar. Terima kasih telah mengakses GYM kami!")
        break
    else:
        print("Pilihan tidak valid!\n")
