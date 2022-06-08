# operator bitwise adalah operator binary atau bilangan biner

a = 9
b = 5

# bitwise OR (|)
print("=====OR=====")
c = a | b

print("nilai :", a , ", binary :", format(a,"08b"))
print("nilai :", b , ", binary :", format(b,"08b"))
print("nilai :", c , ", binary :", format(c,"08b"))

# bitwise AND (&)
print("=====AND=====")
c = a & b

print("nilai :", a , ", binary :", format(a,"08b"))
print("nilai :", b , ", binary :", format(b,"08b"))
print("nilai :", c , ", binary :", format(c,"08b"))

# bitwise XOR (^)
print("=====XOR=====")
c = a ^ b

print("nilai :", a , ", binary :", format(a,"08b"))
print("nilai :", b , ", binary :", format(b,"08b"))
print("nilai :", c , ", binary :", format(c,"08b"))

# bitwise NOT
a = 60
print("nilai ~a :", ~a)