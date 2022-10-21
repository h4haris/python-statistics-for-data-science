# What can't correlation measure?
# 
# While the correlation coefficient is a convenient way to quantify the strength of a relationship 
# between two variables, it's far from perfect. 
# 
# Explore one of the caveats of the correlation coefficient by examining the relationship between a 
# country's GDP per capita (gdp_per_cap) and happiness score.
# 
# world_happiness is loaded.


# Scatterplot of gdp_per_cap and life_exp
sns.scatterplot(x="gdp_per_cap", y="life_exp", data=world_happiness)

# Show plot
plt.show()


# Correlation between gdp_per_cap and life_exp
cor = world_happiness["gdp_per_cap"].corr(world_happiness["life_exp"])

print(cor)