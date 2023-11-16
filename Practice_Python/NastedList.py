# NASTED LIST / LIST BERSARANG

peserta1 = ["Jaems",27,"Laki - laki"]
peserta2 = ["Michael",29,"Laki - laki"]
peserta3 = ["Angel",22,"Perempuan"]


## CARA MANUAL / NOOB
listPeserta = [peserta1,peserta2,peserta3]
print(f"Peserta 1\t= {peserta1}\nPeserta 2\t= {peserta2}\nPeserta 3\t= {peserta3}\n")


## CARA ADVANCE / GGWP
for i in listPeserta:
    print(f"Name\t= {i[0]}\nAge\t= {i[1]}\nGender\t= {i[2]}\n")

### CARA COPY MENGGUNAKAN DEEP COPY SAAT MENGGUNAKAN NASTED LIST

from copy import deepcopy ### JANGAN LUPA DI IMPORT DARI LIBRARY

duplicateData = deepcopy(listPeserta) 
print(f"Ini adalah data duplikat = {duplicateData}")

print(f"Address original data =\t{hex(id(listPeserta[0]))}")
print(f"Address copied data =\t{hex(id(duplicateData[0]))}")
