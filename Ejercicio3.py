print("***********************************************")
print("¿Cuál es el número más grande de tres números?")
print("***********************************************\n")

numero_uno = int(input("Ingrese el primer número: "))
numero_dos = int(input("Ingrese el segundo número: "))
numero_tres = int(input("Ingrese el tercer número: "))

if numero_uno > numero_dos and numero_uno > numero_tres:
    print("El número ",numero_uno, " es el número más grande de los tres.")
elif numero_dos > numero_uno and numero_dos > numero_tres:
    print("El número ",numero_dos, " es el número más grande de los tres.")
elif numero_tres > numero_uno and numero_tres > numero_dos:
    print("El número ",numero_tres, " es el número más grande de los tres.")
