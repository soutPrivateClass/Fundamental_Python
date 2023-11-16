# OPERASI LOGIKA ATAU BOOLEAN 

# not, or, and xor 

# NOT (memiliki nilai kebalikan)

print('----NOT----')
a = True
b = not a # SAMA SAJA DENGAN PAKAI TANDA (=~) UNTUK ANGKA BINER / BINARY
print(b)

print('----OR-----')
# OR (MEMILIKI SAMPAI 3 SETATMENT)
a = True
b = True
c = a | b 
print(a, '|', b, '=', c)

a = True
b = False
c = a | b
print(a, '|', b, '=' ,c)

a = False
b = True
c = a | b
print(a, '|', b, '=' ,c)

a = False
b = False
c = a | b
print(a, '|', b, '=' ,c)

print('----AND-----')
# AND (MEMILIKI SAMPAI 3 SETATMENT)
a = True
b = True
c = a & b
print(a, 'AND', b, '=' ,c)

a = True
b = False
c = a & b
print(a, 'AND', b, '=' ,c)

a = False
b = True
c = a & b
print(a, 'AND', b, '=' ,c)

a = False
b = False
c = a & b
print(a, 'AND', b, '=' ,c)

print('----XOR-----')
# XOR (AKA BRNILAI TRUE JIKA SALAH SATU NILAI BERILAI TRUE, SISSANYA FALSE)
a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=' ,c)

a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=' ,c)

a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=' ,c)

a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=' ,c)


