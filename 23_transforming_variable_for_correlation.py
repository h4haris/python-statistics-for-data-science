# Transforming variables
# 
# When variables have skewed distributions, they often require a transformation in order to form a 
# linear relationship with another variable so that correlation can be computed. 
# 
# Perform a transformation.
# 
# world_happiness is loaded.


# Scatterplot of happiness_score vs. gdp_per_cap
sns.scatterplot(x="gdp_per_cap", y="happiness_score", data=world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness["gdp_per_cap"].corr(world_happiness["happiness_score"])
print(cor)


# Create log_gdp_per_cap column
world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])

# Scatterplot of log_gdp_per_cap and happiness_score
sns.scatterplot(x="log_gdp_per_cap", y="happiness_score", data=world_happiness)
plt.show()

# Calculate correlation
cor = world_happiness["log_gdp_per_cap"].corr(world_happiness["happiness_score"])
print(cor)