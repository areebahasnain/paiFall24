import numpy as np

even_numbers = np.arange(2, 20, 2).reshape(3, 3)
print("\Even Number Matrix:")
print(even_numbers)

even_numbers = even_numbers * 4
identity_matrix = np.eye(3)
result = np.dot(even_numbers, identity_matrix)

print("\nMatrix after multiplying by 4:")
print(even_numbers)

print("\nResultant matrix after multiplying with identity matrix:")
print(result)