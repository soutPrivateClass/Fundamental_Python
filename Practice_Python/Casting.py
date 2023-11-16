# CASTING MERUBAH DATA KEDALAM TIPE LAIN

# MERUBAH DATA INTEGER
dataInt = 298

dataStr = str(dataInt) # MERUBAH DALAM BENTUK INTEGER
dataFloat = float(dataInt) # MERUBAH DALAM BENTUK FLOAT ATAU DESIMAL
dataBoolean = bool(dataInt) # BERNILAI FALSE JIKA MEMILIKI NILAI 0 
print ("Data String = ", dataStr, "| Bertipe = ", type(dataStr))
print ("Data Float = ", dataFloat, "| Bertipe = ", type(dataFloat))
print ("Data Boolean = ", dataBoolean, "| Bertipe = ", type(dataBoolean))

print("=================================================================")

# MERUBAH DATA FLOAT
dataFloat = 23.8

dataInt = int(dataFloat)
dataStr = str(dataFloat)
dataBoolean =  bool(dataFloat)
print ("Data Integer = ", dataInt, "| Bertipe = ", type(dataInt))
print ("Data String = ", dataStr, "| Bertipe = ", type(dataStr))
print ("Data Boolean = ", dataBoolean, "| Bertipe = ", type(dataBoolean))

print("=================================================================")

# MERUBAH BOOLEAN
dataBoolean = True

dataInt = int(dataBoolean)
dataStr = str(dataBoolean)
dataFloat = float(dataBoolean)
print ("Data Integer = ", dataInt, "| Bertipe = ", type(dataInt))
print ("Data String = ", dataStr, "| Bertipe = ", type(dataStr))
print ("Data Float = ", dataFloat, "| Bertipe = ", type(dataFloat))

print("=================================================================")

# MERUBAH DATA STRING
dataStr = "129"

dataInt = int(dataStr) # MERUBAH DALLAM BENTUK INTEGER
dataFloat = float(dataStr) # MERUBAH DALAM BENTUK FLOAT
dataBoolean = bool(dataStr) # BERNILAI FALSE JIKA MMILIKI DATA KOSONG
print ("Data Integer = ", dataInt, "| Bertipe = ", type(dataInt))
print ("Data Float = ", dataFloat, "| Bertipe = ", type(dataFloat))
print ("Data Boolean = ", dataBoolean, "| Bertipe = ", type(dataBoolean))
