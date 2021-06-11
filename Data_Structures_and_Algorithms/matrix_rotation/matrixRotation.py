def rotateMatrix(matrix):
    for i in range(int(len(matrix) ** 0.5)):
        for j in range(i, len(matrix) - 1 - i):
            temp1 = matrix[j][len(matrix) - 1 - i]
            matrix[j][len(matrix) - 1 - i] = matrix[i][j]
            temp2 = matrix[len(matrix) - 1 - i][len(matrix) - 1 - j]
            matrix[len(matrix) - 1 - i][len(matrix) - 1 - j] = temp1
            temp1 = matrix[len(matrix) - 1 - j][i]
            matrix[len(matrix) - 1 - j][i] = temp2
            matrix[i][j] = temp1
    return matrix

import numpy as np

def printm(matrix):
    for row in matrix:
        print(row)
    
matrix = [list(np.arange(idx, idx + 5)) for idx in range(1,26,5)]
printm(matrix)
print()
printm(rotateMatrix(matrix))




