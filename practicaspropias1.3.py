#Tipos de datos, variables y usos del String con print()

#Strings
string_1 = "pollos"
string_2 = "Luxación Articular"
string_3 = "DESODORANTE DE ALMENDRA"
print(string_1)
print(string_2)
print(string_3)
print(
    type(string_3)
)
##upper()
print(string_1.upper())
##lower()
print(string_2.lower())
##swapcase()
print(string_3.swapcase())
##replace()
print(string_1.replace("pollos", "gallinas"))
##Multiples métodos
print(string_3.replace("ALMENDRA", "PAPA").swapcase())
##count()
print(string_2.count("u"))
##startswith()
print(string_1.startswith("po"))
print(string_1.startswith("Po"))
##endswith()
print(string_2.endswith("Articular"))
print(string_2.endswith("articular"))
##split()
print(string_3.split())
print(string_3.split("E"))
##find()
print(string_1.find("s"))
##len()
print(
    len(string_2)
)
##index()
print(string_3.index("S"))
##isnumeric()
string_4 = "15"
print(string_4.isnumeric())
print(string_1.isnumeric())
##isalpha
print(string_1.isalpha())
print(string_4.isalpha())
##print() según indice
print(string_2[3])
print(string_2[-2])
##print() otros usos
print(string_3 + ", GRATIS")
print(f"{string_1} asados")
print("{0} Grado 1".format(string_2))

#Concatención
concatenacion = string_1 + string_2 + string_3
print(concatenacion)

#Integers
numero_1 = 56
numero_2 = 98
print(numero_1)
print(numero_2)
print(
    type(numero_2)
)

#suma
suma_texto_1 = "56 + 98 ="
suma_1 = numero_1 + numero_2
print(suma_texto_1)
print(suma_1)

#Floats
decimal_1 = 1.6
decimal_2 = 6.8
suma_texto_2 = f"{decimal_1} + {decimal_2} ="
print(suma_texto_2)
suma_2 = decimal_1 + decimal_2
print(suma_2)
print(
    type(suma_2)
)

#Booleans
falso = False
verdadero = True
print("El consumo de carne ha aumentado los indices de cancer intestinal")
print(f"Eso es {verdadero}")
print("El dia de la madre es el 12 de mayo")
print(f"Eso es {falso}")
print(
    type(verdadero)
)

#None
none = None
print("Evidencia de civilizaciones intreterrestres")
print(none)
print(
    type(none)
)

#List
cosas_1 = [string_1, numero_2, decimal_1, verdadero, none]
print(cosas_1)
print(
    type(cosas_1)
)

#Tuple
cosas_2 = (string_2, numero_1, decimal_2, falso, none)
print(cosas_2)
print(
    type(cosas_2)
)

#Dictionary
ambiente = {
    "Coordenadas":[126554.555, -486844.5225],
    "Ambiente":"Humedo",
    "Habitantes":15623,
    "Censo 2019":False,
    "Prueba de COVID-19":None
}
print(ambiente)
for key, value in ambiente.items():
    print(key,"=", value)