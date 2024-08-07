#metadata is data about data
#A Metaclass is a class of a class that defines how a class behaves.


class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name}")
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMeta):
    def dosomething(self):
        print("Doing something 1")
    pass
instanc=MyClass()
print(instanc.dosomething())
# Output: Creating class MyClass
#The metaclass is defined by the metaclass argument in the class definition.
#The metaclass is responsible for creating the class.
#The metaclass is responsible for initializing the class.
#The metaclass is responsible for configuring the class.
#The metaclass is responsible for defining the behavior of the class.
#The metaclass is responsible for defining the attributes of the class.
#The metaclass is responsible for defining the methods of the class.
#The metaclass is responsible for defining the properties of the class.

