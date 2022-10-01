import statistics

lista_de_valores = (1, 7, 3, 8, 6, 1, 7, 7, 0, 3, 6, 7,1, 7, 
8, 0, 7, 3, 1, 6, 3, 1, 3, 7, 6, 9, 7, 7, 3, 7, 0, 7, 1, 7, 
9)

moda = statistics.mode(lista_de_valores)

print(moda)