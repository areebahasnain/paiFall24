import numpy as np

matrix1 = np.random.randint(1, 5, size=(5, 3))
matrix2 = np.random.randint(1, 5, size=(3, 2))

result_matrix = np.dot(matrix1, matrix2)

print(result_matrix)
