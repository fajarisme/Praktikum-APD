pengguna = {}
produk = {
    1: {'nama': 'Membership Bulanan', 'harga': 300000, 'kategori': 'membership'},
    2: {'nama': 'Air Mineral', 'harga': 10000, 'kategori': 'addons'},
    3: {'nama': 'Steroid', 'harga': 500000, 'kategori': 'addons'},
    4: {'nama': 'Protein Powder', 'harga': 150000, 'kategori': 'addons'}
}

def register(username_baru, password_baru, pilihan_akun):
    if username_baru in pengguna:
        print("Username sudah terdaftar, silakan login atau gunakan username lain!\n")
    else:
        if pilihan_akun == '1':
            pengguna[username_baru] = {'password': password_baru, 'role': 'pengguna'}
            print("Registrasi pengguna berhasil!\n")
        elif pilihan_akun == '2':
            pengguna[username_baru] = {'password': password_baru, 'role': 'admin'}
            print("Registrasi admin berhasil!\n")
        else:
            print("Pilihan tidak valid!\n")

def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    
    if username in pengguna and pengguna[username]['password'] == password:
        print(f"\nLogin berhasil sebagai {username} ({pengguna[username]['role']})\n")
        if pengguna[username]['role'] == 'admin':
            menu_admin()
        elif pengguna[username]['role'] == 'pengguna':
            menu_pengguna()
    else:
        print("Login gagal! Username atau password salah.\n")
def lihat_produk_rekursif(index=0):
    keys = list(produk.keys())
    if index < len(keys):
        p_id = keys[index]
        p = produk[p_id]
        print(f"ID: {p_id}, Nama: {p['nama']}, Harga: {p['harga']}, Kategori: {p['kategori']}")
        lihat_produk_rekursif(index + 1)

def lihat_produk():
    print("\nDaftar Produk:")
    lihat_produk_rekursif()
    print()

def tambah_produk():
    id_baru = len(produk) + 1
    nama_baru = input("Masukkan nama produk: ")
    harga_baru = input("Masukkan harga produk: ")

    if not harga_baru.isdigit():
        print("Error: Harga harus berupa angka!\n")
        return 

    kategori_baru = input("Masukkan kategori (membership/addons): ").lower()

    if kategori_baru not in ['membership', 'addons']:
        print("Error: Kategori tidak valid! Harus 'membership' atau 'addons'.\n")
        return 

    produk[id_baru] = {'nama': nama_baru, 'harga': int(harga_baru), 'kategori': kategori_baru}
    print("Produk berhasil ditambahkan!\n")

def edit_produk(id_edit):
    if not id_edit.isdigit():
        print("Error: ID produk harus berupa angka!\n")
        return

    id_edit = int(id_edit)
    if id_edit not in produk:
        print("Error: Produk tidak ditemukan!\n")
        return

    nama_edit = input("Masukkan nama baru: ")
    harga_edit = input("Masukkan harga baru: ")

    if not harga_edit.isdigit():
        print("Error: Harga harus berupa angka!\n")
        return

    kategori_edit = input("Masukkan kategori baru (membership/addons): ").lower()
    if kategori_edit not in ['membership', 'addons']:
        print("Error: Kategori tidak valid! Harus 'membership' atau 'addons'.\n")
        return

    produk[id_edit] = {'nama': nama_edit, 'harga': int(harga_edit), 'kategori': kategori_edit}
    print("Produk berhasil diupdate!\n")

def menu_admin():
    while True:
        print("Menu Admin:\n1. Tambah Produk\n2. Lihat Produk\n3. Edit Produk\n4. Hapus Produk\n5. Logout")
        pilihan_admin = input("Pilih Menu: ")

        if pilihan_admin == '1':
            tambah_produk() 
        elif pilihan_admin == '2':
            lihat_produk()  
        elif pilihan_admin == '3':
            id_edit = input("Masukkan ID produk yang akan diedit: ")
            edit_produk(id_edit)  
        elif pilihan_admin == '4':
            id_hapus = input("Masukkan ID produk yang akan dihapus: ")
            hapus_produk(id_hapus)  
        elif pilihan_admin == '5':
            print("Logout berhasil!\n")
            break
        else:
            print("Pilihan tidak valid!\n")

def hapus_produk(id_hapus):
    if not id_hapus.isdigit():
        print("Error: ID produk harus berupa angka!\n")
        return

    id_hapus = int(id_hapus)
    if id_hapus not in produk:
        print("Error: Produk tidak ditemukan!\n")
        return

    del produk[id_hapus]
    print("Produk berhasil dihapus!\n")

def menu_pengguna():
    while True:
        print("Menu Pengguna:\n1. Lihat Produk\n2. Beli Membership\n3. Beli Addons\n4. Logout")
        pilihan_pengguna = input("Pilih Menu: ")

        if pilihan_pengguna == '1':
            lihat_produk() 
        elif pilihan_pengguna == '2':
            beli_produk('membership')
        elif pilihan_pengguna == '3':
            beli_produk('addons')
        elif pilihan_pengguna == '4':
            print("Logout berhasil!\n")
            break
        else:
            print("Pilihan tidak valid!\n")

def beli_produk(kategori):
    print(f"\nDaftar {kategori.capitalize()}:")
    for p_id, p in produk.items():
        if p['kategori'] == kategori:
            print(f"ID: {p_id}, Nama: {p['nama']}, Harga: {p['harga']}")
    
    id_beli = input(f"Masukkan ID {kategori} yang ingin dibeli: ")

    if not id_beli.isdigit():
        print("Error: ID harus berupa angka!\n")
        return

    id_beli = int(id_beli)
    if id_beli not in produk or produk[id_beli]['kategori'] != kategori:
        print(f"Error: {kategori.capitalize()} tidak ditemukan!\n")
        return

    print(f"Anda telah membeli {produk[id_beli]['nama']} seharga {produk[id_beli]['harga']}\n")

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
        password_baru = input("Masukkan password baru: ")
        pilihan_akun = input("Pilih akun\n1. Untuk akun pengguna\n2. Untuk admin: ")
        register(username_baru, password_baru, pilihan_akun)
    elif pilihan == '2':
        login()
    elif pilihan == '3':
        print("Anda memilih untuk keluar. Terima kasih telah mengakses GYM kami!")
        break
    else:
        print("Pilihan tidak valid!\n")
