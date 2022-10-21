# Mean vs. median
# 
# mean is the sum of all the data points divided by the total number of data points, and the median is the 
# middle value of the dataset where 50% of the data is less than the median, and 50% of the data is greater 
# than the median. 


#Import matplotlib.pyplot with alias plt
import matplotlib.pyplot as plt

# Subset for food_category equals rice
rice_consumption = food_consumption[food_consumption['food_category']=='rice']

# Histogram of co2_emission for rice and show plot
rice_consumption["co2_emission"].hist()
plt.show()


# Calculate mean and median of co2_emission with .agg()
print(rice_consumption['co2_emission'].agg( [np.mean, np.median] ) )