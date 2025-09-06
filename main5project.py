import scipy.stats as stats

lam = 10  

prob1 = 1 - stats.poisson.cdf(11, lam)
print(f"Probability of 12 or more rainy days: {prob1}")

prob2 = stats.poisson.cdf(18, lam) - stats.poisson.cdf(11, lam)
print(f"Probability of between 12 and 18 rainy days: {prob2}")