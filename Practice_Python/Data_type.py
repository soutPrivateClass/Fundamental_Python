# TIPE DATA INTEGER
data1 = 125
print("- Data 1 = ", data1)
print("- Bertipe = ", type(data1))

print("--------------------------")

# TIPE DATA FLOAT
data2 = 1.5
print("- Data 2 = ", data2)
print("- Bertipe = ", type(data2))

print("---------------------------")

# TIPE DATA STRING
data3 = "Sujud Ramdhan"
print("- Data 3 = ", data3)
print("- Bertipe ", type(data3))

print("---------------------------")

# TIPE DATA BOOLEAN
# BISA TRUE BISA FALSE
data4 = True
print("- Data 4 ", data4)
print("- Bertipe ", type(data4))


print("---------------------------")


# TIPE DATA KOMPLEKS
data_complex = complex(5,6)
print("- Data kompleks = ", data_complex)
print("- Bertipe = ", type(data_complex))

print("---------------------------")

from ctypes import c_double # IMPORT DARI LIBRARY C

data_c_double = c_double(23.98767)
print("- Data = ", data_c_double)
print("- Bertipe = ", type(data_c_double))