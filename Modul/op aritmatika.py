# operasi aritmatika

# misal variabelnya 
a = 10
b = 3

# operasi tambah +
hasil = a + b
print(a,"+",b,"=",hasil)

# operasi kurang -
hasil = a - b
print(a,"-",b,"=",hasil)

# operasi kali *
hasil = a * b
print(a,"*",b,"=",hasil)

# operasi bagi /
hasil = a / b
print(a,"/",b,"=",hasil)
 
# operasi eksponen (pangkat) **
hasil = a ** b
print(a,"**",b,"=",hasil)

# operasi modulus atau sisa pembagian %
hasil = a % b
print(a,"%",b,"=",hasil)

# operasi floor division atau kebalikan dari modulus
# pembulatan kebawah apabila hasilnya positive,
# pembulatan keatas apabila hasilnya negative
# operasi floor division //
hasil = a // b
print(a,"//",b,"=",hasil)

#################note################
# prioritas operasi atau operational precedance
"""
    1. ()
    2. ** eksponen
    3. * / % // perkalian, pembagian dll
    4. tambah dan kurang + -
"""

x = 2
y = 4
z = 6

hasil = x * z // (y + z) % x / x ** y - z
print(x,"*",z, "//","(",y,"+",z,")%",x,"/",x,"**",y,"-",z,"=",hasil)