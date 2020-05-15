# Tipos de datos, condicionales, funciones y modulos

str_1 = "hola"
str_2 = "bienvenido invocador"
int_1 = 45
int_2 = 189
flt_1 = 7.9
flt_2 = 78.6
bool_f = False
none_1 = None 
list_1 = list(("pollos", "perros", "conejos"))
list_2 = list(range(1, 6))
tuple_1 = tuple(range(1, 11))
tuple_2 = tuple((11,))
set_1 = {"caballos", 45, True}
dict_1 = {
    "Marca PC":"HP",
    "ID":65468651,
    "Pulgadas":15.6,
    "SSD":None
}
print(type(bool_f))

# Str
print(str_1.upper())
print(str_2.lower())
print(str_1.swapcase())
print(str_2.replace("invocador", "summoner").capitalize)
print(str_1.find("l"))
print(str_2.index("c"))
print(str_1.isnumeric())
print(str_2.isalpha())
print(str_1.split("l"))
print(str_2.split())
print(len(str_1))
print(str_2[4])
print(str_1.capitalize(), ", ", str_2)
print(f"{str_1}, {str_2}".capitalize())
print("{0}, {1}".format(str_1, str_2).capitalize())
print(str_1.startswith("hello"))
print(str_2.endswith("summoner"))
print(str_1.count("h"))

# Int y Float
suma_1 = (int_1 - flt_2) * (int_2 + flt_1) / (flt_2 ** flt_1)
print(suma_1)
print(int_1 / int_2)
print(int_1 // int_2)
print(int_1 % int_2)

# Concatenación
print(str_1 + ", " + str_2)

# Bool y None
print("Pruebas de la muerte de Obama")
print(bool_f)
print("Pruebas de la Tierra hueca")
print(none_1)

# List
print(list_1[2])
list_2.append(15)
print(list_2)
print(list_1.index("pollos"))
print(len(list_2))
print("pollos" in list_1)
list_2.extend((15, 16, 17))
print(list_2)
list_1.pop()
print(list_1)
list_2.pop(2)
print(list_2)
list_1.remove("perros")
print(list_1)
# list_2.clear()
# print(list_2)
list_1.extend(("jaguares", "sapos"))
print(list_1)
list_1.sort()
print(list_1)
list_1.sort(reverse = True)
print(list_2.count(15))

# Tuples y Sets
# print(dir(tuple_1))
print(tuple_2[0])
# del tuple_1
set_1.add(None)
print(set_1)
set_1.remove(1)
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

# Condicionales y Loops
error_m = "Hubo un error. Intente de nuevo"

while True:
    try:
        n1 = float(input("Escriba el primer número: "))
    except:
        print(error_m)
    try:
        n2 = float(input("Escriba el segundo número: "))
        break
    except:
        print(error_m)
suma_2 = n1 + n2
if suma_2 > 5:
    print(f"La suma {suma_2} > que 5")
elif suma_2 < 5:
    print(f"La suma {suma_2} < que 5")
resta_1 = n1 - n2
if resta_1 > 5:
    print(f"La resta {resta_1} > que 5")
elif resta_1 < 5:
    print(f"La resta {resta_1} < que 5")

numeros = list(())
x = 0
while True:
    stri = input("Escriba un número: ")
    if stri == "salir":
        break
    try:
        inti = int(stri)
        numeros.append(inti)
    except:
        print(error_m)
        continue
for y in numeros:
    x = x + y
    print(f"{x} {y}")
print(f"La suma final fue de {x}")

    


    

