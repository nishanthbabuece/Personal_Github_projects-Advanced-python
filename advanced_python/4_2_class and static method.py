#class method and static method
# class method and static method are used for defining the methods in a class.


class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32


#@fahrenheit.setter
#def fahrenheit(self, value):
#    self._celsius = (value - 32) * 5 / 9


# Usage
temp = Temperature(10)
print(temp.fahrenheit)  # Output: 32.0
#temp.fahrenheit = 212
print(temp._celsius)  # Output: 100.0

# multiple inheritance

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

#mixins
# Mixins are classes that provide methods to other classes.
# Mixins are used to add functionality to classes.

class Logmixin():
    def log(self, message):
        print(message)

class Connection():
    def connect(self):
        print("Connected")

class Database(Connection, Logmixin):
    def select(self):
        print("Select query")

# Usage
db = Database()
db.connect()  # Output: Connected
db.log("Log message")  # Output: Log message
db.select()  # Output: Select query


#Magic methods
# Magic methods are special methods that start and end with double underscores.
# Magic methods are used to perform various operations in Python.
# Magic methods are also known as dunder methods.
# Magic methods are automatically invoked when certain operations are performed on objects.

#Description	Magic Method
#Initialization	__init__(self, ...)
#String representation	__str__(self)
#Length	__len__(self)
#Comparison	__eq__(self, other), __lt__(self, other), __gt__(self, other)
#Arithmetic	__add__(self, other), __sub__(self, other), __mul__(self, other)
#Indexing	__getitem__(self, key), __setitem__(self, key, value)
#Function calling	__call__(self, ...)
#Context management	__enter__(self), __exit__(self, ...)
#Attribute access	__getattr__(self, name), __setattr__(self, name, value)
#Iteration	__iter__(self), __next__(self)
#Conversion	__int__(self), __float__(self), __bool__(self)
#Copying	__copy__(self), __deepcopy__(self, memo)
#Pickling	__getstate__(self), __setstate__(self, state)
print('Magic methods Example - descriptor')
class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value
# we can keep all private variable in the description function so all users dont have access to it.
# we can also keep the validation in the description function
# we can also keep the default value in the description function

class MyClass:
    attr = Descriptor('attr')

    def __init__(self, attr):
        self.attr = attr


# Usage
obj = MyClass(10)
print(obj.attr)  # Output: 10
obj.attr = 20
print(obj.attr)  # Output: 20

#dynamic attributes
# Dynamic attributes are attributes that are created at runtime.