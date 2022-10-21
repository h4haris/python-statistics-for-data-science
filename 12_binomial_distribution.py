# Calculating binomial probabilities
# 
# Assume that Amir wins 30% of deals. He wants to get an idea of how likely he is to close a certain number of deals each week. 
# Compute what the chances are of him closing different numbers of deals using the binomial distribution.


# Probability of closing 3 out of 3 deals
prob_3 = binom.pmf(3, 3, 0.3)

print(prob_3)


# Probability of closing <= 1 deal out of 3 deals
prob_less_than_or_equal_1 = binom.cdf(1, 3, 0.3)

print(prob_less_than_or_equal_1)


# Probability of closing > 1 deal out of 3 deals
prob_greater_than_1 = 1 - binom.cdf(1, 3, 0.3)

print(prob_greater_than_1)