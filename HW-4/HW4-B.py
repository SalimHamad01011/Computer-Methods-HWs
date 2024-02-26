from scipy.optimize import fsolve
import numpy as np

# Define the equations
equation1 = lambda x: x - 3 * np.cos(x)
equation2 = lambda x: np.cos(2 * x) * x**3

# Find roots using fsolve
root1 = fsolve(equation1, 0)
root2 = fsolve(equation2, [-1, 0, 1])

print(f'Root of x - 3*cos(x) = 0: {root1[0]:.4f}')
print(f'Roots of cos(2*x)*x^3 = 0: {root2}')
