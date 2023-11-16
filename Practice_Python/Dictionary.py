"""
DICTIONARY ADALAH ASOSIATIF ARRAY
YANG MENGGUNAKAN IDENTIFIER UNTUK MENGAKSES DATA DIDALAMNYA
DICTIONARY MENGGUNAKAN {KEY1 : VALUE} SEBAGAI IDENTIFIER DATA DIDALAMNYA
"""

print("\n==========================DICTIONARY=============================\n")
number = [2,3434,45,2,23,42,434,534,56]
dataDict = {
    'rma' : 'Rama', 
     'jj' : 'Jeje',
     'fkh' : 'Fakih',
     #'number' : number # BISA JUGA UNTUK MENAMPUNG DATA LIST
}

print(dataDict)


print("\n====================OPERATOR DICTIONARY==========================\n")
# OPERATOR DICTIONARY

# PANJANG DICTIONARY
longDict = len(dataDict)
print(f"Panjang data dictionary = {longDict}")

# CEK ADA ATAU TIDAKNYA DATA
data = "jj"
isExist = data in dataDict
print(f"Apakah terdapat data {data} ? {isExist}")

# READ DATA DICTIONARY MENGGUNAKAN GET
print(dataDict.get('jj'))

# UPDATE DATA
dataDict.update({'hrm':'Herman'}) # JIKA DATA TIDAK ADA MAKA AKAN SECARA OTOMATIS DITAMBAHKAN PADA DICTIONARY
print(dataDict)

# DELETE DATA
del dataDict['hrm']
print(dataDict)

print("\n====================LOOPING DICTIONARY==========================\n")


# CARA DIBAWAH INI HANYA AKAN MENGHASILKAN NILAI KEY
# MENGGUNAKAN CARA BASIC

keys = dataDict.keys()
print(keys)

# MENGGUNAKAN FOR LOOP
for key in dataDict.keys():
    print(key)

print(70*"-")

# CARA DIBAWAH INI HANYA AKAN MENGHASILKAN NILAI VALUE
# MENGGUNAKAN CARA BASIC

value = dataDict.values()
print(value)

# MENGGUNAKAN FOR LOOP

for value in dataDict.values():
    print(value)

print(70*"-")

# CARA DIBAWAH INI AKAN MENAMPILKAN KEYS & VALUES
# MENGGUNAKAN CARA BASIC

item = dataDict.items()
print(item)

# MENGGUNAKAN CARA FOR LOOP

for key,value in dataDict.items():
    print(f"Key = {key} | Value = {value}")


print("\n=========================COPY DICTIONARY==========================\n")


dataBaru = dataDict.copy()
for data in dataBaru.items():
    print(data)


print("\n=========================POP DICTIONARY==========================\n")

# DIBAWAH INI AKAN MENTRANSFER DATA VALUE KEDALAM VARIABEL BERDASARKAN KEY

trashData = dataBaru.pop('jj') # DATA DENGAN KEY 'JJ' AKAN DITRANSFER KEDALAM VARIABEL TRASH DATA
print(dataBaru)
print(trashData)

# DIBAWAH INI AKAN MENTRANSFER DATA ITEM KEDALAM VARIABEL
draft = dataBaru.popitem() # AKAN MENTRRANSFER DATA ITEM YANG PALING TERAKHIR DARI DATA BARU
print(dataBaru)
print(draft)

print("\n========================MULTI DICTIONARY==========================\n")

# IMPORT DULU DATETIME PADA LIBRARY
import datetime

mahasiwa1 = {
    'nama' : 'Ucup Surucup',
    'NIM' : '12191685',
    'SKS' : 140,
    'beasiswa' : True,
    'TTL' : datetime.datetime(2000,10,10)
}
mahasiwa2 = {
    'nama' : 'Otoong Surotong',
    'NIM' : '12191698',
    'SKS' : 130,
    'beasiswa' : False,
    'TTL' : datetime.datetime(2003,2,3)
}
mahasiwa3 = {
    'nama' : 'Jack',
    'NIM' : '12191609',
    'SKS' : 120,
    'beasiswa' : False,
    'TTL' : datetime.datetime(2009,1,8)
}

dataMahasiswa = {
    'MAH001' : mahasiwa1,
    'MAH002' : mahasiwa2,
    'MAH003' : mahasiwa3
}

# SYNTAX :>(VALUE) UNTUK RATA KANAN 
print(F"{'KEY':<6} {'NAMA':<17} {'NIM':<11} {'SKS':<3} {'BEASISWA':<9} {'TTL':>5}")
print('-'*70)
for mahasiswa in dataMahasiswa:
    KEY = mahasiswa
    NAMA = dataMahasiswa[KEY]['nama']
    NIM = dataMahasiswa[KEY]['NIM']
    SKS = dataMahasiswa[KEY]['SKS']
    BEASISWA = dataMahasiswa[KEY]['beasiswa']
    TTL = dataMahasiswa[KEY]['TTL'].strftime('%x') # .STRFTIME UNTUK MEMBUAT FORMAT TANNGGAL EX : 01/08/09

    print(f"{KEY:<6} {NAMA:<17} {NIM:<11} {SKS:<3} {BEASISWA:^9} {TTL:>5}")

