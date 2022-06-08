# SOAL NO 1

Bilangan_A = -4
Bilangan_B = 2
Selisih_bilangan = (Bilangan_B - Bilangan_A)
print("Bilangan A = -4")
print("Bilangan B = 2")
print("Selisih bilangan A dan Bilangan B adalah :", Selisih_bilangan)

Bilangan_C = 10
Bilangan_D = 3
Selisih_bilangan = (Bilangan_C - Bilangan_D)
print("Bilangan C = 10")
print("Bilangan D = 3")
print("Selisih bilangan C dan Bilangan D adalah :", Selisih_bilangan)

# Soal No 2
print(60*("#"))

# Pak Raden memiliki sebuah kantin yang menjual berbagai makanan kecil. Harga makanan 
#yang ia jual bervariasi mulai dari Rp. 500 hingga Rp. 10.000. Para pelanggan Pak Raden 
#beranggapan makanan yang harganya dibawah Rp 4.000 termasuk murah, yang 
#harganya diatas Rp 7.500 termasuk mahal, sedangkan yang diantaranya termasuk 
#sedang-sedang saja. 
#Untuk membantu Pak Raden menentukan sebuah harga makanan itu termasuk kriteria 
#murah, sedang, atau mahal, maka diperlukan program dengan user input sebuah harga 
#makanan, lalu mengeluarkan kalimat “Murah”, “Sedang”, atau “Mahal”.

makanan = 3000

if 500<=makanan<=4000:
    print("Harga Makanan =", makanan)
    print("Kriteria Murah")
elif 7500<=makanan<=10000:
    print("Harga Makanan =", makanan)
    print("Kriteria Mahal")
elif 4000<=makanan<=7000:
    print("Harga Makanan =", makanan)
    print("Kriteria Sedang")

makanan = 6000

if 500<=makanan<=4000:
    print("Harga Makanan =", makanan)
    print("Kriteria Murah")
elif 7500<=makanan<=10000:
    print("Harga Makanan =", makanan)
    print("Kriteria Mahal")
elif 4000<=makanan<=7000:
    print("Harga Makanan =", makanan)
    print("Kriteria Sedang")

makanan = 10000

if 500<=makanan<=4000:
    print("Harga Makanan =", makanan)
    print("Kriteria Murah")
elif 7500<=makanan<=10000:
    print("Harga Makanan =", makanan)
    print("Kriteria Mahal")
elif 4000<=makanan<=7000:
    print("Harga Makanan =", makanan)
    print("Kriteria Sedang")

# SOAL NO 3
print(100*("#"))
IPK = 3.56

if 3.51<=IPK<=4.00:
    print("Dengan Pujian")
elif 2.76<=IPK<=3.50:
    print("Sangat Memuaskan")
elif 2.00<=IPK<=2.75:
    print("Memuaskan")

