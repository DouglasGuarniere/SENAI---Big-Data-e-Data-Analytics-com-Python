import statistics

lista = {35, 37, 36, 34, 38, 35, 37, 37, 33, 36, 
38, 37,35, 37, 34, 33, 37, 36, 35, 38, 36, 35, 36, 37, 38, 
39, 37, 37, 36, 37, 33, 37, 35, 37, 39}

variancia = statistics.pvariance(lista)

print(f"Variancia:{variancia}")