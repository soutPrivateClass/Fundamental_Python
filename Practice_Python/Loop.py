# FOR LOOP

# LIST

dataAngkaList = [1,2,3,4,5] # DATA 1 SAMPAI 5
print(dataAngkaList)
for i in dataAngkaList:
    print(f"Data ke -> {i}")

print(20*"=")

# RANGE 

dataAngkaRange = range(5)
for i in dataAngkaRange:
    print(f"Data ke -> {i}") 

print(20*"=")

dataAngkaRange = range(1,5) # Data diulang sebanyak 1 - 5 kali
for i in dataAngkaRange:
    print(f"Sujud Ramadhan") 

print(20*"=")

# WHILE LOOP

angka = 0

while angka <5:
    angka += 1
    if angka == 3:
        print(f"Data ke -> {angka} dan Ini adalah nomor faavoritku, jadi sampai sini aja ya")
        break
    print(f"Data ke -> {angka}")

print("Cukup")