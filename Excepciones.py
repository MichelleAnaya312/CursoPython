try:
    numero = int(input("Ingresa un número: "))
    resultado = 50 // numero
    print(f"50 / {numero} =", resultado)
    
except ValueError as ve:
    print(f"Debes ingresar un número entero: Error! {ve}")
except ZeroDivisionError as zde:
    print(f"No puedes dividir por cero: {zde}")
except Exception as e:
    print(f"Operación no válida: {e}")
    
else:
    # Se ejecuta si el try se cumplió
    print("else: - ¡Operación exitosa!")

finally:
    # Se ejecuta siempre
    print("finally: - ¡Fin del programa!")
