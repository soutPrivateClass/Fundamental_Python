import os as reset
import numpy as np

reset.system("clear")

# NUMPY ADALAH SALAH SATU PACKAGE DARI PYTHON ATAU PIP UNTUK MENGOLAH OPERASI ARITMATIKA

matrixA = np.array([(3,2,3),(4,5,7),(2,9,6)])
print(f"Matrix A =\n{matrixA}\n")

matrixKuadrat = matrixA**2
print(f"Matrix A ^2 =\n{matrixKuadrat}") # KUADRAT DARI KOMPONEN MATRIX A

matrixB = np.zeros((3,3)) # MEMBUAT MATRIX KOSONG DENGAN 3 KOLOM DAN 3 BARIS
print(f"\nMatrix kosong B =\n{matrixB}\n")

matrixC = np.ones((3,3)) # MEMBUAT MATRIX DENGAN KOMPONEN ANGKA 1 MENGGUNAKAN 3 KOLOM DAN 3 BARIS
print(f"Matrix C komponen angka 1 =\n{matrixC}")

jumlah = matrixA + matrixKuadrat + matrixB + matrixC
print(f"\nHasil keseluruhan =\n{jumlah}")