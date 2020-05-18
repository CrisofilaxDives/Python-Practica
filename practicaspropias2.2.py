# Tipos de datos, condicionales y loops

str_1 = "hola"
str_2 = "pescado y pollo"
int_1 = 3
int_2 = 9
flt_1 = 1.2
flt_2 = 8.6
bool_t = True
none_1 = None
list_1 = list(("tierra", "agua", "fuego"))
list_2 = list(range(1, 6))
tuple_1 = tuple((1, 1.5, "perro"))
tuple_2 = tuple((1,))
set_1 = {1, 2.3, False} 
dict_1 = {
    "dueño":"pepe",
    "id":4552,
    "vacunas":True
}

# Str 
print(str_1.upper())
print(str_2.lower())
print(str_1.swapcase())
print(str_2.replace("y", "and").capitalize())
print(str_2.split())
print(str_1.split("l"))
print(str_2.isnumeric())
print(str_1.isalpha())
print(str_2.count("o"))
print(len(str_1))
print(str_2.startswith("pescado"))
print(str_2.endswith("pollo"))
print(str_1.find("o"))
print(str_2.index("e"))
print(str_1[2])
print(str_1, ", ", str_2)
print(f"{str_1}, {str_2}")
print("{0}, {1}".format(str_1, str_2))

# Concatenación
print(str_1 + ", " + str_2)

# Int y Float
s_1 = (int_1 + int_2) * (flt_1 - flt_2)
print(s_1)
print(int_1 / flt_1)
print(int_1 // flt_1)
print(int_1 % flt_1)

# List
print(list_1[2])
list_2.append(6)
print(list_2)
list_1.extend(("aire", "rayo"))
print(list_1)
list_2[5] = 7
print(list_2)
list_2.pop(1)
list_1.pop()
print(list_1)
print(list_2)
list_1.remove("tierra")
print(list_1)
# list_2.clear()
# print(list_2)
print(list_1.index("aire"))
print(7 in list_2)
list_1.sort()
print(list_1)
list_1.sort(reverse = True)
print(list_1)
print(list_2.count(7))

# Bool y Loops
print("False * False = True")
print(bool_t)
print("Str + Int = ")
print(none_1)

# Set y Tuples
set_1.add("limón")
print(set_1)
set_1.remove(2.3)
print(set_1)
# set_1.clear()
# print(set_1)
print(tuple_1[1])
# del tuple_1
# print(tuple_1)
# print(dir(tuple_1))

# Dict
for keys, values in dict_1.items():
    print(keys, "=", values)
print(dict_1.items())
print(dict_1.keys())
print(dict_1.values())
# del dict_1
# dict_1.clear()
# print(dict_1)

# Condicionales y Loops
totales = list(())                                  # En donde se guardaran los precios
error_messsage = "Hubo un error. Intente de nuevo"  
x = 0                                               # Variable referencia para la suma de precios en el for
while True:
    strx = input("Escriba los precios: ")
    if strx == "salir":
        break
    try:
        intx = float(strx)
        totales.append(intx)
    except:
        print("Hubo un error. Intente de nuevo")
        continue
for i in totales:
    x = x + i
print(totales)
print(x)

# n_prod = nombre del producto, p_prod = precio del producto
def calprecios(n_prod = 0, p_prod = 0):     
    # n_prod como key del dict
    while True:
        n_prod = input("Escriba el nombre del producto: ")
        if n_prod == "salir":
            break
        try:
            # hago de n_prod un str                
            str_n_prod = str(n_prod)       
            break
        except:
            print(error_messsage)
    while True:
        p_prod = input("Escriba el precio del producto: ")
        if p_prod == "salir":
            break
        try:  
            # p_prod como un float
            flt_p_prod = float(p_prod)
            break
        except:
            print(error_messsage)
    # l_prod como el dict              
    l_prod = {str_n_prod:flt_p_prod} 
    for keys, values in l_prod.items():
        print(keys, "=", values)
    x = 0
    for i in l_prod.values():
        x = x + i
        print(x)    
calprecios()
    

