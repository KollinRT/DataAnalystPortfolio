# Import required packages
import pandas as pd
import os

# load data
df = pd.read_csv("./Weekly_Provisional_Counts_of_Deaths_by_State_and_Select_Causes__2020-2023.csv")

os.chdir('./static')

# convert 'Week Ending Date' column to datetime type
df['Week Ending Date'] = pd.to_datetime(df['Week Ending Date'])

# set the 'Week Ending Date' column as the index
df.set_index('Week Ending Date', inplace=True)

# group the data by state and resample by month
df_monthly = df.groupby('Jurisdiction of Occurrence').resample('M').sum()

# reset the index to make 'Jurisdiction of Occurrence' and 'Week Ending Date' columns
df_monthly = df_monthly.reset_index()


state_month_combinations = df_monthly[['Jurisdiction of Occurrence', 'Week Ending Date']].drop_duplicates()

# Get StateData files generated for chloropleth
for state, month in state_month_combinations.itertuples(index=False):
    # Select data for the current state and month
    subset = df_monthly[(df_monthly['Jurisdiction of Occurrence'] == state)]
    subset = subset[['Jurisdiction of Occurrence', 'COVID-19 (U071, Underlying Cause of Death)', 'Week Ending Date']]
    subset = subset.rename(columns={"Jurisdiction of Occurrence": "state", "COVID-19 (U071, Underlying Cause of Death)": "value", "Week Ending Date":"Month"})
    subset = subset.loc[~subset["state"].isin(["New York City", "Puerto Rico"])]
    subset['Month'] = subset['Month'].dt.strftime('%m-%Y')
    subset = subset[['Month', 'value']]
    
# Check if the current state is not Puerto Rico or New York City
    if state not in ["New York City", "Puerto Rico"]:
        # Create file name with spaces
        filename = f"./StateData/{state}_data.csv"
        # Create file and write data to it
        subset.to_csv(filename, index=False)
os.rename("./StateData/United States_data.csv", "./StateData/All_data.csv")

# Get allData files generated for line graphs
for state, month in state_month_combinations.itertuples(index=False):
    # Select data for the current state and month
    subset = df_monthly[(df_monthly['Week Ending Date'].dt.month == month.month) & (df_monthly['Week Ending Date'].dt.year == month.year)]    
    subset = subset[['Jurisdiction of Occurrence', 'COVID-19 (U071, Underlying Cause of Death)', 'Week Ending Date']]
    subset = subset.rename(columns={"Jurisdiction of Occurrence": "state", "COVID-19 (U071, Underlying Cause of Death)": "value", "Week Ending Date":"Month"})
    subset = subset.loc[~subset["state"].isin(["New York City", "Puerto Rico", "United States"])]
    subset['Month'] = subset['Month'].dt.strftime('%m-%Y')
    subset = subset[['state', 'value']]
    
# Check if the current state is not Puerto Rico or New York City
    if state not in ["New York City", "Puerto Rico", "United States"]:
        # Create file name with spaces
        filename = f"./allData/{month.strftime('%Y-%m')}.csv"
        # Create file and write data to it
        subset.to_csv(filename, index=False)