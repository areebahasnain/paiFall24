import numpy as np

student_data = np.array([('Areeba', 5.4, 10), ('Emman', 5.5, 9), ('Rumaisa', 5.6, 10)],
                        dtype=[('name', 'U10'), ('height', 'f4'), ('class', 'i4')])

sorted_data = np.sort(student_data, order=['class', 'height'])

print(sorted_data)
