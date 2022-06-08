# Latihan 2

#NO 1
print("=== No 1 ===")
"""Buatlah program sederhana untuk mencari 
angka maksimal dari 2 buah angka masukan."""

Bil1 = 598142869
Bil2 = 598863147

if Bil1>Bil2 :
    print(Bil1, "adalah bilangan maksimal")
if Bil2>Bil1 :
    print(Bil2, "adalah bilangan maksimal")

#NO 2
print("=== No 2 ===")
"""Buatlah program sederhana untuk menghitung keliling 
lingkaran dan luas lingkaran.
Dengan pilihan:
- Jika memasukan angka 1 maka menghitung keliling lingkaran, 
- Jika memasukan angka 2 maka menghitung luas lingkaran. 
Selain itu juga ada masukan nilai untuk jari – jari."""

phi = 3.14 
print("phi = 3.14")
r = 18 
print("r = 18")
d = 2 * r 
print("d = 2 * r")
Keliling = phi * d 
print("Keliling = phi * d")
L = phi * (r*r) 
print("L = phi *(r*r)")

memasukkan = 2
print("memasukkan = ", memasukkan)

if memasukkan == 1:
    print("Keliling lingkaran adalah", Keliling)
elif memasukkan == 2:
    print("Luas lingkaran adalah", L)
else:
    print("Masukkan nilai jari-jari!")

# No 3
print("=== No 3 ===")

"""sebuah usaha fotokopi memiliki aturan seperti berikut :
- Jika yang fotokopi statusnya adalah Langganan, maka berapa 
lembar pun dia fotokopi harga per lembarnya adalah Rp. 100
- Jika yang fotokopi statusnya Bukan Langganan, maka jika dia
fotokopi kurang dari 100 lembar, harga per lembarnya adalah Rp. 150.
sedangkan jika lebih atau sama dengan 100 lembar, maka harga
per lembarnya adalah Rp. 125
 a. buatlah flowchar untuk menghitung total harga jika seseorang memfotokopi sejumlah lembar
 b. buatlah kode program """

status= input("Langganan: ")
Jumlah_lembar = 50

if status == "Langganan":
     total_pembayaran = Jumlah_lembar * 100
     print("Total pembayarannya adalah ", total_pembayaran)
elif status == "Bukan Langganan":
    if Jumlah_lembar <=100:
        total_pembayaran = Jumlah_lembar * 150
        print("Total pembayarannya adalah ", total_pembayaran)
    else:
        total_pembayaran = Jumlah_lembar * 125
        print("Total pembayarannya adalah", total_pembayaran)