#Método rstrip
#al final de la cadena
cadena = "\tHola Ernesto\n"
print(cadena)

cadena = cadena.rstrip()
print(cadena)

#Método lstrip
#al inicio de la cadena
cadena = "\tHola Ernesto\n"
print(cadena)

cadena = cadena.lstrip("s tHo\t\n")
print(cadena)
