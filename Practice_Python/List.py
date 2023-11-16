# ---------- LIST ADALAH KUMPULAN DATA DALAM PYTHON --------------

# KUMPULAN DATA NUMBERS
dataAngka = [20,1,3,9,10,3,4,5]
print(dataAngka)

# KUMPULAN DATA STRING
dataStr = ["Ucup", "Otong", "Odah"]
print(dataStr)

# KUMPULAN DATA BOOLEAN 
dataBool = [True, False, True, False]
print(dataBool)

# KUMPULAN CAMPURAN
dataMix = ["Ucup" , "membeli", "tahu", 2, "itu", True]
print(dataMix)

## ALTERNATIF MEMBUAT LIST
dataRange = range(0,10,2) # (Dari 0, sampai 9, dengan jarak atau kelipatan 2)
dataList = list(dataRange)
print(dataList)

## MENGGUNAKAN FOR LOOP
data = [i**2 for i in range(0,10)]
print(f"Ini menggunakan for loop = {data}")

## MMENGGUNAKAN FOR DAN IF 
data = [i for i in range(0,10) if i != 5]
print(f"Ini menggunakan For dan IF = {data}")

## MMENGGUNAKAN FOR DAN IF ANGKA BILANGAN GENAP
data = [i for i in range(0,10) if i%2 == 0]
print(f"Ini menggunakan For dan IF bilangan genap = {data}")

## MMENGGUNAKAN FOR DAN IF ANGKA BILANGAN GANJIL
data = [i for i in range(0,100) if i%2 == 1]
print(f"Ini menggunakan For dan IF bilangan ganjil = {data}")


### MANIPULASI LIST 
data = ["Rama", "Asep"] ### MENGAMBIL DATA INDEX KE 1
print(data[0])

print(data[-1]) ### MENGMBIL DATA INDEX PALING TERAKHIR

panjangData = len(data) ### CEK PANJANG DATA
print(panjangData)

data.insert(2,"Dudung") ### MENAMBAHKAN ITEM PADA INDEX KE 2 PADA LIST
print(data)

data.append("Ucup") ### MENAMBAHKAN ITEM PADA INDEX PALING AKHIR PADA LIST
print(data)

dataBaru = ["Jarwo", "Sopo"]
data.extend(dataBaru) ### MENNGGABUNGKAN 2 BUAH LIST  
print(data)

data[0] = "joe" ### MERUBAH DATA INDEX KE 0
print(data)

data.remove("joe") ### MENGHAPUS DATA DARI LIST, HARUS DIPERHATIKAN CAMEL CASE
print(data)

data.pop() ### MENGHAPUS DATA PALING AKHIR PADA LIST
print(data)

longData = len(data)
print(longData)

#### DUPLICATE DATA LIST KEDALAM MEMORY YANG BERBEDA ATAU REFRENSI YANG BERBEDA

dataAngka.sort()
a = dataAngka.copy()
print(f"Data angka = {dataAngka}")
print(f"Data a = {a}") 

print(f"Address Data angka = {hex(id(dataAngka))} ")
print(f"Address A = {hex(id(a))} ")