""" def nama_fungsi(parameter):
    #isi kode fungsi
    return object_variabel
    parameter boleh kosong

print("===Implementasi===")
def option():
    print("Pilih salah satu dari 3 fungsionalitas berikut:")
    print("1. Mencari Luas Persegi Panjang")
    print("2. Mencari Keliling Persegi Panjang")
    print("3. Keluar Program")
    pilihan = int(input("Masukkan pilihan anda :"))

def luas_persegi_panjang(panjang,lebar):
    luas = panjang*lebar

def keliling_persegi_panjang(panjang_lebar):
    keliling = 2*(panjang+lebar)

while(pilihan<3):
    pilihan = option()
    if(pilihan==3 | pilihan==0):
        break;
    else:
        panjang = int(input("Masukkan panjang:"))
        lebar = int(input("Masukkan lebar:"))
        if (pilihan==1):
            luas= luas_persegi_panjang(panjang,lebar)
            print("Hasil luas persegi panjang adalah %i", (luas))
        else:
            keliling = keliling_persegi_panjang(panjang,lebar)
            print("Hasil keliling persegi panjang adalah %i", (keliling) )

"""
def Menyimpan_biodata():
    print("Menyimpan Biodata")
    print("")
    a = str(input("Masukkan Nama :"))
    b = str(input("Masukkan tanggal lahir:"))
    c = str(input("Masukkan Asal Daerah:"))

def Tampilkan_semua_biodata():
    Menyimpan_biodata


while True:
    pilihan = float(input("Pilih masukkan :"))
    if pilihan == 1:
        Menyimpan_biodata()
    elif pilihan == 2:
        Tampilkan_semua_biodata()