# LATIHAN UNTUK TAMBAH DATA MENGGUNAKAN DICTIONARY


import datetime
import os
import string
import random

templateMahasiswa = {
    'name' : 'bla bla',
    'number' : '0000000',
    'faculty' : 'bla bla',
    'born' : datetime.datetime(1111,11,11)
}


kamusMahasiswa =  {}

while True:
    os.system("clear")
    print("\nFORM BIODATA MAHASISWA\n")

    dataMahasiswa = dict.fromkeys(templateMahasiswa.keys())
    dataMahasiswa['name'] = input("Masukkan nama = ")
    dataMahasiswa['number'] = input("Masukkan nomor mahasiswa = ")
    dataMahasiswa['faculty'] = input("Fakultas = ")
    year = int(input("Masukkan angka tahun lahir (YYYY) = "))
    month = int(input("Masukkan angka bulan lahir (MM) = "))
    day = int(input("Masukkan tanggal lahir (DD) = "))
    dataMahasiswa['born'] = datetime.datetime(year,month,day)

    
    
    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(3)))
    kamusMahasiswa.update({KEY:dataMahasiswa})

    print(f"\nKEY | Name | Number | Faculty | Born |")
    for i in kamusMahasiswa:
        print(f"{i} | {kamusMahasiswa[i]['name']} | {kamusMahasiswa[i]['number']} | {kamusMahasiswa[i]['faculty']} | {kamusMahasiswa[i]['born'].strftime('%x')} |")

    isNext = input("\nApakah ingin lanjut ? (y/n) = ")
    if isNext == "n":
        break
    elif isNext == "N":
        break
print("Akhir dari program, Terima kasih")


