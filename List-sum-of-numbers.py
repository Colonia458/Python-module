a =  int(input("Enter the 1st number: "))
b =  int(input("Enter the 2nd number: "))
c =  int(input("Enter the 3rd number: "))
x =  int(input("Enter the 4th number: "))
y =  int(input("Enter the 5th number: "))

numbers = [{a},{b}, {c}, {x}, {y}]


total = sum(numbers)
print(f" {a} + {b} + {c} + {x} + {y} = {total}")


myList = []
counter = 0 
while counter<10: #change this to true for infinite (unlimited) loop. also remove counter variables
    num = input("Enter numbers or (q)uit")
    if num == 'q': 
        break
    else:
        myList.append(int(num))
    counter +=1

print (sum(myList))