number = [90,1,2,3,4,8,5,6,7,7,8,9,10]


print(f"Data angka = {number}")


# MENGHITUNG KUANTITAS DATA DALAM SATU LIST

jumlahData_3 = number.count(7)
print(f"Total data 3 dalam list number adalah = {jumlahData_3}")

jumlahData_4 = number.count(4)
print(f"Total data 4 dalam list number adalah = {jumlahData_4}")


## CEK DATA PADA INDEX BERAPA

dataNama = ["Ucup", "Ujang", "Jarwo", "Dudung"]
print(f"Data nama = {dataNama}")

dataUcup = dataNama.index("Ucup")
print(f"Data 'Ucup' ada pada index ke - {dataUcup}")

### MENGRUTUKAN DATA LIST (SORTIR)

number.sort()
print(f"Data sortir nomor = {number}")

dataNama.sort()
print(f"Data sortit nama = {dataNama}")

#### SORTIR REVERS (TERBALIK)

number.reverse()
dataNama.reverse()

print(f"Ini adalah data reverse number = \n{number}\nIni adalah data reverse nama = \n{dataNama}")
