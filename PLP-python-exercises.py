# This is a program that requires you to enter two numbers
# And an arithmetic operation e.g addition, subtraction, multplication and division
# To do basic math operations

def sum(a,b):
    return (a+b)

def minus(a,b):
    return(a - b)

def mult(a,b):
    return(a * b)

def div(a,b):
    return(a /b)

print("This is a program that requires you to enter two numbers")
print("And an arithmetic operation e.g addition, subtraction, multplication and division")

a = int(input("Enter the first number"))
b = int(input("Enter the second number"))
c = str(input("Enter the arithmetic operation i.e +, -, * or /"))


match c:
    case ("+"):
        print(f'{a} + {b} = {sum(a,b)}')
    case ("-"):
        print(f'{a} - {b} = {minus(a,b)}')
    case("*"):
        print(f'{a} * {b} = {mult(a,b)}')
    case ("/"):
        print(f'{a} / {b} = {div(a,b)}')

# Task 1:
# Write a program that accepts user input to create a list of integers. 
# Then, compute the sum of all the integers in the list.

myList = []
counter = 0 
while counter<10: 
    num = input("Enter numbers or type q to quit: ")
    if num == 'q': 
        break
    else:
        myList.append(int(num))
    counter +=1

print (sum(myList))

# Task 2
#Create a tuple containing the names of five of your favorite books. 
# Then, use a for loop to print each book name on a separate line.


books = ("If tomorrow comes", "The Dark Half", "Chasing Tomorrow", "Archie Andrews", "Will")

for book in books:
    print(book)

# Task 3
# Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. 
# Ask the user for input and store the information in the dictionary. 
# Then, print the dictionary to the console.

info = {"Name":"",
        "Age":"",
        "Color":""}

info["Name"] = input("What's your name? ")
info["Age"] = int(input("How old are you? "))
info["Color"] = input("What's your favourite color? ")

print ("\ninfo:")
print(info)

# Task 4
# Write a program that accepts user input to create two sets of integers. 
# Then, create a new set that contains only the elements that are common to both sets.

num_set1 = set()
num_set2 = set()

while True:
    num1 = int(input("Enter a number: "))
    num_set1.add(num1)

    choice1 = input("Do you want to enter another number? (Y/n)")

    if choice1.casefold() == 'n':
        print("Alright, let's go to the other set.")
        break

while True:
    num2 = int(input("Enter a number: "))
    num_set2.add(num2)

    choice1 = input("Do you want to enter another number? (Y/n)")

    if choice1.casefold() == 'n':
        print("Alright, let's compare both sets and see what appears in both.")
        break

set1_set2  = num_set1 & num_set2

print(set1_set2)

# Task 5
# Create a program that stores a list of words. 
# Then, use list comprehension to create a new list that contains only the words that have 
# an odd number of characters.

genres_list = ["amapiano", "afrobeats", "afropop", "afrosoul", "rhumba", "lingala", "moohmbaton","EDM", "country", "rock", "pop", "drill", "garage", "alt"]
genres = [genre for genre in genres_list if len(genre) % 2!=0]

print(genres)


# Assignment 2



# Create an empty list called my_list.
my_list = []

# Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position in the list.
my_list.insert(2,15)

# Extend my_list with another list: [50, 60, 70].
another_list =[50,60,70]
my_list.extend(another_list)

# Remove the last element from my_list.
my_list.pop(-1)

# Sort my_list in ascending order.
my_list.sort()
print(my_list)

# Find and print the index of the value 30 in my_list.
print (my_list.index(30))

