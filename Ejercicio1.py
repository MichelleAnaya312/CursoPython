print("Rappy")
print("Cálculo de días de vacaciones\n")

nombre = input("Ingrese su nombre: ")
clave_depto = int(input("Ingrese la clave de su departamento: "))
antiguedad = int(input("Ingrese cuántos años de servicio tiene en la empresa: "))

if clave_depto == 1:
    print("Departamento: Atención al cliente")

    if antiguedad == 1 and antiguedad < 2:
        print(nombre, "recibirá 6 días de vacaciones.")
    elif antiguedad == 2 or antiguedad <= 6:
        print(nombre, "recibirá 14 días de vacaciones.")
    elif antiguedad >= 7:
        print(nombre, "recibirá 20 días de vacaciones.")
    else:
        print("No ingresó años de servicio válidos para calcular días de vacaciones.")
        
elif clave_depto == 2:
    print("Departamento: Logística")

    if antiguedad == 1 and antiguedad < 2:
        print(nombre, "recibirá 7 días de vacaciones.")
    elif antiguedad == 2 or antiguedad <= 6:
        print(nombre, "recibirá 15 días de vacaciones.")
    elif antiguedad >= 7:
        print(nombre, "recibirá 22 días de vacaciones.")
    else:
        print("No ingresó años de servicio válidos para calcular días de vacaciones.")

elif clave_depto == 3:
    print("Departamento: Gerencia")

    if antiguedad == 1 and antiguedad < 2:
        print(nombre, "recibirá 10 días de vacaciones.")
    elif antiguedad == 2 or antiguedad <= 6:
        print(nombre, "recibirá 20 días de vacaciones.")
    elif antiguedad >= 7:
        print(nombre, "recibirá 30 días de vacaciones.")
    else:
        print("No ingresó años de servicio válidos para calcular días de vacaciones.")
        
else:
    print("Departamento no disponible.")
