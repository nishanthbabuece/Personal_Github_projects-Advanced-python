#Inheritance and polymorphism in python
# Inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly
# the existing class is a base class (or parent class).

#single inheritance
class Mammal:
    def feed_milk(self):
        print("Mammal feeds milk")


class Bird:
    def lay_eggs(self):
        print("Bird lays eggs")


class Platypus(Mammal, Bird):
    pass


# Usage
platypus = Platypus()
platypus.feed_milk()  # Output: Mammal feeds milk
platypus.lay_eggs()  # Output: Bird lays eggs


#polymorphism
#Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
#Suppose, we need to color a shape, there are multiple shapes (rectangle, square, circle). However we could use the same method to color any shape. This concept is called Polymorphism.
print('Polymorphism Example')
class Dog:
    def speak(self):
        print("Dog barks")

class Cat:
    def speak(self):
        print("Cat meows")

def speak(animal):
    animal.speak()

# Usage
dog = Dog()
cat = Cat()
speak(dog)  # Output: Dog barks
speak(cat)  # Output: Cat meows

#polymorphism with functions
print('Polymorphism with functions Example')
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Usage
print(add(5, 3))  # Output: 8
print(subtract(5, 3))  # Output: 2
print(multiply(5, 3))  # Output: 15
print(divide(5, 3))  # Output: 1.666
