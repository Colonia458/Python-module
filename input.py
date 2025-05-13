file = open("input.txt", "r")
# print(file.read())

# print(file.readline())
# print(file.readline())

# for line in file:
#     print(line)
#     file.close()


# try:
#     file = open("Jimbo.txt")
#     print(file.read())
# except:
#     print("That file doesn't exist")
# finally:
#     file.close()
# file.close()


file = open("input.txt", "a")
file.write("Canio")
file.close()

file = open("input.txt", "r")
print(file.read())
file.close()

user_file = input("Enter the file name: ")