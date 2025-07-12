names_tuple = ("Ana", "Gerardo", "María", "Carlos", "Valentina")
print(names_tuple, "\n")

validator = 0

while validator == 0:
    number = int(input("Ingresa un número entero entre 0 y 4: "))

    if 0 <= number <= 4:
        print(f"El nombre es: {names_tuple[number]}")
        validator = 1
    else:
        print("¡Error! Número inválido, vuelve a intentar. \n")
