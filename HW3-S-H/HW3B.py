import scipy.stats

def t_distribution_probability(deg_freedom, z_value):
    t_stat = abs(z_value)
    prob = scipy.stats.t.sf(t_stat, deg_freedom)
    return prob

def main_t_distribution():
    # User input for degrees of freedom and z values
    degrees_of_freedom = int(input("Enter degrees of freedom: "))
    z_values = [float(input(f"Enter z value for test {i+1}: ")) for i in range(3)]

    for z_value in z_values:
        probability = t_distribution_probability(degrees_of_freedom, z_value)
        print(f"P(T > {z_value} | df={degrees_of_freedom}) = {probability:.4f}")

if __name__ == "__main__":
    main_t_distribution()
