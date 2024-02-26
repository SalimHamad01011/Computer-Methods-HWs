import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Define the normal distribution parameters
mu = 0
sigma = 1
x_values = np.linspace(-3, 3, 1000)

# Calculate P(x < 1 | N(0,1))
prob_x_less_than_1 = stats.norm.cdf(1, mu, sigma)

# Calculate P(x > μ + 2σ | N(175, 3))
mu_2 = 175 + 2 * 3
prob_x_gt_mu_2sigma = 1 - stats.norm.cdf(mu_2, loc=175, scale=3)

# Plot the probability density function and cumulative distribution function
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(x_values, stats.norm.pdf(x_values, mu, sigma), label='PDF')
plt.title('Normal Distribution PDF')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(x_values, stats.norm.cdf(x_values, mu, sigma), label='CDF')
plt.title('Normal Distribution CDF')
plt.xlabel('x')
plt.ylabel('Cumulative Probability')
plt.legend()

plt.tight_layout()
plt.show()

print(f'P(x < 1 | N(0,1)) = {prob_x_less_than_1:.4f}')
print(f'P(x > μ + 2σ | N(175, 3)) = {prob_x_gt_mu_2sigma:.4f}')


#Part A: Using the scipy stats module
#This part utilizes the scipy.stats module to work with normal distributions. It begins by defining parameters for a normal distribution, such as mean (mu) and standard deviation (sigma). The cumulative distribution function (cdf) is then used to calculate the probability that a random variable is less than 1 (P(x < 1 | N(0,1))). Additionally, the cumulative distribution function is applied to find the probability that a random variable is greater than μ + 2σ in a normal distribution with mean 175 and standard deviation 3.

#Formulas and functions used:

#Cumulative Distribution Function (CDF): stats.norm.cdf(x, mu, sigma)
#Probability Density Function (PDF): stats.norm.pdf(x, mu, sigma)
#Parameters: mu, sigma
#Visualization: Matplotlib is used to create a plot of the PDF and CDF.