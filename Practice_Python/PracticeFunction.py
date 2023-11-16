import os

def header():
    os.system('clear')
    print(f"{'PROGRAM MENGHITUNG LUAS':^40}")
    print(f"{'DAN KELILING PERSEGI PANJANG':^40}")
    print(f"{40*'-'}")

def inputUser():
    panjang = int(input("Masukkan panjang = "))
    lebar = int(input("Masukkan lebar = "))
    return panjang,lebar

def hitungLuas(panjang,lebar):
    return panjang * lebar

def hitungKeliling(panjang,lebar):
    return 2*(panjang+lebar)

def display(message,value):
    print(f"Nilai {message} adalah = {value}")

while True:
    header()
    panjang,lebar = inputUser()
    luas = hitungLuas(panjang,lebar)
    keliling = hitungKeliling(panjang,lebar)
    display("Keliling",keliling)
    display("luas",luas)

    isNext = input("\nAPAKAH INGIN LANJUT ? (y/n) ")
    if isNext == "n":
        break
print("Akhir dari program")

