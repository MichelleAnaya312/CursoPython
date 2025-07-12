numeros = []

longitud_lista = int(input("¿Cuántos números enteros contendrá la lista?: "))

for _ in range(longitud_lista):
    numeros.append(int(input("Ingresa un número entero: ")))
    
print(f"Lista: {numeros} \nLa suma total de los elementos es: {sum(numeros)}")

