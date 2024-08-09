import pandas as pd
import numpy as np

#Read the CSV file into a DataFrame
df= pd.read_csv('Tourism.csv')

# total tourists for each year
total_2019 = df["Trips Ending March 2019"].sum()

total_2024 = df["Trips Ending March 2024"].sum()

# print the total number of tourists
print(f"Total 2019 tourists = {total_2019}\n Total 2024 tourists = {total_2024}\n")

# print data type
print(df.dtypes)
