#Variables y tipos de datos

#Strings
string_1 = "Limón"
string_2 = "Fresas"
string_3 = "Sandía"
string_4 = ", "
print(string_1)
print(string_2)
print(string_3)
print(
    type(string_3)
)

#Concatenación
concatenacion = string_1 + string_4 + string_2 + string_4 + string_3
print(concatenacion)

#Integers
integer_1 = 1000
integer_2 = 1600
integer_3 = 400
print(integer_1)
print(integer_2)
print(integer_3)

#Suma
signo_mas = "+"
suma_texto_1 = integer_1, signo_mas, integer_2, signo_mas, integer_3
print(suma_texto_1)
suma_1 = integer_1 + integer_2 + integer_3
print(suma_1)
print(
    type(suma_1)
)

#Floats
float_1 = 95.6
float_2 = 76.7
float_3 = 56.1
print(float_1)
print(float_2)
print(float_3)
suma_texto_2 = float_1, signo_mas, float_2, signo_mas, float_3
print(suma_texto_2)
suma_2 = float_1 + float_2 + float_3
print(suma_2)
print(
    type(suma_2)
)

#Boolean
print("¿El cielo es rojo?")
verdadero = True
falso = False
print(falso)
print("¿Las serpientes vuelan?")
print(falso)
print("¿El pasto es verde?")
print(verdadero)
print(
    type(verdadero)
)

#None
print("Información verdarera de la tierra hueca")
ninguna = None
print(ninguna)
print("Información exacta del funcionamiento del SMM")
print(ninguna)
print("Información sobre la existencia de reptilianos")
print(ninguna)
print(
    type(ninguna)
)

#List
frutas = [string_1, string_2, string_3]
enteros = [integer_1, integer_2, integer_3]
decimales = [float_1, float_2, float_3]
print(frutas)
print(enteros)
print(decimales)
print(
    type(decimales)
)

#Tuple
respuestas = (falso, falso, verdadero)
ramdom_1 = (string_1, ninguna, verdadero)
ramdom_2 = (integer_3, falso, float_3)
print(respuestas)
print(ramdom_1)
print(ramdom_2)
print(
    type(ramdom_2)
)

#Dictionary
informacion_personal = {"dirección":"Cll 56# 26B-5", 
                        "telefóno":4415325, 
                        "contrato":658547, 
                        "ultima_factura":56897.32, 
                        "premium":False, 
                        "hizo_encuesta":None}
print(informacion_personal)
for key, value in informacion_personal.items():
    print(key, "=", value)
amigos = {"Carlos":["Lio", 5689658, 3125634578],
          "Sergio":["Jiro", 2655878, 3198566543],
          "Daniel":["Kelvin", 5689663, 3035621452]}
print(amigos)
for key, value in amigos.items():
    print(key, "=", value)
historia_medica = {"temperatura":37.8,
                   "antecedentes familiares":None,
                   "prueba COVID-19":False,
                   "caso local":False,
                   "caso importado":True,
                   "sexo":"M",
                   "edad":56}
print(historia_medica)
for key, value in historia_medica.items():
    print(key, "=", value)
print(
    type(historia_medica)
)
#Final práctica tipos de datos, variables, print() y type()