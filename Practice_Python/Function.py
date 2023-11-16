import os

os.system("clear")

# FUNGSI OPERASI BILANGAN DIBAWAH INI 

def penjumlahan(angka1,angka2):
    hasil = angka1 + angka2
    print(f"Hasil = {hasil}")

def pengurangan(angka1,angka2):
    hasil = angka1 - angka2
    print(f"Hasil = {hasil}")


# BENTUK PEMANGGILAN FUNGSI SEPERTI DIBAWAH INI

penjumlahan("Haloo"," Ucup")
pengurangan(5,125)
print(pengurangan(20,5))


# FUNGSI MENGUNAKAN LIST DENGAN FOR LOOP

def bacapres(listNama):
    namaPeserta = listNama.copy()
    for nama in namaPeserta:
        print(f"Yang terhormat Bpk {nama}")

kandidat = ["Anis", "Ganjar", "Prabowo"]

bacapres(kandidat)


# FUNGI DENGAN NILAI KEMBALIAN / RETURN

def kuadrat(angka):
    hasil = angka**2
    return hasil

# BENTUK PEMANGGILAN FUNGSI

y = kuadrat(3)
print(y)
print(kuadrat(5))

# FUNGSI DENGAN DEFAULT ARGUMENT

def tambah(angka1 = 6, angka2 = 4):
    return angka1 + angka2

print(tambah())

# MENGGANTI NILAI ARGUMEN ANGKA1 SEPERTI DIBAWAH INI 

print(tambah(angka1= 4)) 

# TYPE HINT PADA FUNGSI

def pembagian(angka1:int) -> int: # INI ADALAH BENTUK INISIASI TYPE DATA
    hasil = 2**angka1
    return hasil

operasi = pembagian(5)
print(operasi)


# FUNGSI DENGAN *args
# *args MERUPAKAN DATA TUPLLE YANG HANYA BISA DILAKUKAN ITERASI  


def dataList(*args):
    nama = args[0]
    usia = args[1]
    gender = args[2]

    print(f"Nama = {nama}, Usia = {usia}, Gender = {gender}")

dataList("Ari", 21, "Laki - laki")

def count(*number): # BISA JUGA DIGANTI MENGGUNAKAN NAMA LAIN SELAIN args
    y = 0
    for data in number:
        y += data
    return y

hasil = count(1,2,3,4)
print(hasil)


# FUGSI DENGAN **kwargs
# MENGISI PARAMETER FUNGSI DENGAN KEY WORD ARGS / **kwargs

# CONTOH 1 : 

def dataMahasiswa(**key):
    name = key["name"]
    number = key["number"]
    major = key["major"]

    print(f"Name = {name}, Number = {number}, Major = {major}")

dataMahasiswa(name = "Rama", number = 12191685, major = "Informatika")

# CONTOH 2 :

def operasi(*bilangan,**key):
    x = 0
    if key["option"] == "penjumlahan":
        for angka in bilangan:
            x += angka
        print(f"Hasil penjumlahan = {x}")
    elif key ["option"] == "perkalian":
        y = 1
        for angka in bilangan:
            y *= angka
        print(f"Hasil perkalian = {y}")
    else:
        print("Operasi tidak valid")


operasi(1,2,3,4, option = "penjumlahan")
operasi(1,2,3,option = "perkalian")

# FUNGI ANONYMOUS DAN LAMBDA

dataKuadrat = lambda angka : angka**2
print(f"Data lambda kuadrat = {dataKuadrat(2)}")

listNama = ["Rama", "Abi"]

listNama.sort(key = lambda nama : len(nama))
print(f"Ini hasil lambda = {listNama}")


def pangkat(n):
    return lambda angka:angka**n

hasil = pangkat(2)(3)
print(hasil)

