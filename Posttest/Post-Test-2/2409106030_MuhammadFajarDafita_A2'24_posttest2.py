nama = input("Masukkan nama lengkap kalian = ")
nim = input("Masukkan NIM kalian = ")

beras = int(input("Masukkan harga beras = "))
diskon = {
    "diskon1" : 0.11,
    "diskon2" : 0.14,
    "diskon3" : 0.17
}

diskon1 = beras * diskon["diskon1"]
diskon2 = beras * diskon["diskon2"]
diskon3 = beras * diskon["diskon3"]

mawar = beras - diskon1
sania = beras - diskon2
maknyus = beras - diskon3

print(f"{nama} dengan NIM {nim} ingin membeli beras seharga {beras}")
print(f"Jika dia membeli beras Mawar ia harus membayar {mawar} setelah mendapat diskon 11%")
print(f"Jika dia membeli beras Sania ia harus membayar {sania} setelah mendapat diskon 14%")
print(f"Jika dia membeli beras Maknyus ia harus membayar {maknyus} setelah mendapat diskon 17%")