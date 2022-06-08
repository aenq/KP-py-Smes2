# operasi logika atau boolean

# not, or, and, xor

#NOT
print("===NOT===")
a = True
c = not a
print("data a =", a)
print("===not")
print("data c =", c) 

#OR (jika salah satu TRUE, maka hasilnya TRUE)
print("===OR===")
a = False
b = False
c = a or b
print(a,"OR",b,"=",c)

a = False
b = True
c = a or b
print(a,"OR",b," =",c)

a = True
b = False
c = a or b
print(a," OR",b,"=",c)

a = True
b = True
c = a or b
print(a," OR",b," =",c)

#AND (jika 2 buah nilai TRUE, maka hasilnya TRUE)
print("===AND===")
a = False
b = False
c = a and b
print(a,"and",b,"=",c)

a = False
b = True
c = a and b
print(a,"and",b," =",c)

a = True
b = False
c = a and b
print(a," and",b,"=",c)

a = True
b = True
c = a and b
print(a," and",b," =",c)

#XOR atau Bitwise (akan TRUE jika salah satunya True, sisanya false)
print("===XOR===")
a = False
b = False
c = a ^ b
print(a,"XOR",b,"=",c)

a = False
b = True
c = a ^ b
print(a,"XOR",b," =",c)

a = True
b = False
c = a ^ b
print(a," XOR",b,"=",c)

a = True
b = True
c = a ^ b
print(a," XOR",b," =",c)