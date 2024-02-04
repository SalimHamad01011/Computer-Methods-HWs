import math


def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    Use the Secant Method to find the root of fcn(x) in the neighborhood of x0 and x1.

    Parameters:
    fcn (callable): Function for which we want to find the root.
    x0, x1 (float): Two x values in the neighborhood of the root.
    maxiter (int): Maximum number of iterations.
    xtol (float): Tolerance for convergence.

    Returns:
    float: Final estimate of the root.
    """
    iter_count = 0

    while iter_count < maxiter:
        xnew = x1 - fcn(x1) * (x1 - x0) / (fcn(x1) - fcn(x0))

        if abs(xnew - x1) < xtol:
            return xnew

        x0, x1 = x1, xnew
        iter_count += 1

    return x1

def main():
    # Test cases
    root1 = Secant(lambda x: x - 3 * math.cos(x), 1, 2, maxiter=5, xtol=1e-4)
    root2 = Secant(lambda x: math.cos(2 * x) * x ** 3, 1, 2, maxiter=15, xtol=1e-8)
    root3 = Secant(lambda x: math.cos(2 * x) * x ** 3, 1, 2, maxiter=3, xtol=1e-8)

    print(f'Root of x-3cos(x)=0: {root1:.5f}')
    print(f'Root of cos(2x)*x^3=0: {root2:.5f}')
    print(f'Root of cos(2x)*x^3=0 (limited iterations): {root3:.5f}')

if __name__ == "__main__":
    main()
