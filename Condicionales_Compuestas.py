""" num_uno = 5

if num_uno == 7:
    print("El número es cinco.")
else:
    print("El número no es cinco.")
print("Fin.") """


print("Sistema para calcular el promedio de un alumno.")
nombre = input("Para comenzar, ¿Cuál es tu nombre?: ")

matematicas = float(input(nombre + " ¿Cuál es tu calificación en matemáticas?: "))
quimica = float(input(nombre + " ¿Cuál es tu calificación en quimica?: "))
biologia = float(input(nombre + " ¿Cuál es tu calificación en biologia?: "))

promedio = (matematicas + quimica + biologia) / 3

if promedio >=6:
    print('Felicidades '+ nombre + " 'aprobaste' con un promedio de: ", promedio)
    print('Felicidades '+ nombre + " 'aprobaste' con un promedio de: ", round(promedio, 2))
else:
    print('Lo sentimos '+ nombre + " has 'reprobado' con un promedio de: ", promedio)
    print('Lo sentimos '+ nombre + " has 'reprobado' con un promedio de: ", round(promedio, 1))

print("Fin.")
