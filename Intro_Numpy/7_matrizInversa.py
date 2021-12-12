import numpy as n

# Creación de las listas que serán utilizadas para la obtención de las matrices con numpy
matrizA = [[1, 2, 4], [3, 5, 6]]
matrizB  = [[5, 8, 6], [2, 9, 12], [3, 7, 8]]
print(matrizA)
print(matrizB)

print() # Para hacer espacio

# Obtención de las matrices a partir de las li+stas de python
A = n.array(matrizA)
B = n.array(matrizB)
print(A)
print()
print(B)


# REQUISITO PARA MULTIPLICAR MATRICES:
    # que la matriz origen sea cuadrada

# Consideraciones:  A es una matriza rectangular y B es una matriz cuadrada

# A_inv = n.linalg.inv(A)       # no se puede porque es rectangular

B_inv = n.linalg.inv(B)

print()
print("Resultado de B inversa:")
print(B_inv)

# Comprobación: B * Binv = Binv * B = I (I = matriz identidad)

# La matriz identidad es aquella que su diagonal principal tiene 1´s y el resto de elementos son 0
print()
print("Comprobacion 1: ")
print(B.dot(B_inv))
print()
print("Matriz identidad redondeada: ")
print(B.dot(B_inv))

print()
print("Comprobacion 2: ")
print(B_inv.dot(B))


