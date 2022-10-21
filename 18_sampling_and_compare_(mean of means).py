# The mean of means
# 
# You want to know what the average number of users (num_users) is per deal, but you want to know this number for the entire 
# company so that you can see if Amir's deals have more or fewer users than the company's average deal. 
# 
# The problem is that over the past year, the company has worked on more than ten thousand deals, so it's not realistic to 
# compile all the data. Instead, you'll estimate the mean by taking several random samples of deals, since this is much easier 
# than collecting data from everyone in the company.
# 
# amir_deals is available and the user data for all the company's deals is available in all_deals.


# Set seed to 321
np.random.seed(321)

sample_means = []
# Loop 30 times to take 30 means
for i in range(30):
  # Take sample of size 20 from num_users col of all_deals with replacement
  cur_sample = all_deals['num_users'].sample(20, replace=True)
  # Take mean of cur_sample
  cur_mean = np.mean(cur_sample)
  # Append cur_mean to sample_means
  sample_means.append(cur_mean)

# Print mean of sample_means
print(np.mean(sample_means))

# Print mean of num_users in amir_deals
print(np.mean(amir_deals['num_users']))