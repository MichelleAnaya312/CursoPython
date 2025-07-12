tabla = int(input("¿Qué tabla de multiplicar quieres ver?: "))

"""print("La tabla del ",tabla, " es: \n")"""
print(f"La tabla del {tabla} es: ")

"""for indice in range(0,11):
    multiplicacion = tabla * indice
    print("", tabla, " * ", indice, " = ", multiplicacion)"""
    
for i in range (11):
    print(f"{tabla} x {i} = {tabla*i}")
    
