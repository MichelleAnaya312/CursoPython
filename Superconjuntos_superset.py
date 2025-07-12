# Solo se pueden usar 2 subconjuntos
A = {1, 2, 3, 4, 5}
B = {1, 2, 3, 4, 5}

"""Casos"""
"""B = {2, 5} todas True"""
"""B = {-3, 5} todas False"""
"""B = {1, 2, 3, 4, 5} todas True menos la última"""


print(f"Conjunto A: {A}\nConjunto B: {B}\n")

print("¿A es un superconjunto de B?\n")

es_superconjunto = A.issuperset(B)
print("Utilizando el método issuperset(): ", es_superconjunto)

# Operador de superconjunto inclusivo
es_superconjunto = A >= B
print("Utilizando el operador >=:", es_superconjunto)

# Operador de superconjunto estricto
es_superconjunto = A > B
print("Utilizando el operador >:", es_superconjunto)
