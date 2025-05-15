# 📌 Task Requirements:
# Import the following libraries:

# pandas (for data manipulation)
# numpy (for numerical operations)
# matplotlib (for data visualization)
# requests (for making web requests)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests


# Complete the following tasks using the libraries:

# Create a NumPy array of numbers from 1 to 10 and calculate the mean.
arraynum = [1,2,3,4,5,6,7,8,9,10]
mean= np.mean(arraynum)
print("The array is:", arraynum)
print("The mean is: " , mean)


# Load a small dataset into a pandas DataFrame and display summary statistics.
data = {
    'Name': ['Ayra Starr', 'Becky G', 'Metro Boomin'],
    'Age': [23, 30, 34],
    'Score': [85, 40, 95]
    }
df = pd.DataFrame(data)
print(df)

print("\nSummary Statistics:")
print(df.describe())

# # Fetch data from a public API using requests and print a key piece of information.
# url = "https://api.coindesk.com/v1/bpi/currentprice.json"
# response = requests.get(url)
# data = response.json()

# price_usd = data["bpi"]["USD"]["rate"]
# print(f"\nCurrent Bitcoin price in USD: ${price_usd}")

# Plot a simple line graph using matplotlib (e.g., a list of numbers).
x = np.linspace(-10, 10, 100)
y = x ** 2

# Plot the graph
plt.plot(x, y, label="y = x^2", color="blue")
plt.title("Simple Line: y = x^2")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.legend()
plt.show()