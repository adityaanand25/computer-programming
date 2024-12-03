Solve a system of linear equations represented in matrix form

import numpy as np
A = np.array([[2, 3, 1], [1, 2, 3], [3, 1, 2]])
b = np.array([7, 8, 9])
x = np.linalg.solve(A, b)
print(x)
