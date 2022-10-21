# Relationships between variables
# 
# Working with a dataset world_happiness containing results from the 2019 World Happiness Report. 
# 
# The report scores various countries based on how happy people in that country are. It also ranks 
# each country on various societal aspects such as social support, freedom, corruption, and others. 
# The dataset also includes the GDP per capita and life expectancy for each country.
# 
# Examine the relationship between a country's life expectancy (life_exp) and happiness score 
# (happiness_score) both visually and quantitatively. 
# 
# dataframe world_happiness is available.


# Create a scatterplot of happiness_score vs. life_exp and show
sns.scatterplot(x="life_exp", y="happiness_score", data=world_happiness)

# Show plot
plt.show()


# Create scatterplot of happiness_score vs life_exp with trendline
sns.lmplot(x="life_exp", y="happiness_score", data=world_happiness, ci=None)

# Show plot
plt.show()


# Correlation between life_exp and happiness_score
cor = world_happiness["life_exp"].corr(world_happiness["happiness_score"])

print(cor)