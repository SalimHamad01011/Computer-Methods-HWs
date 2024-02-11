import numpy as np
import scipy.linalg

def is_symmetric_positive_definite(A):
    # Check if matrix A is symmetric
    if not np.allclose(A, A.T):
        return False

    # Check if matrix A is positive definite using eigenvalues
    eigenvalues = np.linalg.eigvals(A)
    if np.all(eigenvalues > 0):
        return True
    else:
        return False

def solve_linear_system(A, b):
    if is_symmetric_positive_definite(A):
        # Use Cholesky method
        L = np.linalg.cholesky(A)
        y = np.linalg.solve(L, b)
        x = np.linalg.solve(L.T, y)
        method_used = "Cholesky"
    else:
        # Use Doolittle method
        P, L, U = scipy.linalg.lu(A)
        y = np.linalg.solve(L, P @ b)
        x = np.linalg.solve(U, y)
        method_used = "Doolittle"

    return x, method_used

def main_linear_systems():
    # Test cases
    A1 = np.array([[1, -1, 3, 2], [-1, 5, -5, 2], [3, -5, 19, 3], [2, 4, 3, 21]])
    b1 = np.array([15, -35, 94, 1])

    A2 = np.array([[4, 2, 4, 0], [2, 2, 3, 2], [4, 3, 6, 3], [0, 2, 3, 9]])
    b2 = np.array([20, 36, 60, 122])

    solution1, method_used1 = solve_linear_system(A1, b1)
    solution2, method_used2 = solve_linear_system(A2, b2)

    print(f"Solutions for System 1 ({method_used1} method): {solution1}")
    print(f"Solutions for System 2 ({method_used2} method): {solution2}")

if __name__ == "__main__":
    main_linear_systems()
