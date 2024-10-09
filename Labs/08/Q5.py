import numpy as np

random_matrix = np.random.choice([2, 5, 9, 10], size=(4, 4))
identity_matrix = np.eye(4)
result_matrix = np.dot(random_matrix, identity_matrix)
odd_matrix = np.arange(1, 33, 2).reshape(4, 4)
final_matrix = result_matrix + odd_matrix

print(final_matrix)
