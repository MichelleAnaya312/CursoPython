rows = int(input("¿Cuántas filas tendrá la matriz?: "))
columns = int(input("¿Cuántas columnas tendrá la matriz?: "))

matrix = []

for row_position in range(rows):
    row = []
    for element in range(columns):
        row.append(int(input(f"Ingresa un elemento a la fila {row_position}: ")))
    matrix.append(row)

print("Mostrar todos los elementos de la matriz fila por fila")
for row in matrix:
    print(row)
