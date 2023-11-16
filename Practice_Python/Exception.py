import os
os.system("clear")

# EXCEPTION ADALAH MEKANISME YANG DIJALANKAN UNTUK MENANGKAP ERROR RUNTIME

# CARA 1

angkaPembagi = 10

condition = True
while condition:
    try:
        dataAngka = int(input("\nMasukkan angka = "))
        hasil = angkaPembagi/dataAngka
        print(f"Hasil = {hasil}")
        condition = False
    except Exception as errorMessage: 
        print(errorMessage)

print("Akhir dari program")

# CARA 2 DENGAN FILE I/O

try:
    with open("Data2.txt","r",encoding="utf-8") as file:
        print("\nData ditemukan :")
        print(file.read())
except:
    with open("Data2.txt","w",encoding="utf-8") as file:
        print("\nData tidak ditemukan, Membuat data baru :")
        file.write("GEGE RAMA")
    with open("Data2.txt","r",encoding="utf-8") as file:
        print(file.read())
        
print("Akhir dari program")

# CARA 3 MENGGUNAKAN RAISE

from numbers import Number
def tambah(a,b):
    if not isinstance(a,Number) or not isinstance(b,Number):
        raise "Input harus angka"
    return a+b

hasil = tambah(2,3)
print(f"\nHasil dari operasi tambah adalah = {hasil}")