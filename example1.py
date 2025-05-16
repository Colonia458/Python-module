import pandas as pd

df = pd.read_csv('example.csv')

df['Age']  # Selects the Age column
df[df['Age'] > 30]  # Returns rows where Age > 30

df['Country'] = ['USA', 'USA', 'USA']  # Adds a new column

# Get rows where Age is greater than 30
# df_filtered = df[df['Age'] > 30]

# Get rows where Age is greater than 30 and City is 'New York'
df_filtered = df[(df['Age'] > 30) & (df['City'] == 'New York')]


# Sort by Age in descending order
df_sorted = df.sort_values(by='Age', ascending=False)  
# df_sorted = df.sort_values(by=['Age', 'City'], ascending=[True, False])

grouped = df.groupby('City').agg({'Age': 'mean', 'Name': 'count'})

df['Age'].mean()  # Mean of 'Age' column
df['Age'].sum()   # Sum of 'Age' column
df['Age'].max()   # Maximum of 'Age' column



print(df)
print(df_filtered)
print(df_sorted)
print(grouped)
