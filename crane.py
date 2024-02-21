import numpy as np


A = np.array([[1, 1, 7],
              [1, 2, 8],
              [6, 6, 4]])



# Função para calcular o determinante de uma matriz 3x3
def det_3x3(matrix):
    return (matrix[0,0] * matrix[1,1] * matrix[2,2] +
            matrix[0,1] * matrix[1,2] * matrix[2,0] +
            matrix[0,2] * matrix[1,0] * matrix[2,1] -
            matrix[0,2] * matrix[1,1] * matrix[2,0] -
            matrix[0,0] * matrix[1,2] * matrix[2,1] -
            matrix[0,1] * matrix[1,0] * matrix[2,2])

determinante= det_3x3(A)
print(determinante)