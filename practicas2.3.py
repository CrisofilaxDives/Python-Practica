# Tipos de datos, condicionales y loops 

str_1 = "hola"
str_2 = "buenos días"
int_1 = 1
flt_1 = 3.5
bool_f = False
none_1 = None 
list_1 = list(("limon", "manzana", "piña"))
tuple_1 = tuple((1, 2, 3))
tuple_2 = tuple((4,))
set_1 = {1, "perro", True, None, 0.5}
dict_1 = {
    "clima":"humedo",
    "lluvias":True,
    "latitud":546.465
}

# Str
print(str_1.upper())
print(str_2.lower())
print(str_1.swapcase())
print(str_2.replace("días", "noches").capitalize())
print(str_1.split("l"))
print(str_2.split())
print(len(str_1))
print(str_1.isalpha())
print(str_2.isnumeric())
print(str_1.index("o"))
print(str_2.find("n"))
print(str_1.startswith("Hola"))
print(str_2.endswith("días"))
print(str_2.count("s"))
print(str_1[2])
print(str_1, ", ", str_2)
print(f"{str_1}, {str_2}".capitalize())
print("{0}, {1}".format(str_1, str_2).capitalize())

# Int y Float
op = (int_1 + flt_1) * (int_1 - flt_1)
print(op)
print(int_1 / flt_1)
print(int_1 // flt_1)
print(int_1 % flt_1)

# Bool y None
print("Las ideas médicas de Donald Trump son inteligentes")
print(bool_f)
print("Pruebas de que las vacunas causen autismo")
print(none_1)

# List
print(list_1[2])
list_1.append("maracuya")
print(list_1)
list_1.sort()
print(list_1)
list_1.sort(reverse = True)
print(list_1)
list_1.extend(("mango", "banana"))
print(list_1)
list_1.pop(1)
print(list_1)
list_1.pop()
print(list_1)
list_1[2] = "jamaica"
print(list_1)
list_1.remove("piña")
print(list_1)
# list_1.clear()
# print(list_1)
print(list_1.index("manzana"))
print("piña" in list_1)
print(list_1.count("mango"))

# Sets y Tuples
print(tuple_1[1])
del tuple_2
try:
    print(tuple_2)
except:
    print("tuple_2 ha sido eliminado")
# print(dir(tuple_1))    
set_1.add("piedra")
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
dict_1.clear()
print(dict_1)
del dict_1
try:
    print(dict_1)
except:
    print("dict_1 ha sido eliminado")

# Condicionales y Loops
list_precios = list(())
x = 0
while True:
    precios = input("Introduzca los precios: ")
    if precios == "terminar":
        break
    try:
        flt_precios = float(precios)
        list_precios.append(flt_precios)
    except:
        print("Hubo un error")
for precio in list_precios:
    x = x + precio
if x > 100000 and x <= 150000:
    print("Descuento del 10%")
    x = x * 0.9
    print(f"Su pago total es de {x}")
elif x > 150000 and x <= 200000:
    print("Descuento del 20 %")
    x = x * 0.8
    print(f"Su pago total es de {x}")
else:
    print("Descuento del 30%")
    x = x * 0.7
    print(f"Su pago total es de {x}")

# Funciones
def saludo(saludo = "hola", persona = "persona"):
    print(f"{saludo}, {persona}".capitalize())
saludo()
saludo("Hi", "Charles")

def mult(n1 = 0, n2 = 0):
    while True:
        n1 = input("Escriba el primer número: ")
        if n1 == "salir":
            break
        try:
            flt_n1 = float(n1)
        except:
            print("Hubo un error") 
        break
    while True:
        n2 = input("Escriba el segundo número: ")
        if n2 == "salir":
            break
        try:
            flt_n2 = float(n2)
        except:
            print("Hubo un error") 
        break
    mult = flt_n1 * flt_n2
    return mult
print(mult())
