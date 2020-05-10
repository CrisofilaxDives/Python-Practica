# Tipos de datos y condicionales

# String
string_1 = "hola"
string_2 = "david"
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
print(string_1.replace("hola", "qué tal").capitalize())
## count()
print(string_2.count("d"))
## startswith()
print(string_1.startswith("hola"))
## endswith()
print(string_2.endswith("david"))
## split(), también se puede hacer por palabras
print(string_1.split("o"))
## find()
print(string_2.find("i"))
## len()
print(len(string_1))
## index()
print(string_2.index("a"))
## isnumeric()
print(string_1.isnumeric())
## isaplha()
print(string_2.isalpha())
## print() segun indice
print(string_1[2])
## otras formas de print()
print(string_1, string_2)
print(f"{string_1}, {string_2}")
print("{0}, {1}".format(string_1, string_2))

# Concatenación
print(string_1 + string_2)

# Integers
x = 26
y = 52
print(type(x))
## Operaciones básicas y orden de operaciones
print((((x + y) - (y - x) ) * 2) / 4)
##Divición entera
print(x // y)
##Residuo divición
print(x % y)
## Exponenciación
print(x ** 2)
## Usaré input() con los condicionales

# Floats
float_1 = 56.3
float_2 = 89.3
print(type(float_2))
print(float_1 + float_2)

# Boolean
suma = float_1 + float_2
if suma == 145.6:
    print(True)
else:
    print(False)
print(type(False))

# None
print("Evidencias tierra plana")
print(None)
print(type(None))

# List
list_1 = list(("Pollo", "Cerdo"))
print(type(list_1))
## range()
list_2 = list(range(1, 4))
## len()
print(len(list_2))
## print() según indice
print(list_1[1])
## "in" para saber si esta
print(1 in list_2)
## Reemplazar elementos por indice, solo Integers
list_2[2] = 4
print(list_2)
## append()
list_1.append("Res")
print(list_1)
## extend()
list_2.extend((3, 5))
print(list_2)
## pop()
list_2.pop()
list_2.pop(2)
print(list_2)
## remove()
list_1.remove("Res")
print(list_1)
## clear()
# list_2.clear()
# print(list_2)
## sort()
list_1.sort()
print(list_1)
list_1.sort(reverse = True)
## index()
print(list_2.index(1))
## count()
print(list_1.count("Cerdo"))

# Tuple
tuple_1 = tuple((2, 4, 6))
print(type(tuple_1))
## dir()
# print(dir(tuple_1))
## Tuple único
tuple_2 = tuple((8,))
print(tuple_2)
## print() según indice
print(tuple_1[0])
## "del" para eliminar la variable
# del tuple_2
# print(tuple_2)

# Dictionary
dictionary_1 = {
    "Tipo de mascota":"Perro",
    "ID":5464564654665,
    "Vacunado":True,
    "Peso":44.6,
    "Operaciones":None
}
print(type(dictionary_1))
for keys, values in dictionary_1.items():
    print(keys, "=", values)
## dir()
# print(dir(dictionary_1))
## keys()
print(dictionary_1.keys())
## items()
print(dictionary_1.items())
## values()
print(dictionary_1.values())
## "del"
# del dictionary_1
# print(dictionary_1)
## clear()
# dictionary_1.clear()
# print(dictionary_1)+

# Set
set_1 = {"azul", "rojo", "verde"}
print(type(set_1))
## "in" para saber si algo esta en el Set
print("cafe" in set_1)
## add()
set_1.add("cafe")
print(set_1)
## remove()
set_1.remove("cafe")
print(set_1)
## clear()
# set_1.clear()
# print(set_1)
## "del"
# del set_1
# print(set_1)


# Condicionales
nombre = input("Nombre: ")
if nombre == "david":
    print("Eres david")
elif nombre == "carlos":
    print("Eres carlos")
else:
    print("Eres otra persona")
numero = int(input("Número: "))
if numero >= 1000000 and numero <= 9999999:
    print("Número guardado")
elif numero == str or numero == float:
    print("Número invalido")
else:
    print("Intente de nuevo")
usuario = input("Ingrese su usuario: ")
if (not(usuario == "pedro")):
    if (not(usuario == "jaime")):
        if (not(usuario == "matias")):
            contraseña = input("Contraseña: ")
            if contraseña == "contraseña":
                print("Acceso concedido")
            else:
                print("Contraseña invalida")