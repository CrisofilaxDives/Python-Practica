#Tipos de datos, variaables y usos del String con print()

#String
string_1 = "Los limones tienen un pH ácido"
string_2 = "El ácido debíl"
print(string_1)
print(
    type(string_1)
)
##upper()
print(string_1.upper())
##lower()
print(string_2.lower())
##swapcase()
print(string_1.swapcase())
##replace()
print(string_2.replace("ácido", "alcali"))
##Multiples métodos
print(string_1.replace("Los", "The").upper())
##count()
print(string_2.count("d"))
##startswith()
print(string_1.startswith("Los"))
print(string_1.startswith("The"))
##endswith()
print(string_2.endswith("debíl"))
print(string_2.endswith("debil"))
##split()
print(string_1.split())
print(string_1.split("i"))
##find()
print(string_2.find("E"))
##len()
print(
    len(string_1)
)
##index()
print(string_2.index("d"))
##isnumeric()
string_3 = "56"
print(string_3)
print(string_3.isnumeric())
print(string_1.isnumeric())
##isalpha()
string_4 = "Papa"
print(string_4.isalpha())
print(string_3.isalpha())
##print() según indice
print(string_2[5])
##print() otros usos
print(string_2, ", como el vinagre")
print(f"{string_2}, como el vinagre")
print("{0}, como el vinagre".format(string_2))

#Concatenación
concatenacion = string_1 + string_2
print(concatenacion)
print(f"{string_1}, {string_2.lower()}")

#Integers
integer_1 = 7885
integer_2 = 655
print(integer_1)
print(integer_2)
print(
    type(integer_2)
)

#Suma
texto_suma_1 = f"{integer_1} + {integer_2} ="
print(texto_suma_1)
suma_1 = integer_1 + integer_2
print(suma_1)

#Floats
float_1 = 56.4
float_2 = 89.7
print(float_1)
print(float_2)
texto_suma_2 = f"{float_1} + {float_2} ="
print(texto_suma_2)
suma_2 = float_1 + float_2
print(suma_2)
print(
    type(suma_2)
)

#Boolean
print("1 + 1 = 3")
print(False)
print(
    type(False)
)

#None
print("Pruebas de la tierra hueca")
print(None)
print(
    type(None)
)

#List
list_1 = [string_1, integer_1, float_1, False, None]
print(list_1)

#Tuple
tuple_1 = (string_2, integer_2, float_2, True, None)
print(tuple_1)

#Dictionary
dictionary_1 = {
    "Jaime":["Café", 32, 1.6, None, True],
    "Camilo":["Verde", 15, 1.8, None, False],
    "Kant":["Rosa", 56, 1.7, None, True]
}
print(dictionary_1)
for key, value in dictionary_1.items():
    print(key, "=", value)