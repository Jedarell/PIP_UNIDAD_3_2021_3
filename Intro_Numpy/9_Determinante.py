import numpy as n

# Creación de las listas que serán utilizadas para la obtenmción de las matrices con numpy
matrizA = [[3, -1, -1], [2, 1, 0], [3, 1, 2]]
print(matrizA)

print() # Para hacer espacio

# Obtención de las matrices a partir de las listas de python
A = n.array(matrizA)
print(A)
print()

# Determinante de A
A_det = n.linalg.det(A)

print("Determinante: ")
print(n.round(A_det))


