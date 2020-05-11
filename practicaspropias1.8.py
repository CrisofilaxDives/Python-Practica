# Tipos de datos y condicionales

str_1 = "Pollo"
str_2 = "Gratis para Todos"
int_1 = 562
int_2 = 86
float_1 = 1.65
float_2 = 5.9
none = None 
bool_T = True
list_1 = list(("Pera", "Mango", "Limon"))
list_2 = list(range(1, 4))
tuple_1 = tuple((1, 2, 3, 4))
tuple_2 = tuple((5,))
dict_1 = {
    "ID":46524555,
    "Nombre":"Jaime",
    "Premium":bool_T,
    "Telefono":None,
    "Tiempo":15.6
}
set_1 = {str_1, int_1, float_1}
print(type(str_1))

# Str
print(str_1.upper())
print(str_2.lower())
print(str_1.swapcase())
print(str_2.replace("para", "for").capitalize())
print(str_1.count("o"))
print(str_2.startswith("Gratis"))
print(str_2.endswith("Todos"))
print(str_2.split())
print(str_1.split("o"))
print(str_2.find("i"))
print(len(str_1))
print(str_2.index("T"))
print(str_1.isnumeric())
print(str_2.isalpha())
print(str_1[2])
print(str_2, "!!")
print(f"{str_1} {str_2}!".capitalize())
print("{0} {1}!".format(str_1, str_2).capitalize())

# Concatenación
print(str_1 + " " + str_2)

# Int y Float
print(int_1 + int_2 + float_1 + float_2)
print((int_1 + float_1) * (int_2 - float_2) / float_2)
print(int_1 / float_1)
print(int_1 // float_1)
print(int_1 % float_1)

# Bool y None
print("¿Existen pruebas de el funcionamiento de las vacunas?")
print(bool_T)
print("Pruebas de que las vacuans causen autismo")
print(none)

# List
print(len(list_1))
print(list_2[2])
print("Pera" in list_1)
list_2[1] = 9
print(list_2)
list_1.append("Sandia")
print(list_1)
list_2.extend((12, 286))
list_1.pop()
list_2.pop(4)
print(list_1)
print(list_2)
list_1.remove("Mango")
print(list_1)
# list_2.clear()
# print(list_2)
list_1.sort()
print(list_1)
list_1.sort(reverse = True)
print(list_1)
print(list_2.index(1))
print(list_1.count("Pera"))

# Tuple y Set
# print(dir(tuple_1))
print(tuple_1[2])
# del set_1
set_1.add("Changos")
print(set_1)
set_1.remove(562)
print(set_1)
# set_1.clear()
# print(set_1)

# Dict
for keys, values in dict_1.items():
    print(keys, "=", values)
print(dict_1.items())
print(dict_1.keys())
print(dict_1.values())
# del dict_1
# dict_1.clear()
# print(dict_1)

# Condicionales
nombre = input("Ingrese su nombre: ")
if nombre == "David":
    print("Eres David")
elif nombre == "Mabell":
    print("Eres Mabell")
else:
    print("Eres otra persona")
año = int(input("Escribe tu fecha de nacimiento: "))
if not(año < 1880):
    if año >= 1880 and año < 1920:
        print("Tienes más de 100 años")
    elif año == 1920:
        print("Tienes 100 años")
    elif año > 1920 and año < 2002:
        print("Tienes entre 100 y 19 años")
    elif año >= 2002 and año <= 2019:
        print("Tienes entre 18 y 1 año")
    elif año == 2020:
        print("Acabas de nacer")
    else:
        print("Vienes del futuro") 
else:
    print("Estas muerto")
ahorros = 100000
precio = int(input("Escribe el precio:"))
if (not(precio < 0)):
    if precio > ahorros or precio <0:
        print("No puedes comprarlo")
    else:
        print("Puedes comprarlo")
else:
    print("Error")
    