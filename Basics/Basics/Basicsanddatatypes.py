

a = 67
b = "hello"

print("{}{}{}".format(a, " ", b))


#datatpes

a, b, c = 23.45, "kalyan", 6789087
print(type(a))
print(type(b))
print(type(c))

#list
listlist= [1, 2, 3, "kalyan"]
print(listlist)
listlist.append("krishna")
listlist.reverse()
print(listlist)
listlist.insert(4, "Srinivas")
print(listlist)
#tuple : values can't be changed
lista = (1, "kalyan", 23, "krishna")
print(lista)
print(lista[2])

#dictionaries

listd = {1: "Kalyan", "b": 2345}
print(listd)
print(listd["b"])