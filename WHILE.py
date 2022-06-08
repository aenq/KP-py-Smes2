
#contoh
print("Perulangan While")
i = 1
while(i < 11):
    print(i, end=" ")
    i = i+1
    if i == 11:
        break
    print("oke")
    
#contoh
print("Perulangan For")
for i in range(0,5):
    if i == 3:
        print("angka 3 didapat")
        break
    print(i)