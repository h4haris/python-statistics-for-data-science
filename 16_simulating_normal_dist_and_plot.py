# Simulating sales under new market conditions
# 
# The company's financial analyst is predicting that next quarter, the worth of each sale will increase by 20% and the 
# volatility, or standard deviation, of each sale's worth will increase by 30%. 
# 
# To see what Amir's sales might look like next quarter under these new market conditions, simulate new sales amounts 
# using the normal distribution and store these in the new_sales DataFrame, which has already been created.


# Calculate new average amount
new_mean = 5000 + (5000 * 0.2)

# Calculate new standard deviation
new_sd = 2000 + (2000 * 0.3)

# Simulate 36 new sales
new_sales = norm.rvs(new_mean, new_sd, size=36)
print(new_sales
)
# Create histogram and show
plt.hist(new_sales)
plt.show()