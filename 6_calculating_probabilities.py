# Calculating probabilities
# 
# You're in charge of the sales team, and it's time for performance reviews, starting with Amir. 
# As part of the review, you want to randomly select a few of the deals that he's worked on over the past 
# year so that you can look at them more deeply. 
# 
# Before you start selecting deals, you'll first figure out what the chances are of selecting certain deals.


# Count the deals for each product
counts = amir_deals["product"].value_counts()
print(counts)


# Calculate probability of picking a deal with each product
probs = counts / amir_deals[ "product" ].count()
print(probs)