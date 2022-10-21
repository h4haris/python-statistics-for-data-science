# Variance and standard deviation
# 
# Variance and standard deviation are two of the most common ways to measure the spread of a variable, 
# 
# Spread is important since it can help inform expectations. 
# 
# For example, if a salesperson sells a mean of 20 products a day, but has a standard deviation of 10 
# products, there will probably be days where they sell 40 products, but also days where they only sell 
# one or two. 
# 
# Information like this is important, especially when making predictions.


# Print variance and sd of co2_emission for each food_category
print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std]))

# Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Create histogram of co2_emission for food_category 'beef'
print(food_consumption[food_consumption['food_category']=='beef'])
print(food_consumption[food_consumption['food_category']=='beef']["co2_emission"])
food_consumption[food_consumption['food_category']=='beef']["co2_emission"].hist()
# Show plot
plt.show()

# Create histogram of co2_emission for food_category 'eggs'
food_consumption[food_consumption['food_category']=='eggs']["co2_emission"].hist()
# Show plot
plt.show()