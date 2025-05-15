# Practice Task (Pandas)
# Create a DataFrame with 3 students: name, age, and grade.
# Add a column called “Passed” where grade > 50 = True.
# Filter and display only students who passed.

import pandas as pd

# Create a DataFrame (table-like structure)
data = {
    'Name': ['Ayra Starr', 'Becky G', 'Metro Boomin'],
    'Age': [23, 30, 34],
    'Score': [85, 40, 95]
}
df = pd.DataFrame(data)

# Filter rows
print("Scores above 50:")
print(df[df['Score'] > 50]) 