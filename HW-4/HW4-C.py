import numpy as np
from scipy.linalg import solve

# Define the coefficients matrix and the right-hand side vector for the first system
coefficients1 = np.array([[3, 1, -1], [1, 4, 1], [2, 1, 2]])
rhs1 = np.array([2, 12, 10])

# Define the coefficients matrix and the right-hand side vector for the second system
coefficients2 = np.array([[1, -10, 2, 4], [3, 1, 4, 12], [9, 2, 3, 4], [-1, 2, 7, 3]])
rhs2 = np.array([2,12,21,37])

# Solve the linear systems
solution1 = solve(coefficients1, rhs1)

# Use lstsq for the overdetermined system
solution2, residuals, rank, singular_values = np.linalg.lstsq(coefficients2[:, :-1], rhs2, rcond=None)

# Print the solutions
print(f'Solution for the first system: {solution1}')
print(f'Solution for the modified second system: {solution2}')
