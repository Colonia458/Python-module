# Create a class representing anything you like
class Pet:

# Add attributes and methods to bring the class to life!
    def __init__(self, animal, gender):
        self.animal = animal
        self.gender = gender

    def talk(self):
        print(f"{self.animal} speaks")


# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.

class Dog(Pet):
    def bark(self):
        print("This dog barks")

class Cat(Pet):
    def meow(self):
        print("This cat meows")

dog = Dog("Perro", "Male")
cat = Cat("Puss-puss", "Female")

dog.talk()
cat.talk()

# Create a program that includes animals or vehicles with the same action (like move()). 
# However, make each class define move() differently 
# (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).

class Vehicle:
    def __init__(self, type, area):
        self.type = type
        self.area = area    
    
    def move(self):
        print("Moving")

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

car = Car("G-Wagon", "Offroad")
plane = Plane("Chopper", "Air")

car.move()
plane.move()

