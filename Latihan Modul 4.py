print("===A===")
"""A. Dari profile tersebut terjemahkan masing – masing profile (Tweedledoom dan 
Tweedledee) kedalam object python, kelompokan berdasarkan mutable dan 
immutable object, Jelaskan mengapa harus demikian."""

nama1,nama2 = "Tweedledoom", "Tweedledee" #Immutable
"""Pertama buat tuple nama, memakai tuple karena sebuah nama tidak dapat diubah atau immutable"""
Tanggal_lahir = ("1861-10-23") #Immutable
"""Kedua memasukkan tgl lahir menggunakan tuple, karna tgl lahir tidak dapat diubah"""

Kemampuan = (["Bersyair", "Menyanyi", "Suka berpura-pura"]) #Mutable
"""Ketiga memasukkan kemampuan menggunakan list, karena kemampuan itu bisa berubah
dan list ini cocok karena merupakan mutable object"""

print("Nama :", nama1,"dan", nama2)
print("Tanggal lahir :", Tanggal_lahir)
print("Kemampuan :")
for x in Kemampuan:
    print(x)
print("===B===")
""""Dikemudian hari kemampuan tweedledee berubah, dari bersyair menjadi memanah"""

print("Nama :", nama2)
print("Tanggal lahir :", Tanggal_lahir)
Kemampuan = ("Menyanyi", ["Bersyair"], "Suka berpura-pura")
Kemampuan [1][0] = ("Memanah")
print ("Kemampuan :", Kemampuan)

print(100*(""))
print("Latihan Set")
Hari_Pertama = {"Keju","Tepung","Garam","Gula","Coklat" }
Hari_Kedua = {"Garam","Gula","Coklat","Kecap"}

print(100*(""))
print("a. buat 2 set")
Hari_Pertama = {"Keju","Tepung","Garam","Gula","Coklat" }
print("Hari Pertama =", Hari_Pertama)
Hari_Kedua = {"Garam","Gula","Coklat","Kecap"}
print("Hari Kedua =", Hari_Kedua)

print(100*(""))
print("b. tambahkan keju")
Hari_Kedua = {"Garam","Gula","Coklat","Kecap"}
Hari_Kedua.add("Keju")
print(Hari_Kedua)

print(100*(""))
print("c. cari barang yang sama")
Hari_Pertama = {"Keju","Tepung","Garam","Gula","Coklat" }
Hari_Kedua = {"Garam","Gula","Coklat","Kecap"}
print(Hari_Pertama.intersection(Hari_Kedua))

print(100*(""))
print("d. cari barang yg dibeli di hari pertama tetapi tidak dibeli dihari kedua")
print(Hari_Pertama - Hari_Kedua)

print(100*(""))
print("e. hapus garam pada hari pertama")
Hari_Pertama = {"Keju","Tepung","Garam","Gula","Coklat" }
Hari_Pertama.remove("Garam")
print(Hari_Pertama)

print(100*(""))
print("f. cari barang yang dibeli dihari kedua tetapi tidak dibeli dihari pertama")
Hari_Pertama = {"Keju","Tepung","Garam","Gula","Coklat" }
Hari_Kedua = {"Garam","Gula","Coklat","Kecap"}
print(Hari_Kedua-Hari_Pertama)

print(100*(""))
print("g. cari barang yang tidak sama pada pembelian hari pertama dan kedua")
Hari_Pertama = {"Keju","Tepung","Garam","Gula","Coklat" }
Hari_Kedua = {"Garam","Gula","Coklat","Kecap"}
A = (Hari_Pertama-Hari_Kedua)
B = (Hari_Kedua - Hari_Pertama)
print(A.union(B))

print(100*(""))
print("h. tampilkan semua keperluan rumah tangga yg dibeli hari pertama")
print(Hari_Pertama)

print(100*(""))
print("i. tampilkan semua keperluan rumah tangga yg dibeli hari kedua")
print(Hari_Kedua)