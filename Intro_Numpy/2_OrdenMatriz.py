import numpy as np

listaM = [[1, 2, 4], [3, 5, 6]]
print(listaM)

matriz = np.array(listaM)
print(matriz)

F, C = matriz.shape

print("Filas:", F)
print("Columnas:", C)

print()

Filas = matriz.shape[0]
print("Filas:", Filas)