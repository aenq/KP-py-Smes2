Banyak_mahasiswa = 4
print("Masukkan banyak mahasiswa:", Banyak_mahasiswa)

for i in range(Banyak_mahasiswa):
    print("Mahasiswa ke-", i+1)
    for r in range(4):
        if (r == 0):
            mk = str(input("Konsep Pemrograman      :",))

        elif (r == 1):
            mk = str(input("Logika Informatika      :"))

        elif (r == 2):
            mk = str(input("Kalkulus                :"))

        elif (r == 3):
            mk = str(input("Bahasa Inggris          :"))