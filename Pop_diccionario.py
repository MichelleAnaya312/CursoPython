dict_name = {"a": 1,
              "b": 2,
              "c": 3
              }
print(f"Diccionario Original: {dict_name}")

last_value = dict_name.pop("b")
print(f"Diccionario modificado: {dict_name}")
print(f"Valor eliminado: {last_value}")

# La clave no existe en diccionario, pero se coloca valor por defecto para evitar error
print()
dict_name = {"a": 1,
              "b": 2,
              "c":3
              }
print(f"Diccionario Original: {dict_name}")

last_value = dict_name.pop("z", "No se encuentra la clave dentro del diccionario.")
print(f"Diccionario modificado: {dict_name}")
print(f"Valor eliminado: {last_value}")
