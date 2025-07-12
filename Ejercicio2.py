print("***************************************")
print("Determinar si un número es par o impar")
print("***************************************\n")

numero = int(input("Ingresa un número entero: "))

if numero % 2 == 0:
    print("El número ",numero, " es par.")
elif numero % 2 == 1:
    print("El número ",numero, " es impar.")
    
