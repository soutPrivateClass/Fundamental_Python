# STRING

nama = "Rmadhan" # TIDAK PERLU MELAKUKAN CASTING TYPE DATA
ttl = 20
gabungan = f"Sujud {nama} {ttl}"
print(gabungan, type(gabungan))

# BOOLEAN

bool = True
format = f"Boolean = {bool}"
print(format)

# INTEGER

int = 23413323
format = f"Angka bilangan bulat = {int}"
print(format)

# RIBUAN
# MENAMBAHKAN KOMA SECARA OTOMATIS

angkaRibuan = 23413323
format = f"Nilai = {angkaRibuan:,}"
print(format)

# DECIMAL
# MENGAMBIL 2 ANGKA DIBELAKANG KOMA

decimal = 2341.3323
format = f"Decimal = {decimal:.2f}"
print(format)

# ANGKA (-) DAN (+)

minus = -250
plus = 250
format = f"Aangka minus = {minus}"
format2 = f"Angka plus = {plus}"

print(format)
print(format2)

# PERSEN (%)

nilai = 1.98
format = f"Nilai persentase = {nilai:.2%}"
print(format)

# BISA MELAKUKAN OPERASI ARITTMATIKA

hargaBuku = 5000
jumlahBuku = 5
format = f"Harga buku = {hargaBuku:,}/pcs, Jumlah buku {jumlahBuku}, Total belanja {hargaBuku*jumlahBuku:,}"
print(format)

# FORMAT ANGKA (BINARRY, OCTAL, HEXADCIMAL)

angka = 255
formatBinarry = f"Binarry = {bin(angka)}"
formatOctal = f"Octal = {oct(angka)}"
formatHexadecimal = f"Hexadecimal = {hex(angka)}"

print(formatBinarry)
print(formatOctal)
print(formatHexadecimal)

# STRING MULTILINE & ALIGNMENT

nama = "Sujud Ramadhan"
usia = 22
hobi = "Berenang"
# MEMBUAT HASIL OUTPUT JADI RATA KANAN DENGAN LEBAR 15
dataMahasiswa = f"""
Nama : {nama:>15} 
Usia : {usia:>15}
Hobi : {hobi:>15}
"""
print(dataMahasiswa)