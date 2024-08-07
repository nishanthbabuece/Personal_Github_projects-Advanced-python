#magic methods mixins composition
class MyList:
    def __init__(self):
        self.items = {}

    def __getitem__(self, key):
        return self.items[key]

    def __setitem__(self, key, value):
        self.items[key] = value

    def __delitem__(self, key):
        if key == 'id':
            raise Exception("Cannot delete id")
        del self.items[key]


my_list = MyList()
my_list['a'] = 1
my_list['b'] = 2
my_list['id'] = 100
print(my_list['a'])  # Output: 1
del my_list['a']
print(my_list.items)  # Output: {'b': 2, 'id': 100}
#del my_list['id']  # Output: Exception: Cannot delete id
# it is like a json dictionary difference is that it is a class



# Composition
# Composition is a concept in Python that allows you to reuse code.

class Engine:
    def __init__(self, capacity):
        self.capacity = capacity

    def start(self):
        print("Engine started")

class Wheels:
    def __init__(self, number):
        self.number = number

    def rotate(self):
        print("Wheels rotating")

class Car:
    def __init__(self):
        self.engine = Engine(2000)
        self.wheels = Wheels(4)

    def drive(self):
        self.engine.start()
        self.wheels.rotate()
        print("Driving")

# Usage
car = Car()
car.drive()  # Output: Engine started, Wheels rotating, Driving
# In this example, the Car class is composed
# of the Engine and Wheels classes. The Car class
# reuses the code from the Engine and Wheels classes
# by creating instances of these classes in its __init__ method.



