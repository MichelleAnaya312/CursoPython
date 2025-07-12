# Sin utilizar expresiones de comprensión
cuadrados = []

# del 0 al 9
for x in range(10):
    cuadrado = x**2
    cuadrados.append(cuadrado)

print("Sin expresiones de comprensión: ", cuadrados)



# Utilizando expresiones de comprensión
# [expresion for elemento in iterable if condicion]

cuadrados = [x**2 for x in range(10)]
print("Con expresiones de comprensión: ", cuadrados)



""" Desarrollar un programa en Python que genere
una lista con los cuadrados de los números pares
en el rango del 0 al 9."""

# Sin utilizar expresiones de comprensión
cuadrados = []

# del 0 al 9
for x in range(10):
    if x%2==0:
        cuadrado = x**2
        cuadrados.append(cuadrado)

print("Sin expresiones de comprensión: ", cuadrados)

# Utilizando expresiones de comprensión
# [expresion for elemento in iterable if condicion]

cuadrados = [x**2 for x in range(10) if x%2==0]
print("Con expresiones de comprensión: ", cuadrados)


# Creando un diccionario con expresiones de comprensión
print("\n\nDiccionario creado con expresiones de comprensión: ")

# Lista que contiene tuplas
personas = [("Carlos", 30), ("Gerardo", 25), ("Maria", 35)]

#Convertir a diccionario
diccionarios_personas = {nombre: edad for nombre, edad in personas if edad >= 30}
print("Diccionario personas: ", diccionarios_personas)















