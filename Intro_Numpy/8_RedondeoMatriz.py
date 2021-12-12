import numpy as n

# Creación de las listas que serán utilizadas para la obtenmción de las matrices con numpy
matrizA = [[5, 8, 6], [2, 9, 12], [3, 7, 8]]
print(matrizA)

print() # Para hacer espacio

# Obtención de las matrices a partir de las listas de python
A = n.array(matrizA)
print(A)
print()

# Matriz inversa de A
A_inv = n.linalg.inv(A)

print("Inversa: ")
print(A_inv)

print()
inv_redondeada = n.around(A_inv, 4)
print(inv_redondeada)

# Comprobación
print()
print("Comprobación: ")
c = n.around(A.dot(inv_redondeada))
print(c)
