# Quartiles, quantiles, and quintiles
# 
# Quantiles are a great way of summarizing numerical data since they can be used to measure center and spread, 
# as well as to get a sense # of where a data point stands in relation to the rest of the data set. 
#
# For example, you might want to give a discount to the 10% most active users on a website.
# 
# Compute quartiles, quintiles, and deciles, which split up a dataset into 4, 5, and 10 pieces, respectively.


# Calculate the quartiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], [0, 0.25, 0.5, 0.75, 1]))


# Calculate the quintiles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 6)))


# Calculate the deciles of co2_emission
print(np.quantile(food_consumption['co2_emission'], np.linspace(0, 1, 11)))