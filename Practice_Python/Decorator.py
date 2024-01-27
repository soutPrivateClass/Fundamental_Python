import os

os.system('clear')

"""
DECORATOR ADALAH FUNGSI DENGAN SIMBOL @ UNTUK MEMUDAHKAN DALAM PEMANGGILAN FUNGSI DIDALAM & DILUAR FUNGSI

DECORATOR BIASA DIGUNAKAN UNTUK WEBSITE DEVLOPMENT KHUSUSNYA UNTUK BAKCEND
"""

# CONTOH TANPA MENGGUNAAKAN DECORATOR DALAM PEMANGGILAN FUNGSI DIDALAM FUNGSI SEHINGGA KURANG EFISIEN :
def data(nama='Joko'):
    print(f"Ini adalah {nama}")

    def valid():
        return "Data valid"
    
    def invalid():
        return "Data invalid"
    
    if nama == 'Joko':
        return valid
    else:
        return invalid
    
cekData = data() # HARUS ASSIGN TERLEBIH DAHULU DALAM SEBUAH VARRIABEL UNTUK MEMANGGIL FUNGSI
print(f"{cekData()}\n")

# CONTOH TANPA MENGGUNAAKAN DECORATOR DALAM PEMANGGILAN FUNGSI DILUAR FUNGSI SEHINGGA KURANG EFISIEN :
def word():
    return "Selamat Pagi"

def person(nama,fungsi):
    print(f"Hallo {nama} {fungsi}\n")

person("Joko",word())

# CARA DIATAS DINILAI KURANG EFEKTIF
# AKAN LEBIH EFEKTIF MENGGUNAKAN DECORATOR SEPERTI DIBAWAH INI :

# CONTOH PERTAMA :
def word(fungsi):
    def aritmatika():
        print("Ini adalah bentuk aritmatika penjumlahan :")
        fungsi()
        print("Terimakasih program selesai")
    return aritmatika

@word  # PENAMBAHAN DECORATOR 
def word2():
    print(f"1 + 1 = 2")

word2()

# CONTOH KEDUA :
dataKaryawan = {'name' : 'Roy',
                'age' : 22,
                'valid' : True}

def x(fungsi):
    def y(*args, **kwargs):
        if args[0]['valid'] != False:
            return fungsi(*args, *kwargs)
        else:
            print("Data tidak valid")
    return y

@x
def cek(karyawan):
    print("Pesan berhasil dikirim")

cek(dataKaryawan)
