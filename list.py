print("===LIST===")
print("")

print("a. Mencetak list")
list = [1,2,3,4,5]
print(list)
for x in list:
    print(x)

print("")
print("b. list.count(element)")
list = [1,1,3,1,5]
print(list.count(1))


print("")
print("c. list.index(element)")
list = [1,2,3,4,5]
print(list.index(4))

print("")
print("d. len(list")
print(len(list))

print("")
print("e. membership")
member = 3 in list
print(member)

print("")
print("f. not membership")
member = 3 not in list
print(member)

print("")
print("g. max & min")
print(max(list))
print(min(list))

print("")
print("h. penambahan data")
list+=[6,8,9,10,]
print(list)

# menambah data 6 pada index ke-2
list.insert(6,7)
print(list)

# menambah pada akhir list
list.append(11)
print(list)

print("")
print("i. penggabungan data ")
list2 = [12,13,14,15]
print(list + list2)

print("")
print("j. cv list ke variable")
x,y,z = [1,2,3]
print(y)

print("")
print("k. merubah data dalam list")
list = [1,2,[3,4,5]]
list[1]= 0
list[2][0] = 6
print(list)

print("")
print("l. repetition")
list = "yaampun rachel cantik banget"
repetition = list*5
print(repetition)

print("")
print("m. join string list")
list = ["saya","makan", "nasi"]
join_list = " " .join(list)
print(join_list)

print("")
print("n. cv list ke tuple")
list = [1,2,3,4,5]
tuple = tuple(list)
print(tuple)

print("")
print("o. operator perbandingan")
list2 = [1,2,3,4,5]
print(list == list2)

print("")
print("p. hapus element")
list.remove(5)
print(list)

print("")
print("q. menambah element/data list")
list = [1,2,3,4,5]
list.pop(3)
print(list)

print("")
print("r. pengurutan list")
list = [1,6,2,6,34,7]
print(sorted(list))

print("")
print("s. copy list")
list = [1,4,3,5,2]
print(id(list))
list_new = list
print(id(list_new))
print(list)
print(list_new)

print("")
print("t. menghapus semua data")
list.clear()
print(list)