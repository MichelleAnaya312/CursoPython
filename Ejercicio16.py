nums_tuple = (5, 8, 3, 3, 1, 6, 2)
print(f"Tupla original: {nums_tuple} \n")

num = int(input("¿Cuál de estos números quieres modificar por 0?: "))
# La tupla se convierta a lista para editar sus valores
nums_tuple = list(nums_tuple)
len_tuple = len(nums_tuple)

for index in range(len_tuple):
    if nums_tuple[index] == num:
        nums_tuple[index] = 0
        
# La lista se convierta a tupla 
nums_tuple = tuple(nums_tuple)

print(f"\nTupla modificada: {nums_tuple} \n")
