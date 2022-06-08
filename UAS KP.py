""" print("//Soal Nomor 1///")
print("")

Mahasiswa = ["Mahasiswa"]
Total_Pertemuan = 28

while True:
    Jumlah_Kehadiran = int(input("Masukkan Jumlah Kehadiran:"))
    if Jumlah_Kehadiran>=(78/100*Total_Pertemuan):
         print("Mahasiswa tersebut layak mengikuti UAS")
         print("")
    else:
        print("Mahasiswa tidak layak mengikuti UAS")
        print("")

"""

print("/// Soal Nomor 2///")
List_Idola = []
Idola_saya = ["Kim Jong Un", "Soeharto", "Donald Trump", "Gayus Tambonan"]
for x in (List_Idola+Idola_saya):
    print(x)

print("")
print("///Soal Nomor 3///")

while True:
    print("")
    Nama_Karyawan = str(input("Nama Karyawan :"))
    Jumlah_jam_lembur = int(input("Jumlah jam lembur:"))
    Golongan = int(input("Golongan :"))

    if Golongan == 1:
        print("Upah lembur yang diterima:",Jumlah_jam_lembur*25000)
    elif Golongan == 2:
        print("Upah lembur yang diterima:",Jumlah_jam_lembur*40000)
    elif Golongan == 3:
        print("Upah lembur yang diterima:", Jumlah_jam_lembur*50000)
    else:
        print("input salah")
