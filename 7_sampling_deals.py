# Sampling deals
# 
# Randomly pick five deals so that you can reach out to each customer and ask if they were satisfied with 
# the service they received. You'll try doing this both with and without replacement.
# 
# Additionally, you want to make sure this is done randomly and that it can be reproduced in case you get 
# asked how you chose the deals, so you'll need to set the random seed before sampling from the deals.


# Set random seed
np.random.seed(24)

# Sample 5 deals without replacement
sample_without_replacement = amir_deals.sample(5)
print(sample_without_replacement)

# Sample 5 deals with replacement
sample_with_replacement = amir_deals.sample(5, replace = True)
print(sample_with_replacement)