# Immutable object
print("========Immutable Object========")
""" Ada beberapa object yang bersifat immutable, diantaranya adalah :
int
float
decimal
complex
bool
string
tuple
range
frozenset
bytes """

# PAKAI STRING
print(100*" ")
print("===Pakai STRING===")
a = "corey"
print(a)
print("Id of a is:", id(a))

# a[0] = "C"
# print(a) #akan terjadi error kalau corey, huruf awalnya diubah menjadi kapital "C", 
			#karena data string itu immutable

a = "john"
print(a)
print("Id of a is:", id(a))

#Pakai Tuple
print("===Pakai Tuple===")
tuple = (1,2,3,4,5)
print(id(tuple))

tuple += (6,)
print(id(tuple))

#tapi imutable tidak sepenuhnya immutable, didalamnya bisa terdapat mutable object
tuple = (1,[6,7,8],3,4,5)
tuple[1][0] = 7
print(tuple)


# Mutable Object
print(100*" ")
print("========Mutable Object========")
"""Ada beberapa object yang tergolong 
kedalam mutable object diantaranya adalah :
list
dict
set
bytearray """


# PAKAI LIST
print("===Pakai LIST===")
a = [1,2,3,4,5]
print(a)
print("id nya adalah:", id(a))

a[0] = 6
print(a)
print("id nya adalah:", id(a)) #nah kalau mutable ini id nya tetap sama 
								#walaupun a nya diganti jadi 6

####################
print("========Implementasi Modul 4========")
print(100*" ")
print("===Tuple===")
print(100*" ")

print("===> A. Mencetak Data Tuple")
tuple = (1,2,3,4,5) 
print(tuple[4])

tuple = (1,2,3,4,5)
print(tuple[-3])

tuple = (1,2,3,4,5)
print(tuple[2:])

tuple = (1,2,3,4,5) # menggunakan perulangan
for x in tuple:
	print(x)

print("===> B. tuple.count(elemen)")
tuple = (1,2,3,4,5)
print(tuple.count(5))

print("===> C. tuple.index(element)")
tuple = (1,2,3,4,5)
print(tuple.index(3))

print("===> D. len(tuple)")
# untuk mengetahui jml panjang atau banyaknya isi tuple
tuple = (1,2,3,4,5)
print(len(tuple))

print("===> E. Membership")
tuple = (1,2,3,4,5)
member = 5 in tuple
print(member)

print("===> F. max and min")
tuple = (1,2,3,4,5)
print(max(tuple))
print(min(tuple))

print("===> G. Concatination tuple")
tuple = (1,2,3,4,5)
tuple += (6,7,8,9,10,)
print(tuple)

tuple1 = (1,2,3,4,5)
tuple2 = (5,6,7,8,9)
tuple3 = tuple1 + tuple2
print(tuple3)

print("===> H. Convert data tuple ke dalam variable")
x,y,z = (1,2,3)
print(y)

print("===> I. Tuple key/value pairs convert dalam dictionary")
tuple = dict([("Januari", 1), ("Februari", 2), ("Maret", 3)])
print(tuple["Maret"])

print("===> J. Mutable Tuple")
tuple = (1,2,[3,10,100])
tuple[2][0] = 9
print(tuple)

print("===> K. Repetition")
tuple = "Rachel Unyu "
Repetition = tuple*3
print(Repetition)

print("===> L. Join string tuple")
tuple = ("saya", "makan", "nasi")
join_tuple = " " .join(tuple)
print(join_tuple)

print("===> M. convert list ke tuple")
"""list = [1,2,3,4,5]
tuple = tuple(list)
print(tuple)"""

print("===> N. Operator Perbandingan")
tuple1 = [1,2,3,4,5]
tuple2 = [1,2,3,4,5]
print(tuple1 == tuple2)

print("===> O. delete tuple")
tuple = (1,2,3,4,5)
del tuple
print(tuple)
tuple = (4,5,6,7)
print(tuple)

print(100*" ")
print("===Set Method===")
print(100*" ")

print("===>A. Mencetak Set")
set= {1,2,3,4,5}
for data in set:
	print(data)

print("===>B. Mengetahui panjang set")
set = {1,2,3,4,5}
print(len(set))

print("===>C. Mengetahui keanggoataan set atau bukan")
set = {1,2,3,4,5}
print(1 in set)
print(1 not in set)

a = {1,2,3,4,5}
b = {1,2,3,4}
print(a <= b)
print(a >= b)

print("===>D. Set Union") #Gabungan 2 data dari 2 set
A = {1,2,3,4,5}
B = {11,12,13,14,15}
print(A.union(B))
print(A|B)

print("===>E. Set Intersection")
"""Intersection merupakan keterikatan element data pada 
dua set atau lebih, operasi tersebut menggunakan 
set.intersection(otherset) atau set & otherset"""
Bilangan = {1,2,3,4,5}
Prima = {2,3,5}
print(Bilangan.intersection(Prima))
print(Bilangan&Prima)

print("===>F. Set Difference")
"""menggunakan set.difference(otherset) atau set - otherset"""
A = {1,2,3,4,5}
B = {4,5,6,7,8}
print(A.difference(B))
print(A-B)

print("===>G. Set Symmetric Difference")
A = {1,2,3,4,5}
B = {4,5,6,7,8}
print(A.symmetric_difference(B))
print(A^B)

print("===>H. Copy Set")
A = {1,2,3,4,5}
B = A.copy()
print(B)

print("===>I. Menambah Elemen Set")
A = {1,2,3,4,5}
A.add(6)
print(A)

print("===>J. Menghapus Elemen Set")
A = {1,2,3,4,5}
A.remove(3) # Atau bisa pake print(A.discard(3))
print(A)

print("===>K. Mengambil Nilai Elemen pada Set")
A = {1,2,3,4,5}
A.pop()
print(A)

print("===>L. Update Set")
print("Menggunakan set.update(Otherset)")
A = {1,2,3,4,5}
B = {"buku", "pulpen", "penggaris"}
A.update(B) 
print(A)

print('Menggunakan intersection')
a = {1,2,3,4,5}
b = {4,5,6,7,8}
a&=b
print(a)

print("Menggunakan difference")
a-=b
print(a)

print("Menggunakan simmetric.difference")
a^=b
print(a)

print("===>M. Menghapus semua element set")
a ={1,2,3,4,5}
a.clear()
print(a)