# Write a Python script to:
import pandas as pd
from matplotlib import pyplot as plt

# Load the CSV file using pandas.
df = pd.read_csv('sales_data.csv')

# Calculate the total revenue.
total_revenue = df['Revenue ($)'].sum()

# function to parse Quantity column into python
quantity = df['Quantity Sold'].max()

# Find the best-selling product (based on Quantity Sold).
best_product = df.groupby('Product')['Quantity Sold'].sum().idxmax()

# Identify the day with the highest sales.
day_high_sales = df.groupby('Date')['Revenue ($)'].sum().idxmax()

# Save the results to a new file called sales_summary.txt.
with open("sales_summary.txt", "w") as f:
    f.write(f"Total revenue: ${total_revenue:.2f}\n")
    f.write(f"Best-selling product: {best_product} ({quantity} units sold)\n")
    f.write(f"Highest Sales Day: {day_high_sales}")
    f.close()

# Print the insights in a user-friendly format.
with open('sales_summary.txt') as f:
    print (f.read())