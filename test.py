import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import os

# tourism csv
df = pd.read_csv('Tourism_cleaned.csv')

# Select the 'Country' and 'Spend Ending March 2019' columns
trip = df[['Country', 'Trips Ending March 2019']]

# Sorting by 'Spend Ending March 2019' from highest to lowest and resetting the index
sorted = trip.sort_values('Trips Ending March 2019', ascending=False).reset_index(drop=True)

# Setting the index to start from 1
sorted.index = sorted.index + 1




trip24 = df[['Country', 'Trips Ending March 2024']]

sorted24 = trip24.sort_values('Trips Ending March 2024', ascending=False).reset_index(drop=True)

sorted24.index = sorted24.index + 1


# Display the sorted values
print(f"The Top 5 Countries most traveled in 2019: \n {sorted[0:5]}\n")
print(f"The Top 5 Countries most traveled in 2024: \n {sorted24[0:5]} \n")







