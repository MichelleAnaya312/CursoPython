
string = input("Ingresa una frase: ")
palabra = input("Ingresa la palabra que deseas eliminar: ")

substring = ""
indice = string.find(palabra)
substring = string[0:indice] + string[indice + len(palabra) + 1 : ]


print(f"Cadena con palabra eliminada: {substring}")
