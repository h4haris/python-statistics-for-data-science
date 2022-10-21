# The CLT in action
# 
# The central limit theorem states that a sampling distribution of a sample statistic approaches the normal distribution as you 
# take more samples, no matter the original distribution being sampled from.
# 
# Focus on the sample mean and see the central limit theorem in action while examining the num_users column of amir_deals more 
# closely, which contains the number of people who intend to use the product Amir is selling.


# Create a histogram of num_users and show
amir_deals['num_users'].hist()
plt.show()


# Set seed to 104
np.random.seed(104)

# Sample 20 num_users with replacement from amir_deals
samp_20 = amir_deals['num_users'].sample(20, replace = True)
print(samp_20)

# Take mean of samp_20
print(np.mean(samp_20))


sample_means = []
# Loop 100 times
for i in range(100):
  # Take sample of 20 num_users
  samp_20 = amir_deals['num_users'].sample(20, replace=True)
  # Calculate mean of samp_20
  samp_20_mean = np.mean(samp_20)
  # Append samp_20_mean to sample_means
  sample_means.append(samp_20_mean)
  
print(sample_means)


# Convert to Series and plot histogram
sample_means_series = pd.Series(sample_means)
sample_means_series.hist()
# Show plot
plt.show()