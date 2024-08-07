from functools import partial


def multiply(x, y, z):
    return x * y * z


double = partial(multiply, 2)
print(double(5, 10))  # Output: 10

#functools.partial() is used to create a new function with some of the arguments of the original function fixed.
#The partial() function takes a function and some arguments as input and returns a new function with the arguments fixed.
#The new function can be called with the remaining arguments.
#The new function can be called with the fixed arguments and the remaining arguments.

from functools import lru_cache

@lru_cache(maxsize=9)
def fibonacci(n):
    if n < 2:
        return n
    print("inside fn")
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))
print(fibonacci.cache_info())

#functools.lru_cache() is used to cache the results of a function.
#The lru_cache() function takes the maximum size of the cache as input.
#The lru_cache() function returns a decorator that can be applied to a function.
#The decorator caches the results of the function.
#The decorator uses a least-recently-used (LRU) cache.
#The decorator stores the results of the function in the cache.

from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('Calling decorated function')
        return func(*args, **kwargs)
    return wrapper
@my_decorator
def say_hello():
    """A simple function that says hello"""
    print('Hello')

say_hello()
print(say_hello.__name__)
print(say_hello.__doc__)

#functools.wraps() is used to preserve the metadata of the original function.
#The wraps() function takes the original function as input and returns a decorator.
#The decorator preserves the metadata of the original function.
#The decorator copies the metadata of the original function to the new function.
#The new function can be called with the same metadata as the original function.
#The new function has the same name and docstring as the original function.
#The new function has the same module and signature as the original function.


