# SOal No 1

X = 3
Y = 10
P = X + Y

if (P>0):
    print("Q=",X*Y)
else :
    print("Q=",X/Y)

# Soal Nomer 2

total=int(input("total = "))

if(1000000<total<2000000):
    diskon=total*(5/100)
    print
elif(total>2000000):
    diskon=total*(10/100)
else:
    diskon=total*(0/100)

setelah_diskon=total-diskon

print("Diskonnya adalah :", diskon)
print("Harga setelah diskon:", setelah_diskon)