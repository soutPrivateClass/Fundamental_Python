import os
os.system("clear")



# MELAKUKAN READ ATAU MEMBACA PADA FILE EKSTERNAL


with open("data1.txt",mode="w",encoding="utf-8") as file: # ENCODING ADALAH UNTUK MENENTUKAN KARAKTER
    file.write("\nData Mahasiswa :")
with open("data1.txt",mode="a",encoding="utf-8") as file: # MODE A UNUTK MNAMBAHKAN TEXT PADA FILE EKSTERNAL
    file.write("\n-Ucup Surucup ganteng")




