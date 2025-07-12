#Operador and
print ("Conjunción (and)")
num_uno = int(input("Escribe un número mayor a 2 y menor a 5: "))

if num_uno > 2 and num_uno < 5:
    print("El número ", num_uno, " cumple con la condición.\n")
else:
    print("El número ", num_uno, " no cumple con la condición.\n")


#Operador or
print ("Disyunción (or)")
palabra = input("Para cumplir con la condición escribe 'si' o 'yes': ")

if palabra == "si" or palabra == "yes":
    print("La condición se ha cumplido.\n")
else:
    print("La condición no se ha cumplido.\n")


#Operador not
print ("Negación (not)")
num_uno = int(input("Ingresa un número igual a 5: "))

if not num_uno == 5:
    print("\n El número es diferente de cinco y si cumple la condición.\n")
else:
    print("\n El número es igual a cinco y no cumple la condición.\n")
