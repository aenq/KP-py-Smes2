# IF AND OR

print("=== IF AND ===")
X = 3
if ((X%2)==1) and (X==3):
    print("X adalah bilangan ganjil")

print("=== IF OR ===")
X = 3
if ((X%2)==1) or (X==3):
    print("X adalah bilangan ganjil")

# NESTED IF atau IF BERSARANG
print("=== Nested IF ===")
x = 3

if ((x%2) == 1):
    if (x>10):
        print("x lebih dari 10")
    elif (x<10):
        print("x kurang dari 10")