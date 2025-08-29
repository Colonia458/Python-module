# Activity 1

# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
class Pet:
    def __init__(self, name, animal, gender,):
        self.name = name
        self.animal = animal
        self.gender = gender

    # A method to make the pet speak.
    def speak(self):
        print(f"The {self.animal} makes a sound.")

    # A method to display information about the pet.
    def get_info(self):
        print(f"Animal: {self.animal}, Gender: {self.gender}")


# Add an inheritance layer to explore polymorphism or encapsulation.
class Dog(Pet):
    """A class representing a dog, inheriting from Pet."""
    
    # The constructor for the Dog class.
    def __init__(self, name, breed):
        super().__init__(name=name, animal="Dog")
        self.breed = breed
    
    def fetch_ball(self):
        print(f"{self.name} is fetching the ball!")

# Activity 2: Polymorphism Challenge! 🎭

# Create a program that includes animals or vehicles with the same action (like move()). 
"""
However, make each class define move() differently 
(for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
"""
class Vehicle:
    def __init__(self, type):
        self.type = type

    def move(self):
        print(f"The {self.type} has moved")

class Car(Vehicle):
    def __init__(self, type="Car"):
        super().__init__(type)

    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def __init__(self, type="Plane"):
        super().__init__(type)

    def move(self):
        print("Flying ✈️")

v = Vehicle("Generic Vehicle")
v.move()

c = Car()
c.move()

p = Plane()
p.move()