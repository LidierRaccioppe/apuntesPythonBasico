
lista = [[1,2,3,4],
         [4,5,7,8],
        [9,10,11,12]]

lista [1][2] = "Golazoooooo"
print (lista [1][2])

print (lista [2][0])

lista2 = [1, 2.0, " tres " , [3+7j, 23],22, 33, 44, 55]
print (lista2 [3][0])


print (lista2 [0:2+1])
print (lista2 [0:8:2])

lista2 [0:3] = ["un", "dos", "tres", "cuatro"]
print (lista2)



t= (1,2,4,5, 2.0, "ola", 4+5j)
print(t[2])


listaUn = ["un"]

tuplaUn = ("un",)  # o se puede usar tuplaUn= "un"

'''
t2 = tuple()  ## tupla vacia
'''
t2 = tuple("Un")
print (type (t2))

print (type(listaUn))
print (type(tuplaUn))

 ## se obtiene informacion      help(tuple)

l = list()  ## lista vacia
l = []  ## lista vacia
l.append("Nuevo objeto")
l.append([2,3, 5])
print(l.count([2,3,5]))
print(l.__contains__([2,3,5]))
print(len(l))
l.extend([6,7,8,"nueve"])
l.insert(3, "siete")

print(l)
print(l.pop(3))
l.remove([2,3,5])
l.reverse()
print (l)

l2 = [2,4,3,1,5,9,7,8]
print(l2)



cadena = "el patio de mi casa es particular"


print (cadena [4:10])
print (cadena [4:24:3])




diccionario = {
    1 : "Un",
    2 : "Dos",
    3 : "Tres",
    4 : ["Cuatro", 4, "IV", 0b0000100, 0o4, 0x4, 4.0]}

print("Diccionario")

print (diccionario [3])
diccionario [3] = 0b0000011
print (diccionario [3])


print(diccionario.get(5,"No existe el valor")) ## De no encontrarse el valor devuelve el segundo
print( 0b0011 in diccionario)
print(diccionario.items())
print(diccionario.keys())
print(diccionario.values())
print("Borrando el valor : " + diccionario.pop(2, "No existe la clave"))
print(diccionario.items())







"""


# leer una tupla
numeros = [1,2,3,4,5]
suma = 0
for numero in numeros :
    print (numero)



for i in range (5,17,3):
    print (i)

"""



'''Cadenas'''


c = "Holas que tal "
c.count("qu")
c.find("qu")
print (c.join("varias cadenas"))
print(c.partition(" "))
c = c.replace(" ", "_")
c.split()

print(c)

d = "cs"
d.join(["a"])
print (d)

