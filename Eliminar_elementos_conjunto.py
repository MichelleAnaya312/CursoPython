# Utilizando el método remove()
print("---Utilizando el método remove():")
vocales = {"a", "e", "i", "o", "u"}

vocales.remove('i')
print("vocales.remove('i'): ", vocales, "\n")

""" # Eliminar elemento que no pertenece al conjunto
vocales.remove('z')
print("vocales.remove('z'): ", vocales, "\n")
# Error: KeyError: 'z' """


# Utilizando el método discard()
print("---Utilizando el método discard():")
vocales = {"a", "e", "i", "o", "u"}

vocales.remove('a')
print("vocales.discard('a'): ", vocales, "\n")

""" # Eliminar elemento que no pertenece al conjunto
vocales.discard('z')
print("vocales.discard('z'): ", vocales, "\n")
# No genera un error """


# Evitar error utilizando el método remove()
print("---Evitar error utilizando el método remove():")
vocales = {"a", "e", "i", "o", "u"}

elemento = "z"
if elemento in vocales:
    vocales.remove(elemento)
    print("vocales.remove(elemento): ", vocales, "\n")
else:
    print(f"{elemento} no está en el conjunto vocales.")






    
