# Tipos de datos, condicionales, operadores lógicos, loops y funciones

str_1 = "Comer"
str_2 = "papas y arroz"
int_1 = 45
int_2 = 69
float_1 = 1.9
float_2 = 89.5
bool_1 = True
none_1 =  None
list_1 = list(("Canada", "Argentina", "España"))
list_2 = list(range(1, 11))
tuple_1 = tuple((11, 12, 13))
tuple_2 = tuple((14,))
set_1 = {"Gatos", "Dulces", 86, 1.4}
dict_1 = {
    "ID":45544,
    "Jardín":True,
    "Color":"Verde",
    "m2":145.6,
    "Calefacción":None
}
print(type(int_1))

# Str
print(str_1.upper())
print(str_2.lower())
print(str_1.swapcase())
print(str_2.replace("y", "and").capitalize())
print(str_1.find("m"))
print(str_2.index("y"))
print(str_1.isnumeric())
print(str_1.isalpha())
print(str_2.count("a"))
print(len(str_1))
print(str_2.startswith("papas"))
print(str_2.endswith("arroz"))
print(str_2.split())
print(str_2.split("y"))
print(str_1[2])
print(f"{str_1} {str_2}")
print(str_1, " ", str_2)
print("{0} {1}".format(str_1, str_2))

# Concatenación
print(str_1 + " " + str_2)

# Int y Float
suma_1 = (((int_1 + float_1) * (int_2 - float_2)) / float_1)
print(suma_1)
print(int_1 / int_2)
print(int_1 // int_2)
print(int_1 % int_2)

# Bool y None
print("¿Comer mucho y no hacer actividad física, engorda?")
print(bool_1)
print("Pruebas de la creación de SARS-CoV-2")
print(none_1)

# List
print(len(list_1))
print(list_2[2])
print("Argentina" in list_1)
list_2[9] = 11
print(list_2)
list_1.append("Irlanda")
print(list_1)
list_2.extend((10, 12))
print(list_2)
list_1.pop()
list_2.pop(10)
print(list_1)
print(list_2)
list_2.remove(11)
print(list_2)
# list_2.clear()
# print(list_2)
list_1.sort()
print(list_1)
list_1.sort(reverse = True)
print(list_1)
print(list_2.index(5))
print(list_1.count("Canada"))

# Tuple y Set
# print(dir(set_1))
print(tuple_1[2])
# del tuple_2
set_1.add(False)
print(set_1)
set_1.remove("Gatos")
print(set_1)
# set_1.clear()
# print(set_1)

# Dict
for keys, values in dict_1.items():
    print(keys, "=", values)
print(dict_1.items())
print(dict_1.values())
print(dict_1.keys())
# del dict_1
# dict_1.clear()
# print(dict_1)

# Condicionales
usuario = input("Escriba su nombre de usuario: ")
if usuario == "Reinaldo":
    contraseña = input("Escriba su contraseña: ")
    if contraseña == "contraseña":
        print("Aceso concedido")
    else:
        print("Contraseña incorrecta")
else: 
    print("Nombre de usuario incorrecto")
precios = int(input("Escriba el precio: "))
if not(precios == 0):
    if precios > 500000 and precios < 1500000:
        print("Descuento del 10%")
    elif precios > 25000 and precios <= 500000:
        print("Descuento del 5%")
    elif precios >= 1500000 and precios < 3000000:
        print("Descuento del 15%")
    elif precios <=25000 or precios >=3000000:
        print("No tiene descuento")

# Loops
## "for"
print(list_1)
list_1.extend(("Colombia", "Francia", "Holanda", "China", "Surafrica"))
print(list_1)

for pais in list_1:
    print(pais)
    if pais == "Colombia":
        continue
    elif pais == "China":
        break

veces = 1
while veces <= 10:
    print(":v")
    veces = veces + 1

# Funciones
def imc(peso = 0, altura = 0):
    peso = float(input("Escriba su peso: "))
    altura = float(input("Escriba su altura: "))
    imc = peso / (altura ** 2)
    print(imc)
    if imc >= 18.5 and imc < 25:
        print("Usted tiene un peso normal")
    elif imc > 0 and imc < 18.5:
        print("Usted tiene bajo peso")
    elif imc >= 25 and imc < 30:
        print("Usted tiene sobrepeso")
    elif imc >= 30:
        print("Usted tiene obesidad")
# imc()

suma = lambda n1 = 0, n2 = 0, n3 = 0: n1 + n2 + n3
print(suma())
print(suma(5, 7.8, 254.898))

def suma(n1 = 0, n2 = 0):
    while True:
        try:
            n1 = float(input("Escriba el primer número: "))
            break
        except ValueError:
            print("La entrada no fue valida. Intente de nuevo")
    while True:
        try:
            n2 = float(input("Escriba el segundo número: "))
            break
        except ValueError:
            print("La entrada no fue valida. Intente de nuevo")
    suma = n1 + n2
    print(suma)
suma()

# Modulos
## Recordad que los modulos son tuyos, de otros o de python
## Propios
from fmath import suma, resta
suma(1, 8)
resta(8, 6)
## Python
### Usa import "nombre del modulo" o con from "modulo" import "funcion_1", "funcion_2", "..."
## Otros
### Usa la funcion en consola de windows pi install "nombre del modulo"

