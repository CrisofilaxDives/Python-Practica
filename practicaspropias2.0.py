# Tipos de datos y condicionales

str_1 = "Pescado"
str_2 = "Mariscos y cefalopodos"
int_1 = 56
int_2 = 89
flt_1 = 1.9
flt_2 = 2.5
bool_f = False
none_1 = None
list_1 = list(("Azul", "Verde", "Morado"))
list_2 = list(range(1,4))
tuple_1 = tuple((12, 13, 14))
tuple_2 = tuple((20,))
set_1 = {"Perros", 3, True}
dict_1 = {
    "Especie":"Mamifero",
    "Tamaño":5.6,
    "ID":4555656456
}
print(type(flt_1))

# Str
print(str_1.upper())
print(str_2.lower())
print(str_1.swapcase())
print(str_2.replace("y", "And").capitalize())
print(str_1.count("s"))
print(str_2.find("f"))
print(str_1.index("c"))
print(len(str_2))
print(str_1.startswith("Pescado"))
print(str_2.endswith("cefalopodos"))
print(str_1.isalpha())
print(str_2.isnumeric())
print(str_2.split())
print(str_1.split("c"))
print(str_2[3])
print(str_1, ", ", str_2)
print(f"{str_1}, {str_2}")
print("{0}, {1}".format(str_1, str_2).capitalize())

# Int y Float
operacion = ((int_1 + flt_1) * (int_2 - flt_2) / flt_1)
print(operacion)
print(int_1 // int_2)
print(int_2 % int_1)

# Concatenación
print(str_1 + ", ", str_2)

# Bool y None
print("Pruebas del funcionamiento del dióxido de cloro en el cuerpo humano")
print(bool_f)
print("Pruebas de que el 5G causa COVID_19")
print(none_1)

# List
print(list_1[1])
print(len(list_2))
print("Azul" in list_1)
list_2[2] = 9
print(list_2)
list_1.append("Cafe")
print(list_1)
list_2.extend((15, 48 , 79))
print(list_2)
list_1.pop()
print(list_1)
list_2.pop(4)
print(list_2)
list_1.remove("Azul")
print(list_1)
# list_2.clear()
# print(list_2)
list_1.sort()
print(list_1)
list_1.sort(reverse = True)
print(list_1)
print(list_2.index(2))
print(list_1.count("Verde"))

# Tuples y Sets
# print(dir(set_1))
# print(dir(tuple_1))
print(tuple_1[1])
# del tuple_1
set_1.add("Limón")
print(set_1)
set_1.remove(3)
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

# Condicionales y loops
nombre = input("Ingrese su nombre: ")
if nombre == "Gustav" or nombre == "Helena":
    print(f"Welcome Commander, {nombre}")
elif nombre == "Hector":
    print(f"Welcome Capitan, {nombre}")
else:
    print(f"Welcome Soldier, {nombre}")

while True:
    try:
        ID = int(input("Escriba su número de usuario: "))
        if ID >= 0 and ID < 10:
            print("Bienvenido Diamante")
        elif ID >= 10 and ID < 50:
            print("Bienvenido Oro")
        elif ID >= 50 and ID < 100:
            print("Bienvenido Plata")
        else: 
            print("Bienvenido Bronce")
        break
    except:
        print("Erro. Escriba de nuevo su número de usuario.")

try:
    ahorros = int(input("Ingrese sus ahorros: "))
    if (not(ahorros == 0)):
        if ahorros < 100000:
            print("Siga ahorrando")
        elif ahorros >= 100000 and ahorros < 1000000:
            print("Tiene buenos ahorros")
        elif ahorros >= 1000000 and ahorros < 10000000:
            print("Puede invertir en bolsa")
        else:
            print("Puede invertir en bienes raices")
except:
    print("Ahorros no validos")

# Funciones
def imc(peso = 0, altura = 0):
    while True:
        try:
            peso = float(input("Ingrese su peso en Kg: "))
            break
        except:
            print("Peso no valido, intentelo de nuevo.")
    while True:
        try:
            altura = float(input("Ingrese su altura en m: "))
            break
        except:
            print("Altura no valido, intentelo de nuevo.")
    imc = peso / (altura ** 2)
    print(f"Su IMC es de {imc:.1f}")                            #Use formart() ":." "un numero de decimales"f para hacer que me mostrara solo 1 decimal
    print("Eso significa: ")
    if imc < 18.5:
        print("Bajo peso")
    elif imc >= 18.5 and imc < 25:
        print("Peso normal")
    elif imc >= 25 and imc < 30:
        print("Sobrepeso")
    else:
        print("Obesidad")
imc()

resta = lambda n1 = 0, n2 = 0: n1 - n2
print(resta(2, 8))

# Modulos
## Recordad que los modulos son tuyos, de otros o de python
## Propios
## Python
### Usa import "nombre del modulo" o con from "modulo" import "funcion_1", "funcion_2", "..."
## Otros
### Usa la funcion en consola de windows pi install "nombre del modulo"
