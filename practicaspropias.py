#Tipos de datos

#String
print("Hola")
print(
    type("Hola")
)
print("¿Cómo estás?")
print(
    type("¿Cómo estás?")
)
print("¿Estás aprendiendo Python?")
print(
    type("¿Estás aprendiendo Python?")
)
print("¡Super!")
print(
    type("¡Super!")
)
print("¿Qué tal si escribes algunos números?")
print(
    type("¿Qué tal si escribes algunos números?")
)

#Integer
print(1)
print(
    type(1)
)
print(2)
print(
    type(2)
)
print(3)
print(
    type(3)
)
print("¡Muy bien! ¿Qué tal unos números decimales?")

#Float
print(1.1)
print(
    type(1.1)
)
print(1.2)
print(
    type(1.2)
)
print(1.3)
print(
    type(1.3)
)
print("¡Genial! ¿Y si los sumas?")

#Suma
print("1 + 2 + 3 + 1.1 + 1.2 + 1.3")
print("¿Es igual a?")
print(1 + 2 + 3 + 1.1 + 1.2 + 1.3)
print("¡Super! ¿Y si concatenas una frase?")

#Concatenación
print("Organiza en una frase las palabras:")
print("Estoy")
print(" ")
print("practicando")
print(" ")
print("Python")
print("Estoy" + " " + "practicando" + " " + "Python")
print("Ahora usemos booleans")

#Boolean
print("Responde usando 'False' o 'True'")
print("¿La tierra es plana?")
print(False)
print(
    type(False)
)
print("¿Tienes 30 años?")
print(False)
print(
    type(False)
)
print("¿Te gustan las hamburguesas?")
print(True)
print(
    type(True)
)
print("¿Te gusta Python?")
print(True)
print(
    type(True)
)
print("¡Muy bien! ¿Qué tal si hacemos agrupaciones?")

#List
print("Organiza números enteros, decimales, palabras y booleans en listas separadas y luego, unelas")
print("Los números enteros:")
print(
    [1, 2, 3, 4, 5]
)
print(
    type(
        [1, 2, 3, 4, 5]
    )
)
print("Luego los números decimales:")
print(
    [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
)
print(
    type(
        [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
    )
)
print("Ahora las palabras:")
print(
    ["Uno", "Dos", "Tres", "Cuatro", "Cinco"]
)
print(
    type(
        ["Uno", "Dos", "Tres", "Cuatro", "Cinco"]
    )
)
print("Después los booleans:")
print(
    [True, True, False, True, False]
)
print(
    type(
        [True, True, False, True, False]
    )
)
print("Por último, unelos todos en una lista:")
print(
    [1, 2, 3, 4, 5, 1.0, 
    1.1, 1.2, 1.3, 1.4, 1.5, 
    "Uno", "Dos", "Tres", "Cuatro", "Cinco", 
    True, True, False, True, False]
)
print(
    type(
        [1, 2, 3, 4, 5, 
        1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 
        "Uno", "Dos", "Tres", "Cuatro", "Cinco", 
        True, True, False, True, False]
    )
)
print("¡Buen trabajo! Hagamos un Tuple")

#Tuple
print("Has dos Tuple con las cosas que no cambiarías nunca:")
print(
    ("Limón", "Mango", 11, 3.3, True)
)
print(
    type(
        ("Limón", "Mango", 11, 3.3, True)
    )
)
print(
    ("Papitas", 33, 7.7, "ewe")
)
print(
    type(
       ("Papitas", 33, 7.7, "ewe") 
    )
)
print("Bien hecho, hagamos un Dictionary")

#Dictionary
print("Has un Dictionary de mamiferos y reptiles")
print(                          #No sé porque solo hace print() en el 1° y ultimo item de Mamifero y Reptil,
    {                           #no todos.
        "Mamifero":"Gato",
        "Reptil":"Lagartija",
        "Mamifero":"Perro",
        "Reptil":"Tortuga",
        "Reptil":"Serpiente",
        "Mamifero":"Koala"
    }
)
print(
    type(
        {
        "Mamifero":"Gato",
        "Reptil":"Lagartija",
        "Mamifero":"Perro",
        "Reptil":"Tortuga",
        "Mamifero":"Koala",
        "Reptil":"Serpiente"
        }
    )
)
print("Genial, por último usemos None")

#None
print("Completa las frases con None")
print("Pruebas de que el autismo es causado por las vacunas:")
print(None)
print(
    type(None)
)
print("Evidencia de que el 5G causa COVID-19:")
print(None)
print(
    type(None)
)
print("Pruebas de contundentes y claras de que no se llegó a la Luna:")
print(None)
print(
    type(None)
)
print("Muy buen trabajo, con esto repasamos los tipos de datos, print() y type()")