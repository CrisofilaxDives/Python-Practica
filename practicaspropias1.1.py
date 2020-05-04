#Tipos de datos y variables

#Strings
print("Practicaremos a la par tipos de datos y variables.")
print("Tembién has la prueba de type() a una variable y concatena las frases.")
print("Así que, crea 5 Strings y guardalos en variables para hacer print():")
string_1 = "Me gusta Python."
print(string_1)
string_2 = "Estoy aprendiendo sobre tipos de datos y variables."
print(string_2)
string_3 = "Aún tengo que repasar sobre los Dictionary, no lo entiendo bien."
print(string_3)
string_4 = "Me anima poder pensar en usar Python para algo útil o divertido."
print(string_4)
string_5 = "Hacer Strings es bastante fácil."
print(string_5)
prueba_de_type = "Prueba de type():"
print(prueba_de_type)
print(string_5)
print(
    type(string_5)
)
print("Concatenación:")
concatencion = string_1 + " " + string_2 + " " + string_3 + " " + string_4 + " " + string_5
print(concatencion)
print("¡Muy bien! Sigamos con Integers.")

#Integers
print("Ahora has variables con 5 números, has la prueba de type() a una y práctiquemos al final la suma:")
integer_1 = 1125
print(integer_1)
integer_2 = 2653
print(integer_2)
integer_3 = 3654
print(integer_3)
integer_4 = 4963
print(integer_4)
integer_5 = 5878
print(integer_5)
print("La suma de:")
suma_texto_1 = integer_1, "+", integer_2, "+", integer_3, "+", integer_4, "+", integer_5 #No sé por qué al ejecutarlo se ve con parentesis y '' en los +.
print(suma_texto_1)
print("Es igual a:")
suma_1 = integer_1 + integer_2 + integer_3 + integer_4 + integer_5
print(suma_1)
print(prueba_de_type)
print(suma_1)
print(
    type(suma_1)
)
print("¡Super! Sigamos con Floats.")

#Floats
print("Has lo mismo que con los Integers con los Floats.")
print("Las 5 variables:")
float_1 = 1.6
print(float_1)
float_2 = 2.4
print(float_2)
float_3 = 3.5
print(float_3)
float_4 = 4.9
print(float_4)
float_5 = 5.8
print(float_5)
print("La suma de:")
suma_texto_2 = float_1, "+", float_2, "+", float_3, "+", float_4, "+", float_5
print(suma_texto_2)
print("Es igua a:")
suma_2 = float_1 + float_2 + float_3 + float_4 + float_5
print(suma_2)
print(prueba_de_type)
print(suma_2)
print(
    type(suma_2)
)
print("Buen trabajo. Ahora sigamos con Booleans.")

#Booleans
print("Has tres preguntas en variables y responde con Booleans y has una prueba de type().")
print("Preguntas:")
pregunta_1 = "¿Hay pruebas fuertes de vida extraterreste?"
print(pregunta_1)
respuesta_1 = False
print(respuesta_1)
pregunta_2 = "¿La suerte es mayor que la disciplina?"
print(pregunta_2)
respuesta_2 = False
print(respuesta_2)
pregunta_3 = "¿Tienes libros de J. R. R. Tolkien?"
print(pregunta_3)
respuesta_3 = True
print(respuesta_3)
print(prueba_de_type)
print(respuesta_3)
print(
    type(respuesta_3)
)
print("Super. Ahora sigamos con None.")

#None
print("Has lo mismo que con los Booleans.")
print("Preguntas:")
pregunta_4 = "Ganas del partido del gobierno de Colombia de eliminar la corrupción."
print(pregunta_4)
none = None
print(none)
pregunta_5 = "Cambio en el salario de los médicos en los últimos 20 años en Colombia."
print(pregunta_5)
print(none)
pregunta_6 = "Pruebas de como Petro destruye Colombia."
print(pregunta_6)
print(none)
print(prueba_de_type)
print(none)
print(
    type(none)
)
print("Genial. Ahora hagamos Lists.")

#Lists
print("Has 3 Lists usando los distintos tipos de datos y has una prueba de type():")
list_1 = [string_1, integer_1, float_1, respuesta_1, none]
list_2 = [string_2, integer_2, float_2, respuesta_2, none]
list_3 = [string_3, integer_3, float_3, respuesta_3, none]
print(list_1)
print(list_2)
print(list_3)
print(prueba_de_type)
print(list_3)
print(
    type(list_3)
)
print("Muy bien. Ahora hagamos Tuples.")

#Tuple
print("Has lo mismo que con los List:")
tuple_1 = (string_4, integer_4, float_4, respuesta_1, none)
tuple_2 = (string_5, integer_5, float_5, respuesta_2, none)
tuple_3 = (string_1, integer_2, float_3, respuesta_3, none)
print(tuple_1)
print(tuple_2)
print(tuple_3)
print(prueba_de_type)
print(tuple_3)
print(
    type(tuple_3)
)

#Dictionary
print(string_3)
print("Pero ví este vídeo de YouTube:")
print("'Python Dictionaries || Python Tutorial || Learn Python Programming'")
print("Su URL es:")
print("https://www.youtube.com/watch?v=XCcpzWs-CI4")
print("Además, gracias a los post de Reddit, GitHub y Stack Overflow, entendí mejor el tema.")
print("Así que crearé 3 Dictionaries:")
dictionary_1 = {"animal":"gato", "numero_patas":4, "cola":True, "edad":3.6, "nombre":None}
print(dictionary_1)
for key, value in dictionary_1.items(): #Aprendí esto mirando el vídeo y los post, aunque no se cómo funciona.
    print(key, "=", value)
dictionary_2 = {
    "Casa 1":["2 pisos", "3 baños", "2 habitaciones", "1 estudio", "1 jardín"],
    "Casa 2":["1 piso", "2 baños", "3 habitaciones", "0 estudios", "0 jardines"]
    }
print(dictionary_2)
for key, value in dictionary_2.items():
    print(key, "=", value)
dictionary_3 = {"pisos":3, "baños":4, "habitaciones":5, "estudios":0, "jardín":None, "color":"azul", "m^2":164.3, "colegio_cerca":False, "trabajo_cerca":True}
print(dictionary_3)
for key, value in dictionary_3.items():
    print(key, "=", value)
print("Muy bien. Con esto practicamos tipos de datos y variables, y resuelvo mi duda con los Dictionary.")
