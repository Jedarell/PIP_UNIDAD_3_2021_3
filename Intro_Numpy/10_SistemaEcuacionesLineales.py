import numpy as n

# Creación de las listas que serán utilizadas para la obtenmción de las matrices con numpy
matrizCoef = [[3, 1], [4, -3]]
matrizTI = [22, -1]
print(matrizCoef)
print(matrizTI)

print() # Para hacer espacio

# Obtención de las matrices a partir de las listas de python
C = n.array(matrizCoef)
T = n.array(matrizTI)
print(C)
print(T)
print()

raices = n.linalg.solve(C, T)
print("Raices: ")
print(raices)