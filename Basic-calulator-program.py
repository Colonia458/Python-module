
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