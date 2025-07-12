invitados = ["Carolina", "Juan", "Gerardo"]
amigos = ["Luis", "Ana"]

print(f"Lista invitados: {invitados} \n Lista amigos: {amigos}")

invitados.extend(amigos)
print(f"Lista invitados: {invitados}")

numeros = [10, 20]
print(f"\nLista numeros: {numeros}")

numeros.extend(range(30, 100, 10))
print(f"\nLista numeros: {numeros}")
