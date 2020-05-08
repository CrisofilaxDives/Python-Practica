#Tipos de datos

#Strings
string_1 = "Hola Esteban"
string_2 = "¿Cómo estás?"
string_3 = "Bien"
string_4 = "24"

print(
    type(string_4)
)

##Métodos con print() del String
##upper()
print(string_1.upper())
##lower()
print(string_2.lower())
##swapcase()
print(string_3.swapcase())
##capitalize()
print(f"{string_1}, {string_2}".capitalize())
##replace()
print(string_4.replace("24", "25"))
##Multiples métodos
print(string_1.replace("Esteban", "Daniel").swapcase())
##count()
print(string_2.count("s"))
##startswith()
print(string_3.startswith("Bien"))
print(string_3.startswith("Ok"))
##endswith()
print(string_4.endswith("24"))
print(string_4.endswith("25"))
##split()
print(string_1.split())
print(string_1.split("a"))
##find()
print(string_2.find("C"))
##len()
print(
    len(string_3)
)
##index()
print(string_4.index("4"))
##isnumeric()
print(string_4.isnumeric())
print(string_3.isnumeric())
#isalpha()
print(string_3.isalpha())
print(string_4.isalpha())
##print() según indice
print(string_1[5])
##Otras formas de print()
print(string_2, "¿Qué cuentas?")
print(f"{string_2} ¿Qué cuentas?")
print("{0} ¿Qué cuentas?".format(string_2))

#Concatenación
concatenacion = string_1 + string_2 + string_3
print(concatenacion)

#Integers
x = 156
y = 655

print(
    type(y)
)

##Usos del integer
##Suma
print(x + y)
##Resta
print(y - x)
##Multiplicación
print(x * y)
##Divición
print(y / x)
###Solo número entero
print(y // x)
###Residuo
print(y % x)
##Exponenciación
print(x ** 2)
##Orden de las operaciones
print(20 - 10 / 5 * 3 **2)
##Uso de parentesis
print((20 - 10) / (5 * 3 ** 2))
##input()
# peso = int(input("Inserte su peso en Kg: "))
# print(f"Usted puso: {peso}")
# print(
#     type(peso)
# )
# altura = float(input("Inserte su altura en m: "))
# print(f"Usted puso: {altura}")
# print(
#     type(altura)
# )
# IMC = peso / (altura ** 2)
# print(f"Su Indice de Masa Corporal es: {IMC}")

#Floats
float_1 = 56.4
float_2 = 1.85
print(
    type(float_2)
)
print(float_1 + float_2)

#Boolean
print("5 + 6 = 11")
print(True)
print(
    type(True)
)

#None
print("Pruebas de que las vacunas causan autismo")
print(None)
print(
    type(None)
)

#List
list_1 = list(("Limón", "Pera", "Mango"))
print(list_1)
print(
    type(list_1)
)
##range() para hacer lista de números
list_2 = list(range(0, 11))
print(list_2)
##len()
print(
    len(list_1)
)
##print() según el indice
print(list_1[1])
print(list_1[-1])
##Usar "in" para saber si hay algo en la List
print(10 in list_2)
print("Guayaba" in list_2)
##Reemplazar elementos de la List
list_2[10] = 11 
print(list_2)
##append()
list_1.append("Guayaba")
print(list_1)
##extend()
list_2.extend((10, 12))
print(list_2)
##pop()
list_1.pop()
print(list_1)
list_2.pop(10)
print(list_2)
##remove()
list_2.remove(12)
print(list_2)
##clear()
# list_2.clear()
# print(list_2)
##sort()
list_1.sort()
print(list_1)
list_1.sort(reverse=True)
print(list_1)
##index()
print(list_1.index("Pera"))
##count()
print(list_1.count("Pera"))

#Tuple
tuple_1 = (string_1, x, float_1, None, True)
print(tuple_1)
print(
    type(tuple_1)
)

#Dictionary
dictionary_1 = {
    "Ciudad":"Medellín",
    "Altura":1300.23,
    "Población":3000000,
    "Rios":True,
    "Ciervos Salvajes":None
}
print(dictionary_1)
for key, value in dictionary_1.items():
    print(key, "=", value)