# Tipos de datos, condicionales, loops y funciones

# Proyecto de juegos de azar
# Para todas las funciones de azar, se necesitan generar datos al azar como referencia
# Una función útil es randint() que genera integers random en base a un rango.
import random

# Se debe hacer que las funciones de juego de hacer tambien lleven una forma de apostar
# Moneda
def moneda():
    dinero = 100
    print(f"""Bienvenido al programa de tirar la moneda.
Podrá apostar su dinero y ganar más.
En este momento tiene {dinero} monedas.""")
# input() del lado de la moneda
    while dinero > 0:
        while True:
            lado_moneda = input("""Escriba el lado de la moneda por la que quiere apostar.
Puede escribir 'Salir' para salir del programa.
'Cara' o 'Sello': """).lower()
            if lado_moneda == "salir":
                print("Qué tenga buen día")
                break
            else:
                if lado_moneda == "cara":
                    print("Usted escogió Cara.")
                    break
                elif lado_moneda == "sello":
                    print("Usted escogió Sello.")
                    break
                else:
                    print("""Hubo un error.
Intente de nuevo, escribir el lado de la moneda por la que quiere apostar.
'Cara' o 'Sello'.
    """)
                    continue
    # input() de la apuesta
        while True:
            apuesta = input("""
Escriba el valor de su apuesta.
Recuerde que no puede escribir una apuesta mayor a su dinero.
Puede escribir 'Salir' para salir del programa.
Escriba su apuesta: """).lower()
            if apuesta == "salir":
                break
            try:
                int_apuesta = int(apuesta)
                if int_apuesta >= 0 and int_apuesta <= dinero:
                    print(f"Usted apostó {int_apuesta} monedas")
                    break
                elif int_apuesta < 0:
                    print(f"La apuesta de {int_apuesta} monedas es menor que cero.")
                    print("Intende de nuevo.")
                    continue
                else:
                    print(f"La apuesta de {int_apuesta} monedas es mayor que su dinero.")
                    print("Intende de nuevo.")
                    continue
            except:
                print("Hubo un error. Intente de nuevo ingresar el valor de su apuesta.")
                continue
    # Tirando la moneda
        lado_random = random.randint(0, 1)
        print("Ahora miremos que lado de la moneda salío.")
        if lado_random == 0:
            print("La moneda salió en Cara")
            if lado_moneda == "cara":
                dinero += int_apuesta
                print(f"Ganaste {int_apuesta} monedas. Ahora tienes {dinero} monedas")
            else:
                print(f"Perdiste {int_apuesta} monedas. Ahora tienes {dinero} monedas")
        if lado_random == 1:
            print("La moneda salió en Sello")
            if lado_moneda == "sello":
                dinero += int_apuesta
                print(f"Ganaste {int_apuesta} monedas. Ahora tienes {dinero} monedas")
            else:
                dinero -= int_apuesta
                print(f"Perdiste {int_apuesta} monedas. Ahora tienes {dinero} monedas")
# Condiciones para salir del loop y terminar las apuestas
        if lado_moneda == "terminar" or apuesta == "terminar":
            print(f"""
Gracias por sus apuestas.
Usted ganó {dinero}.
Qué tenga buen día.""")
            break
        elif dinero == 0:
            print("""
Su dinero ha llegado a 0.
Qué tenga buen día.""")
            break
            
moneda()