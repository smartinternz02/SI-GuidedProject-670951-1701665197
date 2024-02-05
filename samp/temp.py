import pandas as pd
#Reading the bodyfat.csv file using pandas and storing it in df.
df1 = pd.read_csv("4_Smart watch prices.csv")
df2 = pd.read_csv("file1.csv")
df1 = df1.rename(columns={
'Display Size (inches)' : 'Display Size',
'Water Resistance (meters)': 'Water Resistance',
'Battery Life (days)' : 'Battery Life',
'Price (USD)' : 'Price'
})
df2 = df2.rename(columns={
'Display Size (inches)' : 'Display Size',
'Water Resistance (meters)': 'Water Resistance',
'Battery Life (days)' : 'Battery Life',
'Price (USD)' : 'Price'
})
print(df1['Resolution'].unique())
print(df2['Resolution'].unique())
