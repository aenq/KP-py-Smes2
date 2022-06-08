# IF TUNGGAL
print("============IF Tunggal=============")
# a. pencarian bilangan ganjil
X = 3
if(X%2) == 1:
    print("Bilangan Ganjil")

# b. IF yang memiliki konteks yang berbeda untuk mencari bilangan ganjil 
#dan pencocokan angka 3
X = 3
if (X%2) == 1:
    print("Bilangan Ganjil")
if X==3:
    print("Angka Tiga")

# IF ELIF ELSE
print("=============if elif else============")
X = 3
if(float(X).is_integer())!=True:
    print("Bukan bulangan bulat bro")
elif(X%2)==1:
    print("Bilangan ganjil bro")
else:
    print("Bilangna genap")

# Ternary IF
print("====Ternary IF====")
X = 3

print("# IF ELSE #")
if (X%2)==1:
    print("Bilangan ganjil")
else:
    print("Bilangan ganjil")

X = 3
print("Bilangan ganjil" if ((X%2)==1) else "Bilangan genap")

# Menggunakan TUPLE
print("====Menggunakan Tuple====")
X = 3
print(("Bilangan genap", "Bilangan ganjil")[((X%2)==1)])

# Menggunakan Dictionary
print("====mengunakan dictionary====")
X = 3
print({True:"Bilangan ganjil", False:"Bilangan genap"}[((X%2)==1)])

# Menggunakan Lambda Function
print("==Menggunakan Lambda function")
X = 3
print((lambda:"Bilangan genap", lambda:"Bilangan ganjil")[(X%2)==1]())




