# OPERASI KOMPARASI

a = 4
b = 2

# LEBIH BESAR DARI >
hasil1 = a > b
hasil2 = b > a
print('a > b = ',hasil1)
print('b > a = ',hasil2)

print('\n========================\n')

# LEBIH BESAR SAMADENGAN >=
hasil1 = a >= b
hasil2 = b >= a
print('a >= b = ',hasil1)
print('b >= a = ',hasil2)

print('\n========================\n')

# KURANG DARI <
hasil1 = a < b
hasil2 = b < a
print('a < b = ',hasil1)
print('b < a = ',hasil2)

print('\n========================\n')

# KURANG DARI SAMADENGAN <=
hasil1 = a <= b
hasil2 = b <= a
print('a <= b = ',hasil1)
print('b <= a = ',hasil2)

print('\n========================\n')

# 'is' sebagai komparasi objek (hanya untuk komparasi dua buah objek yang tersimpan pada memori yang berbeda atau sama)
x = 5
y = 5
# x dan y memiliki nilai yang sama, maka akan disimpan pada memory yang sama dan menghasilkan nilai TRUE
hasil = x is y
print('nilai x = ', x,hex(id(x)),'\nnilai y = ',y,hex(id(y)))
print(hasil)

print('\n========================\n')

# 'is not' kebalikan dari notasi is
x = 5
y = 5 
hasil = x is not y
print('nilai x = ', x,hex(id(x)),'\nnilai y = ',y,hex(id(y)))
print(hasil)