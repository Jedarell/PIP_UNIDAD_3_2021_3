import numpy as n

# Creación de las listas que serán utilizadas para la obtenmción de las matrices con numpy
matrizA = [[1, 2, 4], [3, 5, 6]]
matrizB = [[5, 8, 6], [2, 9, 12]]
print(matrizA)
print(matrizB)

print() # Para hacer espacio

# Obtención de las matrices a partir de las listas de python
A = n.array(matrizA)
B = n.array(matrizB)
print(A)
print()
print(B)

C = A + B
print()
print("Resultado de la SUMA-RESTA de A + B")
print(C)

B_t = B.T
print()
print("B Transpuesta:")
print(B_t)

C = A + B_t # Esto genera un error, porque unicamente se pueden sumar-restar matrices
            # del mismo ORDEN
print()
print("Resultado de la SUMA-RESTA de A + B_t")
print(C)
