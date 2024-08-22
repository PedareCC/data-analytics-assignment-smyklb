import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import os

# clear terminal
os.system("clear")

# tourism csv
df = pd.read_csv('Tourism_cleaned.csv')

# tourism csv (for china graph function)
dfc= pd.read_csv('Tourism_cleaned.csv')

# reasons for travel csv
dfr= pd.read_csv('Reasons_For_Travel.csv')

def country():

    # input country name
    user_in = input("Input country name: ")
    chosen_country = user_in.title()

    # total for each years
    total_2019 = dfc["Trips Ending March 2019"].sum()

    total_2024 = dfc["Trips Ending March 2024"].sum()

    # print the total number of tourists
    print(f"\nTotal 2019 tourists = {total_2019}\n Total 2024 tourists = {total_2024}\n")


    # Create a bar graph to show total tourists for 2019 and 2024
    years = ['2019', '2024']
    totals = [total_2019, total_2024]


    country_data = dfc[dfc['Country'] == chosen_country]


    trips_2019 = country_data['Trips Ending March 2019'].values[0]
    trips_2024 = country_data['Trips Ending March 2024'].values[0]

    years = ['2019', '2024']
    total = [trips_2019, trips_2024]

    plt.figure(figsize=(8, 6))  
    plt.bar(years, total, color=['blue', 'red'])
    plt.ylim(0, 1380)
    plt.title(f'Total Tourists from {chosen_country} for 2019 and 2024')  
    plt.xlabel('Year')  
    plt.ylabel('Total Tourists') 

    # show the graph
    plt.show()

    plt.savefig(f"{chosen_country}.png")
    print(f"\nNumber of Tourists Graph saved as {chosen_country}.png")


def reasons():
    # Ensure the DataFrame contains 6 rows
    if len(dfr) != 6:
        raise ValueError("DataFrame must have exactly 6 rows to match the number of reasons for travel.")
    
    # Bar width and positions
    bar_width = 0.35
    index = range(len(dfr))

    # Plot: Number of Trips in 2019 vs 2024
    plt.figure(figsize=(12, 8))
    plt.bar(index, dfr['Trips Ending March 2019'], bar_width, label='Trips 2019', color='blue', alpha=0.7)
    plt.bar([i + bar_width for i in index], dfr['Trips Ending March 2024'], bar_width, label='Trips 2024', color='green', alpha=0.7)

    # Labels and title for Trips graph
    plt.xlabel('Reason For Travel')
    plt.ylabel('Number of Trips')
    plt.title('Comparison of Reasons for Travel in 2019 and 2024')
    plt.xticks([i + bar_width/2 for i in index], dfr['Reason For Travel'], rotation=45)
    plt.legend()

    # Show the plot
    plt.tight_layout()
    plt.show()
    
    # Save the plot as an image
    plt.savefig("reasons.png")



def total():
        # Convert columns to numeric types
    df['Trips Ending March 2019'] = pd.to_numeric(df['Trips Ending March 2019'], errors='coerce')
    df['Trips Ending March 2024'] = pd.to_numeric(df['Trips Ending March 2024'], errors='coerce')
    df['Spend Ending March 2019'] = pd.to_numeric(df['Spend Ending March 2019'], errors='coerce')
    df['Spend Ending March 2024'] = pd.to_numeric(df['Spend Ending March 2024'], errors='coerce')

    # Handle NaN values (optional)
    df.fillna(0, inplace=True) # Replaces NaNs with 0s

    # Save the cleaned DataFrame to a new CSV file
    df.to_csv('Tourism_cleaned.csv', index=False)

    # Read the cleaned CSV file into a new DataFrame
    new_df = pd.read_csv('Tourism_cleaned.csv')


    # Calculate the total number of people that traveled in 2019
    total_2019 = new_df['Trips Ending March 2019'].sum()

    # Calculate the total number of people that traveled in 2024
    total_2024 = new_df['Trips Ending March 2024'].sum()

    # Print the totals
    print(f'\nTotal number of travelers in 2019: {total_2019}')
    print(f'Total number of travelers in 2024: {total_2024}\n')

    # Create a bar chart
    plt.figure(figsize=(8, 6))
    plt.bar(['2019', '2024'], [total_2019, total_2024], color=['blue', 'orange'])
    plt.xlabel('Year')
    plt.ylabel('Total Number of Travelers')
    plt.title('Total Number of Travelers in 2019 vs. 2024')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Save the plot as a PNG file
    plt.savefig('total.png')

    # Show the plot
    plt.show()


# mode select loop
print("Mode 1: Choose Country to see Travel \n Mode 2: Reasons for Travel Graph \n Mode 3: Total Travellers")
mode = input("Choose mode: ")
while mode != "exit":
    # choose the country function
    if mode == "1":
        country()
        mode = input("Choose mode: ")

    # choose the reasons for travel function
    elif mode == "2":
        print("Generating Reasons for Travel Graph...")
        time.sleep(1)
        reasons()
        print("Saved as 'reasons.png'")
        mode = input("Choose mode: ")

    # choose total number of travellers function
    elif mode == "3":
        print("Printing Total Travellers graph....")
        time.sleep(1)
        total()
        print("Saved as 'total.png'")
        mode = input("Choose mode: ")

    else:
        print("Not recgonised, try again")
        mode = input("Choose mode: ")

