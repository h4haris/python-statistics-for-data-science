# Probabilities from the normal distribution
# 
# Since each deal Amir worked on (both won and lost) was different, each was worth a different amount of money. These values 
# are stored in the amount column of amir_deals and follow a normal distribution with a mean of 5000 dollars and a standard
# deviation of 2000 dollars. 
# 
# As part of his performance metrics, compute the probability of Amir closing a deal worth various amounts.


# Probability of deal < 7500
prob_less_7500 = norm.cdf(7500, 5000, 2000)

print(prob_less_7500)


# Probability of deal > 1000
prob_over_1000 = 1 - norm.cdf(1000, 5000, 2000)

print(prob_over_1000)


# Probability of deal between 3000 and 7000
prob_3000_to_7000 = norm.cdf(7000, 5000, 2000) - norm.cdf(3000, 5000, 2000)

print(prob_3000_to_7000)


# Calculate amount that 25% of deals will be less than
pct_25 = norm.ppf(0.25, 5000, 2000)

print(pct_25)