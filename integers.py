# Given two integer numbers, 
# write a Python program to return their product 
# only if the product is equal to or lower than 
# 1000. Otherwise, return their sum.

num1= int(input("Enter the first number: "))
num2= int(input("Enter the second number: "))

if (num1 * num2) <= 1000:
    print(f"The result is {num1 * num2}")
else:
    print(f"The result is {num1 + num2}")


# Exercise 2: Print the Sum of a 
# Current Number and a Previous number

# Write Python code to iterate 
# through the first 10 numbers and, 
# in each iteration, 
# print the sum of the current and previous 
# number.

# # My solution
print(f"Printing current and previous number sum in a range (10)")
prevnum = 0 

while prevnum<=10:
    nextnum = prevnum + 1
    f = prevnum + nextnum
    
    print(f"Current Number {nextnum} Previous Number {prevnum} Sum: {f}")
    prevnum += 1

# # Expected solution:

# print("Printing current and previous number and their sum in a range(10)")
# previous_num = 0

# # loop from 1 to 10
# for i in range(1, 11):
#     x_sum = previous_num + i
#     print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
#     # modify previous number
#     # set it to the current number
#     previous_num = i

# Exercise 3: Print characters present 
# at an even index number
# Write a Python code to accept a string 
# from the user and display characters present 
# at an even index number.

# For example, str = "PYnative". 
# so your code should display ‘P’, ‘n’, ‘t’, ‘v’.

text = input("Type a word: ")
l = len(text)


for i in range(l):
    if i % 2 == 0:
        print(text[i])


# Write a Python code to 
# remove characters from a string 
# from 0 to n and return a new string.

word = input("Type a word: ")
n = int(input("Type the number of characters you want removed: "))

def remove_chars(word, n):  
   return word[n:]

new_word = remove_chars(word,n)
print(new_word)

# Exercise 5: 
# Check if the first and last numbers of a list 
# are the same
# Write a code to return True if 
# the list’s first and last numbers are the same.
# If the numbers are different, return False.

numbers_x = [10, 20, 30, 40, 10]
# output True

numbers_y = [75, 65, 35, 75, 30]
# Output False

def last_firstx():
    if numbers_x[0] == numbers_x[-1]:
        print("True")
    else:
        print("False")

def last_firsty():
    if numbers_y[0] == numbers_y[-1]:
        print("True")
    else:
        print("False")

last_firstx()
last_firsty()

# Exercise 6: Display numbers divisible by 5
# Write a Python code to display numbers 
# from a list divisible by 5

num = int(input("Enter a number: "))
divlist = []
divlist.append(num)

# while num <=50:
#     div5 = int(divlist) % 5
#     if num % 5 == 0:
#         print(f"Given list is {divlist}")
#         print("Divisible by 5")
#         print(div5)
#     else:
#         print("None of the numbers you typed are divisible by 5")

# Corrected code (ChatGPT)
while True:
    num = int(input("Enter a number between 0 and 50: "))
    if num > 50:
        break
    divlist.append(num)


print(f"\nGiven list is {divlist}")
print("Numbers divisible by 5:")

found = False
for d in divlist:
    if d % 5 == 0:
        print(d)
        found = True

if not found:
    print("None of the numbers are divisible by 5.")

# Exercise 7: Find the number of occurrences 
# of a substring in a string
# Write a Python code to find how often the 
# substring “Emma” appears in the given string.

# Given:
str_x = "Emma is good developer. Emma is a writer"
print(str_x.count("Emma"))

# Exercise 8: Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

for i in range(1,6):
    for j in range(i):
        print(i, end=" ")
    print("\n")



# Exercise 9: Check Palindrome Number
# Write a Python code to check if 
# the given number is a palindrome. 
# A palindrome number reads the same 
# forwards and backward. For example, 545 is a palindrome number.

# Expected Output:

# original number 121
# # Yes. given number is palindrome number

# # original number 125
# # No. given number is not palindrome number

pal = int(input("Enter a number: "))
palnum = str(pal)

palnumrev = palnum[::-1]

if palnum == palnumrev:
    print(f"original number {palnum}")
    print("Yes. given number is palindrome number")
else:
    print(f"original number {palnum}")
    print("No. given number is not palindrome number")


# Exercise 10: 
# Merge two lists using the following condition
# Given two lists of numbers, 
# write Python code to create a new list 
# containing odd numbers from the first list 
# and even numbers from the second list.

# Given:
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# Expected Output:
# result list: [25, 35, 40, 60, 90]

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

odd = [num for num in list1 if num % 2 != 0]
even = [num for num in list2 if num % 2 == 0]

result_list = odd + even
print(f"result list: {result_list}")

