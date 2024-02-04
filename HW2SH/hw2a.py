import math

def Probability(PDF, args, c, GT=True):
    """
    Calculate the probability using Simpson's 1/3 rule.

    Parameters:
    PDF (callable): Gaussian/normal probability density function.
    args (tuple): Tuple containing μ and σ.
    c (float): Upper limit of integration.
    GT (bool): Boolean indicating if we want the probability of x being greater than c (GT=True) or less than c (GT=False).

    Returns:
    float: Probability value.
    """
    mu, sigma = args

    def integrand(x):
        return PDF((x, mu, sigma))

    if GT:
        # Probability of x < c using Simpson's 1/3 rule
        result = simpsons_rule(integrand, mu - 5 * sigma, c)
    else:
        # Probability of x > c using Simpson's 1/3 rule
        result = simpsons_rule(integrand, c, mu + 5 * sigma)

    return result

def simpsons_rule(f, a, b, n=100):
    """
    Approximate the definite integral of a function using Simpson's 1/3 rule.

    Parameters:
    f (callable): Function to be integrated.
    a (float): Lower limit of integration.
    b (float): Upper limit of integration.
    n (int): Number of subintervals.

    Returns:
    float: Approximated integral value.
    """
    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h
        result += 4 * f(x) if i % 2 != 0 else 2 * f(x)

    result *= h / 3
    return result

def main():
    # Test cases
    prob1 = Probability(lambda x: (1 / (x[2] * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x[0] - x[1]) / x[2]) ** 2),
                        (100, 12.5), 105, GT=False)
    prob2 = Probability(lambda x: (1 / (x[2] * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x[0] - x[1]) / x[2]) ** 2),
                        (100, 3), 100 + 2 * 3, GT=True)

    print(f'P(x<105|N(100,12.5))={prob1:.2f}')
    print(f'P(x>μ+2σ|N(100, 3))={prob2:.2f}')

if __name__ == "__main__":
    main()
