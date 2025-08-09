# 1. Large Power

# Define the function to accept two input parameters called base and exponent
# Calculate the result of base to the power of exponent
# Use an if statement to test if the result is greater than 5000. 
# If it is then return True. O
# therwise, return False.

# Coding Question
# Create a function named large_power() that takes two parameters named base and exponent.
# If base raised to the exponent is greater than 5000, return True, otherwise return False

base = int(input("ENTER A NUMBER: "))
exponent = int(input("ENTER AN EXPONENTIAL NUMBER (i.e the number to be raised to): "))

def large_power(base, exponent):
    result = base ** exponent
    if result > 5000:
        print(True)
    else:
        print(False)


large_power(base, exponent)




# 2.Divisible By Ten
# Define the function header to accept one input num
# Calculate the remainder of the input divided by 10 (use modulus)
# Use an if statement to check if the remainder was 0. 
# If the remainder was 0, return True, otherwise, return False

# Coding question
# Create a function called divisible_by_ten() that has one parameter named num.
# The function should return True if num is divisible by 10, and False otherwise. 
# Consider using modulo operator % to check for divisibility.
num = int(input("Enter a number: "))

def divisble_by_ten(num):
    
    if num % 10 == 0:
        print(True)
    else:
        print(False)

divisble_by_ten(num)