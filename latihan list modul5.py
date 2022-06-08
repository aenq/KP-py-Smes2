print("a. Buat List")
Daftar_orang = ["William", "Kate", "Anderson", "Jame", "Mady"]
print("Daftar_orang :", Daftar_orang)

print("")
print("b. Tambahkan List")
Daftar_orang =["William", "Kate", "Anderson", "Jame", "Mady"]
Daftar_orang.append("Jones")
print(Daftar_orang)

print("")
print("c. Ubah nama Anderson menjadi Grace")
Daftar_orang = ["William", "Kate", ["Anderson"], "Jame", "Mady", "Jones"]
Daftar_orang[2][0] = "Grace"
print(Daftar_orang)

print("")
print("d. Cek Membership Thompshon")
membership = "Thompshon" in Daftar_orang
print(membership)

print("")
print("e. Urutkan sesuai abjad")
Daftar_orang = ['William', 'Kate', 'Grace', 'Jame', 'Mady', 'Jones']
print(sorted(Daftar_orang))

print("")
print("f. Tampilkan 6 orang yang telah sampai memakai for/while")
for x in (sorted(Daftar_orang)):
    print(x)

print("")
print("g. Kosongkan list")
Daftar_orang.clear()
print(Daftar_orang)