import numpy as np

def GaussSeidel(Aaug, x, Niter=15):
    """
    Use the Gauss-Seidel method to estimate the solution to a set of N linear equations Ax = b.

    Parameters:
    Aaug (numpy.ndarray): Augmented matrix containing [A | b].
    x (numpy.ndarray): Initial guess.
    Niter (int): Number of iterations.

    Returns:
    numpy.ndarray: Final new x vector.
    """
    A, b = Aaug[:, :-1], Aaug[:, -1]
    N = len(x)

    for k in range(Niter):
        for i in range(N):
            x[i] = (b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]

    return x

def main():
    # Test cases
    A1 = np.array([[3, 1, -1], [1, 4, 1], [2, 1, 2]])
    b1 = np.array([2, 12, 10])
    x1 = np.zeros_like(b1, dtype=float)
    solution1 = GaussSeidel(np.column_stack((A1, b1)), x1)

    A2 = np.array([[1, -10, 2, 4], [3, 1, 4, 12], [9, 2, 3, 4], [-1, 2, 7, 3]])
    b2 = np.array([2, 12, 21, 37])
    x2 = np.zeros_like(b2, dtype=float)
    solution2 = GaussSeidel(np.column_stack((A2, b2)), x2)

    print(f'Solutions for [[3, 1, -1], [1, 4, 1], [2, 1, 2]]: {solution1}')
    print(f'Solutions for [[1, -10, 2, 4], [3, 1, 4, 12], [9, 2, 3, 4], [-1, 2, 7, 3]]: {solution2}')

if __name__ == "__main__":
    main()
