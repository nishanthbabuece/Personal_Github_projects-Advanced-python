#It acts as a wrapper to the original function. The original function is passed to the decorator as an argument and the decorator returns a new function.
# The new function is a modified version of the original function. The decorator can add some functionality to the original function without modifying it.
# The decorator can also modify the arguments passed to the original function and the return value from the original function.


# Decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure.
# Decorators are usually called before the definition of a function you want to decorate.
# The @ symbol is used to specify a decorator function in Python.
# A decorator is a callable that returns a callable.
# The inner function can access the arguments of the outer function.

# Decorator with no arguments
"""
def my_decorator(func):
    def wrapper():
       print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
my_decorator(10)
"""

"""
def greet_decorator(func):
    def wrapper():
        return f"Greetings! {func()}"

    return wrapper


@greet_decorator
def say_hello():
    return "Hello!"


print(say_hello())  # Output: Greetings! Hello!
"""

# Useful when creating logging systems, authentication, and authorization systems, etc.
# below code is with decorator @logging_decorator
# like adding security log before and after the function is called
def logging_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result

    return wrapper


@logging_decorator
def mul(a, b):
    return a * b
@logging_decorator
def add(a, b):
    return a + b
@logging_decorator
def sub(a, b):
    return a - b
@logging_decorator
def div(a, b):
    return a / b



print(mul(5, 3))  # Output:
# Calling function: add
# Function add returned 15
# 15
print(add(5, 3))  # Output:
# Calling function: add
# Function add returned 8
# 8
print(sub(5, 3))  # Output:
# Calling function: sub
# Function sub returned 2
# 2
print(div(5, 3))  # Output:
# Calling function: div
# Function div returned 1.6666666666666667
# 1.6666666666666667


