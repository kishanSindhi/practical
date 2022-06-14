"""
author - Kishan Sindhi
created on - 27/02/22
"""
# importing required lib
import pandas as pd
import numpy as np

# reading the CVS
df = pd.read_csv('attendance.csv')

# renaming the unnamed columns
df.rename(columns={'Unnamed: 0' : 'Name'}, inplace=True)
df.rename(columns={'Unnamed: 5' : 'Duration'}, inplace=True)

# dropping the unwanted columns
df.drop(['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8'], inplace=True, axis=1)

# dropping columns with nan values
df.dropna(inplace=True)

# removing m from the df
df['Duration'] = df['Duration'].str.replace('m', '')

# removing seconds from the df
df['Duration'] = df['Duration'].str[:-4]

# droping empty columns again
df.replace('', np.nan, inplace=True)
df.dropna(inplace=True)

# converting mins to int
df['Duration'] = df['Duration'].apply(pd.to_numeric, errors = 'coerce').fillna(0)

# reseting the index
df.reset_index(inplace=True, drop=True)

# grouping data and converting it to list
details = df.groupby('Name')['Duration'].apply(list)

# creating an empty list so that we can later pass it to out new column 
lis = []

# converting details (series) to data frame
new_df = pd.DataFrame(details, columns=['Duration'])

# creating a for loop so that we can check the condition
for i in new_df['Duration']:  
	if (sum(i)>20):
		lis.append('Present')
	else:
		lis.append('Absent')

# creating a new column
df['Status'] = lis

# exporting the new_df to CVS
new_df.to_csv('Downloads/24_1.csv')
