# Does sugar improve happiness?
# 
# A new column has been added to world_happiness called grams_sugar_per_day, which contains the average 
# amount of sugar eaten per person per day in each country. 
# 
# Examine the effect of a country's average sugar consumption on its happiness score.
# 
# world_happiness is loaded.


# Scatterplot of grams_sugar_per_day and happiness_score
sns.scatterplot(x="grams_sugar_per_day", y="happiness_score", data=world_happiness)
plt.show()

# Correlation between grams_sugar_per_day and happiness_score
cor = world_happiness["grams_sugar_per_day"].corr(world_happiness["happiness_score"])
print(cor)