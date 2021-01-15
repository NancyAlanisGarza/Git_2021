# defining a list
my_list = ('2', '5', [1,2])
print(my_list)
#te dice que methods pueden usarse dentro de la variable
print(dir(my_list))
# index, comienza de 0 a contar
print(my_list[1])
#index una lista dentro de otra lista
print(my_list[2][1])
#para ver la longitud de la lista
print(len(my_list))
#print(my_list[len(my_list)-1]
#linea 11 si me funciona la linea 12 no **NO ME SALIO**
# Sumar Lista
numeros_list = [1,2,3,4,5]
print(sum(numeros_list))
#sorterar listas
shuffled_list = [1,0,4,6,2]
shuffled_list.sort()
print(shuffled_list)
# Modifying lists in place
#append agrega cosas a tu lista, agregó el 6
numeros_list.append([10,99])
print(numeros_list)
#extend combina dos listas
numeros_list.extend([7,8,9])
print(numeros_list)
#replace elementwise with indexing
numeros_list[2] = 55
print(numeros_list)
# usando pop te regresa lo que habías quedado / remueve algo
print(numeros_list.pop(2))
print(numeros_list)
#si no le especificas al final el index a quitar te quita el último index, te modifica la lista
print(numeros_list.pop())
print(numeros_list)
# remove
numeros_list.append(3)
print(numeros_list)
numeros_list.remove(3)
print(numeros_list)
print(numeros_list.pop(4))
print(numeros_list)
print(numeros_list.append((5,55,67)))
print(numeros_list)
# Converting Between List and Strings / SPLIT
my_str = 'La casa fantastica'
splt_str = my_str.split()
print(splt_str)
#puedes poner dentro del paréntesis el caracter que quieras usar como seprardor
# Join es para concatenar una lista 
my_join = 'Los pájaros verdes'
splt_join = my_join.split()
print(splt_join)
print(' '.join(splt_join))
print(splt_join)
print(my_join)
print(splt_join)
print('xxxxx'.join(splt_join))
#mostrar lo que esta dentro de la lista
print(list(my_str))
#slicing de una lista, sacar elementos de una lista
print(numeros_list)
print(numeros_list[0:3])
print(numeros_list[4])
print(numeros_list[:3])