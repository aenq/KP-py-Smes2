
print("no 2 for")

for i in range(10):
	nama = str(input("Masukkan nama: "))
	print("Nama saya ", nama)
	if i == 1:
		pass
	elif nama == "python":
		print("Good bye python")
		break


print("No 2 while")

i = "A"
while i == "A":
    nama = str(input("Masukkan nama:", ))
    print("Nama saya ", nama)
    if nama == "python":
        print("Good bye Python")
        break