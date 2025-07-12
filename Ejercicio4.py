print("Calculadora con una sola variable\n")

print("******************")
print("*Menu de opciones*")
print("******************\n")

print("1. Suma")
print("2. Resta")
print("3. Multipicación")
print("4. División")
print("5. División entera")
print("6. Exponente")
print("7. Modulo o resto\n")

opcion = int(input("Ingrese la opción deseada: "))


if opcion == 1:
    print("Elegiste suma\n")
    numero = int(input("Ingrese el primer número: "))
    numero += int(input("Ingrese el segundo número: "))
    
    print("El resultado de la suma es ", numero)
    
elif opcion == 2:
    print("Elegiste resta\n")
    numero = int(input("Ingrese el primer número: "))
    numero -= int(input("Ingrese el segundo número: "))
    
    print("El resultado de la resta es ", numero)
    
elif opcion == 3:
    print("Elegiste multiplicación\n")
    numero = int(input("Ingrese el primer número: "))
    numero *= int(input("Ingrese el segundo número: "))
    
    print("El resultado de la multiplicación es ", numero)
    
elif opcion == 4:
    print("Elegiste división\n")
    numero = float(input("Ingrese el primer número: "))
    numero /= float(input("Ingrese el segundo número: "))
    
    print("El resultado de la división es ", round(numero,2))
    
elif opcion == 5:
    print("Elegiste división entera\n")
    numero = int(input("Ingrese el primer número: "))
    numero //= int(input("Ingrese el segundo número: "))
    
    print("El resultado de la división entera es ", numero)
    
elif opcion == 6:
    print("Elegiste exponente\n")
    numero = int(input("Ingrese el primer número: "))
    numero **= int(input("Ingrese el segundo número: "))
    
    print("El resultado del exponente es ", numero)
    
elif opcion == 7:
    print("Elegiste modulo o resto\n")
    numero = int(input("Ingrese el primer número: "))
    numero %= int(input("Ingrese el segundo número: "))
    
    print("El resultado del modulo o resto es ", numero)
    
else: 
    print("Opción no disponible.")
