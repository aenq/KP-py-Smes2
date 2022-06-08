########## KELAS TERBUKA YUTUB =============
print(100*"=")

nilai = 50

if 80 <= nilai <= 100:
    print("nilai anda adalah A")
elif 70 <= nilai < 80:
    print("nilai anda adalah B")
elif 60 <= nilai < 70:
    print("nilai anda adalah C")
elif 50 <= nilai < 60:
    print("nilai anda adalah T, lakukan perbaikan")
else:
    print("maaf anda tidak lulus mata kuliah ini")

print(100*"+")
print("operator logika untuk list dan string")
print(" ")

gorengan=["bakwan","cireng","bala-bala","gehu","combro","pisang goreng","pukis","risoles"]
beli = "bandrek"

if beli in gorengan:
    print('Mamang bilang,"ya, saya jual', beli,'"')

if not beli in gorengan:
    print('Mamang bilang, "saya gak jualan', beli,'"')

    # Ternary IF

X = 3
print("Bilangan ganjil" if ((X%2)==1) else "Bilangan genap")

X = 3
print(("Bilangan genap", "Bilangan ganjil")[((X%2)==1)])

X = 3
print({True:"Bilangan ganjil", False:"Bilangan genap"}[((X%2)==1)])

X = 3
print((lambda:"Bilangan genap", lambda:"Bilangan ganjil")[(X%2)==1]())