# OPERASI ARITMATIKA

a = 5
b = 3

# OPERASI TAMBAH
hasil = a + b
print(a, '+', b, '=' , hasil)

# OPERRASI KURANG
hasil = a - b
print(a, '-', b, '=' , hasil)

# OPERASI PERKALIAN
hasil = a * b
print(a, '*', b, '=' , hasil)

# OPERASI PEMBAGIAN
hasil = a / b
print(a, '/', b, '=' , hasil)  

# OPERASI EKSPONEN / PANGKAT
hasil = a ** b # ARTINYA ADALAH A PANGKAT B 
print(a, '**', b, '=', hasil)

# OPERRASI MODULUS / SISA BAGI
hasil = a % b
print(a, '%', b, '=', hasil)

# OPERASI FLOOR DIVISION / PEMBULATAN
hasil = a // b
print(a, '//', b, '=', hasil)

# OPERASI ASSIGNMENT
a += 1
print(a)
a -= 5
print(a)
a *= 100
print(a)
a /= 2
print(a)
a %= 27
print(a)
a //= 3
print(a)
a **= 2
print(int(a)) #INI SAYA CONVERT KEDALAM INT

# OPERASI PRIORITAS / MANA YANG DIDAHULUKAN
'''
YANG DI PRIORITASKAN TERLEBIH DAHULU ADALAH
1. TANDA ()
2. OPERASI EKSPONEN **
3. PERKALAN DLL * / ** % //
4. TAMBAH & KURANG
'''


x = 3
y = 2   
z = 4

hasil = x ** y * z + x / y - y % z // x
print(hasil)