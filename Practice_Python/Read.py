import os
os.system("clear")

# MELAKUKAN READ ATAU MEMBACA PADA FILE EKSTERNAL

# CARA 1

file = open("Data.txt", mode="r") # MEMBUKA FILE
print(file.read()) # MEMBACA ATAU MELAKUKAN READ FILE 

file.close() # MENUTUP FILE

print("\n======================\n")

# CARA 2 : LEBIH GG 

with open ("Data.txt",mode="r") as file:
    print(file.read())
