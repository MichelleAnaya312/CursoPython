try:
    num = int(input("Ingresa un número entero para convertirlo a romano: "))
    if 0 < num < 4000:
        # Lista de miles en números romanos. Los índices representan:
        # 1 => "M", 2 => "MM", 3 => "MMM"
        M = ["", "M", "MM", "MMM"]

        # Lista de centenas (100–900) en números romanos.
        # Índices: 
        # 1 => "C", 2 => "CC", 3 => "CCC", 4 => "CD", 5 => "D",
        # 6 => "DC", 7 => "DCC", 8 => "DCCC", 9 => "CM"
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        
        # Lista de decenas (10–90) en números romanos.
        # Índices:
        # 1 => "X", 2 => "XX", 3 => "XXX", 4 => "XL", 5 => "L",
        # 6 => "LX", 7 => "LXX", 8 => "LXXX", 9 => "XC"
        D = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]

        # Lista de unidades (1–9) en números romanos.
        # Índices:
        # 1 => "I", 2 => "II", 3 => "III", 4 => "IV", 5 => "V",
        # 6 => "VI", 7 => "VII", 8 => "VIII", 9 => "IX"
        U = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        print(f"{M[num // 1000]}{C[(num % 1000) // 100]}{D[(num % 100) // 10]}{U[num % 10]}")
        
    else:
        print("El número ingresado debe estar en un rango entre 1 y 3999")

except ValueError:
    print("Debes ingresar un valor entero.")
except Exception as e:
    print("Valor no válido: ", e)
