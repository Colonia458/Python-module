




# Create a file called input.txt and write at least five lines of text into it.
# with open("input2.txt", "x") as f:
#     f.write("GTA\n")
#     f.write("Sleeping Dogs\n")
#     f.write("Saints Row\n")
#     f.write("Watch Dogs\n")
#     f.write("The Godfather\n")
#     f.write("Scarface: The World is Yours\n")


# Write a Python script to:
# Read the contents of input.txt.
# Count the number of words in the file.
c = 0

with open("input2.txt", "r") as f:
    words = f.read()
    count = words.split()
    c += len(count)
    print(words)
    print(c)


# Convert all text to uppercase.
case = words.upper()

# Write the processed text and the word count to a new file called output.txt.
try:
    with open("output.txt", "w") as f:
        f.write(case)
        f.write(f"\n\nWord Count: {c}")
    print("'output.txt' created successfully.")
except Exception as e:
    print("Failed to create output.txt:", str(e))


# Print a success message once the new file is created.
with open("output.txt", "r") as f:
    print(f.read())


# Create a program that reads a file and writes a modified version to a new file.
# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
user_file = input("Enter the file name: ")

try:
    with open(user_file, "r") as f:
        print("\nFile Found! Contents: \n")
        print(f.read())
except FileNotFoundError:
    print("The file name you wrote doesn't exist")
