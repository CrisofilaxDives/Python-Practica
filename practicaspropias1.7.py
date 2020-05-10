# Tipos de datos y condiconales

# Strings
string_1 = "Hola"
string_2 = "Toma Agua"
print(type(string_1))
## upper()
print(string_1.upper())
## lower()
print(string_2.lower())
## swapcase()
print(string_1.swapcase())
## capitalize()
print(string_2.capitalize())
## replace() y multiples métodos
print(string_1.replace("Hola", "Hi").capitalize())
## count()
print(string_2.count("a"))
## startswith()
print(string_1.startswith("Hola"))
## endswith()
print(string_2.endswith("Agua"))
## split()
print(string_1.split("o"))
## find()
print(string_2.find("m"))
## len()
print(len(string_1))
## index()
print(string_2.index("T"))
## isnumeric()
print(string_2.isnumeric())
## isalpha()
print(string_1.isalpha())
## print() según indice
print(string_2[5])
## Otras formas de print()
print(string_2, ", por favor")
print(f"{string_1}, {string_2}".capitalize())
print("{0}, {1}".format(string_1, string_2))

# Concatenación
print(string_1 + string_2)

# Integers y Floats
x = 5
y = 9
z = 1.5
w = 3.8
print(type(x))
print(type(z))
## Operaciones básicas y orden de operaciones
print(((x + y) - z * x) / w)
## División entera
print(y // x)
## Residuo división
print(w % z)
## Exponenciación
print(z ** y)

# Boolean
boolean_1 = x * z
if boolean_1 < 7.5 and boolean_1 > 7.5:
    print(False)
elif boolean_1 == 7.5:
    print(True)
print(type(True))

# None
print("Evidencias que las vacunas causan autismo")
print(None)
print(type(None))

# List
list_1 = list(("Arbol", "Lechuga", "Arbusto"))
print(type(list_1))
## range()
list_2 = list(range(1, 4))
## len()
print(len(list_1))
## print() según indice
print(list_2[1])
## "in" para saber si esta el elemento
print("Arbol" in string_1)
## Reemplazar Integers por indice
list_2[2] = 4
## append()
list_1.append("Zanahoria")
print(list_1)
## extend()
list_2.extend((3, 5))
print(list_2)
## pop()
list_1.pop()
list_2.pop(3)
print(list_1)
print(list_2)
## remove()
list_1.remove("Arbusto")
print(list_1)
## clear()
# list_2.clear()
# print(list_2)
## sort()
list_1.sort()
print(list_1)
list_1.sort(reverse = True)
print(list_1)
## index()
print(list_1.index("Lechuga"))
## count()
print(list_2.count(1))

# Tuple
tuple_1  = tuple((1, 2, 3, 4, 5))
print(type(tuple_1))
## dir()
# print(dir(tuple_1))
## Tuple único
tuple_2 = tuple((6,))
print(tuple_2)
## print() según indice
print(tuple_1[2])
## "del"
del tuple_2

# Dictionary
dict_1 = {
    "Casa":"Verde",
    "ID":56555,
    "m2":153.3,
    "Linea gas":None,
    "Calefacción":True
}
for keys, values in dict_1.items():
    print(keys, "=", values)
## keys()
print(dict_1.keys())
## values()
print(dict_1.values())
## items()
print(dict_1.items())
## "del"
# del dict_1
## clear()
# dict_1.clear()

# Set
set_1 = {"papas", "yuca", "maiz"}
print(type(set_1))
## "in" para saber si esta en el set
print("papas" in set_1)
## add()
set_1.add("trigo")
print(set_1)
## remove()
set_1.remove("yuca")
print(set_1)
## clear()
# set_1.clear()
## "del"
# del set_1

# Condicionales
# fruta = input("Escriba la fruta: ")
# if fruta == "mango":
#     print("Son 1200$")
# elif fruta == "pera":
#     print("Son 1300$")
# else:
#     print("Son 1000$")
precio = int(input("Introduzca el precio: "))
if (not(precio <= 0)):
    if precio >= 500 and precio <= 1500:
        print("Fruta")
    elif precio < 500 or precio > 1500:
        print("No es fruta")
else:
    print("Error")