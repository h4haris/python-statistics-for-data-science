# Creating a probability distribution
# 
# A new restaurant opened a few months ago, and the restaurant's management wants to optimize its seating space based on the 
# size of the groups that come most often. 
# 
# On one night, there are 10 groups of people waiting to be seated at the restaurant, but instead of being called in the 
# order they arrived, they will be called randomly. 
# 
# Investigate the probability of groups of different sizes getting picked first. Data on each of the ten groups is contained in 
# the restaurant_groups DataFrame.
# 
# Note that expected value can be calculated by multiplying each possible outcome with its corresponding probability and taking 
# the sum.


# Create a histogram of restaurant_groups and show plot
restaurant_groups['group_size'].hist(bins=np.linspace(2,6,5))
plt.show()


# Create probability distribution
size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]
print(size_dist)

# Reset index and rename columns
size_dist = size_dist.reset_index()
size_dist.columns = ['group_size', 'prob']

print(size_dist)


# Calculate expected value
expected_value = np.sum(size_dist['group_size'] * size_dist['prob'])
print(expected_value)


# Subset groups of size 4 or more
groups_4_or_more = size_dist[size_dist['group_size'] >= 4]
print(groups_4_or_more)

# Sum the probabilities of groups_4_or_more
prob_4_or_more = np.sum(groups_4_or_more['prob'])
print(prob_4_or_more)
