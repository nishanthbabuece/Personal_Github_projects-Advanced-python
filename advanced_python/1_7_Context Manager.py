#Connect to a resource, use the resource, and then close the resource.
#This is a common operation. For example, when you open a file, you need to close it after you finish using it.
#This is where context managers come in.
#Context managers are objects that allocate and release resources precisely when you want to.
#The most widely used way of creating a context manager is by using the with statement.
#The with statement simplifies exception handling by encapsulating common preparation and cleanup tasks in so-called context managers.
#The with statement is used to wrap the execution of a block with methods defined by a context manager.
#The context manager handles the entry into, and the exit from, the desired runtime context for the execution of the block of code.
#The context manager returns a resource that will be assigned to the variable in the as part of the with statement.
#The resource is released when the block of code is exited, whether it was exited normally or by an exception.
#The context manager handles the cleanup of the resource.
#The context manager is responsible for defining the runtime context that is established when executing the with statement.

#The context manager protocol consists of two methods:
# __enter__(): This method is called before entering the with block.
# __exit__(): This method is called after exiting the with block.
#The __exit__() method is called even if an exception is raised in the with block.
#The __exit__() method has three arguments: exc_type, exc_value, and traceback.
#These arguments are used to handle exceptions.
#The __exit__() method can return True or False. If it returns True, the exception is suppressed.
#If it returns False, the exception is raised.
#The context manager can also be created using the contextlib module.
#The contextlib module provides utilities for common tasks involving the with statement.
#The contextlib module provides a decorator and a context manager for managing resources.
#The contextlib module provides the contextmanager() decorator to create a context manager.
#The contextmanager() decorator takes a generator function and returns a context manager.
#The generator function should yield exactly one value.
#The value is bound to the variable in the as part of the with statement.
#The generator function can have any number of yield statements.
#The generator function can also have try...finally blocks.
#The generator function can also have return statements.
#The contextlib module provides the closing() function to create a context manager for closing a resource.
#The closing() function takes an object and returns a context manager.
#The object should have a close() method.
#The close() method is called when the with block is exited.
#The contextlib module provides the redirect_stdout() function to redirect the standard output to a file-like object.
#The redirect_stdout() function takes a file-like object and returns a context manager.
#The standard output is redirected to the file-like object when the with block is entered.
#The standard output is restored when the with block is exited.
#The contextlib module provides the suppress() function to suppress exceptions of a specific type.
#The suppress() function takes an exception type and returns a context manager.
#The context manager suppresses exceptions of the specified type.
#The context manager suppresses exceptions raised by the with block.
#The contextlib module provides the ExitStack class to manage multiple context managers.
#The ExitStack class is a context manager that enters multiple context managers.
#The ExitStack class is used to manage dynamic contexts.
#The ExitStack class is used to manage a dynamic number of context managers.
#The ExitStack class is used to manage a dynamic number of resources.
#The ExitStack class is used to manage a dynamic number of cleanup operations.
#The ExitStack class is used to manage a dynamic number of callbacks.
#The ExitStack class is used to manage a dynamic number of context managers and callbacks.
#The ExitStack class is used to manage a dynamic number of context managers and resources.

from contextlib import contextmanager


@contextmanager
def file_manager(file_name, mode):
    file = open(file_name, mode)
    try:
        yield file
        
    finally:
        file.close()


# Usage
with file_manager('movie.txt', 'r') as f:
    data = f.read()
# File is automatically closed after the with block