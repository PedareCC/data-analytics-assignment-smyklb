import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import os

# tourism csv
df = pd.read_csv('Tourism_cleaned.csv')

# Select the 'Country' and 'Spend Ending March 2019' columns
spend = df[['Country', 'Spend Ending March 2019']]

# Sorting by 'Spend Ending March 2019' from highest to lowest and resetting the index
sorted_spend = spend.sort_values('Spend Ending March 2019', ascending=False).reset_index(drop=True)

# Setting the index to start from 1
sorted_spend.index = sorted_spend.index + 1



# spend24 = df[['Country', 'Spend Ending March 2024']]
# sorted_spend24 = spend.sort_values('Spend Ending March 2024', ascending=False).reset_index(drop=True)
# sorted_spend24.index = sorted_spend24.index + 1


# Display the sorted values
print(sorted_spend[0:5])

# print(sorted_spend24[0:4])





