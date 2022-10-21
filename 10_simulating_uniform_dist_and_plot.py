# Simulating wait times
# 
# To give Amir a better idea of how long he'll have to wait, you'll simulate Amir waiting 1000 times and create a histogram 
# to show him what he should expect. His minimum wait time is 0 minutes and his maximum wait time is 30 minutes.

# Set random seed to 334
np.random.seed(334)

# Import uniform
from scipy.stats import uniform

# Generate 1000 wait times between 0 and 30 mins
wait_times = uniform.rvs(0, 30, size=1000)

print(wait_times)


# Create a histogram of simulated times and show plot
plt.hist(wait_times)
plt.show()