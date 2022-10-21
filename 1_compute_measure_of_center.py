# Mean and median
#
# Dataset -  2018 Food Carbon Footprint Index from nu3. 
# 
# The food_consumption dataset contains information about the kilograms of food consumed per person per year in each
# country in each food category (consumption) as well as information about the carbon footprint of that food
# category (co2_emissions) measured in kilograms of carbon dioxide, or CO2, per person per year in each country.
# 
# Compute measures of center to compare food consumption in the US and Belgium.


# Import numpy with alias np
import numpy as np

# Filter for Belgium
be_consumption = food_consumption[food_consumption['country']=='Belgium']

# Filter for USA
usa_consumption = food_consumption[food_consumption['country']=='USA']

# Calculate mean and median consumption in Belgium
print(be_consumption[ "consumption" ].mean())
print(be_consumption[ "consumption" ].median())

# Calculate mean and median consumption in USA
print(usa_consumption[ "consumption" ].mean())
print(usa_consumption[ "consumption" ].median())




# Import numpy as np
import numpy as np

# Subset for Belgium and USA only
be_and_usa = food_consumption[(food_consumption['country']=='Belgium') | (food_consumption['country']=='USA')]

# Group by country, select consumption column, and compute mean and median
print(be_and_usa.groupby("country")['consumption'].agg([np.mean, np.median]))