print("Sistema para calcular el promedio de un alumno")
nombre = input("Para comenzar, ¿Cuál es tu nombre?: ")

matematicas = int(input(nombre + " ¿Cuál es tu calificación en matemáticas?: "))
quimica = int(input(nombre + " ¿Cuál es tu calificación en quimica?: "))
biologia = int(input(nombre + " ¿Cuál es tu calificación en biologia?: "))

promedio = (matematicas + quimica + biologia) / 3
promedio = int(promedio)

if promedio >= 6:
    print('Felicidades '+ nombre + ' "aprobaste" con un promedio de: ', promedio)

print("Fin.")
