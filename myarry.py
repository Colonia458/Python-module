# Practice Task (NumPy)
# Create an array with numbers 10 to 50.
# Find the maximum and minimum values.
# Multiply all elements by 3

import numpy as np

my_array = np.array([10,20,30,40,50])

print("Maximum value: ", np.max(my_array))
print("Minimum value: ", np.min(my_array))
 
print("Array * 3 : ", my_array * 3)