dataAngka = [2,24,32,44,55,65,74]


print("===========FOR==========")
for i in dataAngka:
    print(f"Angka = {i}")



print("========FOR & RANGE======")
limit = len(dataAngka)

for i in range(limit):
    print(f"Angka = {dataAngka[i]}")



print("==========WHILE==========")
i = 0

while i < limit:
    print(f"Angka = {dataAngka[i]}")
    i += 1


print("=====LIST COMPREHENSION=====") ## SUGGESTION MENGGUNAKAN INI KARENA LEBIH SIMPEL

[print(f"Data ke = {i**2}")for i in dataAngka]


print("==========ENUMARET==========")
for i,d in enumerate(dataAngka):
    print(f"Index ke = {i}, Data = {d}")