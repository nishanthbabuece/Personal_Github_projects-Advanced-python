#Decorator with Arguments is best used in cases like authorization, authentication, and logging systems.
#only difference is that the decorator function takes arguments.
#The arguments can be used to pass information
#Only authorized users can access the function by passing the role as an argument to the decorator function.
#The role is checked before calling the function.
#If the role is not authorized, a message is displayed.
#The function is called only if the role is authorized.
#The decorator function returns the wrapper function.

#static method and class method
#Static methods are methods that are bound to a class rather than its object.
#They do not require a class instance creation. So, they are not dependent on the state of the object.
#The difference between a static method and a class method is:
#Static method knows nothing about the class and just deals with the parameters.
#Class method works with the class since its parameter is always the class itself.
#They can be called on both the class and its object.
#Static methods are used when we don't want subclasses to change the behavior of a method.
#Class methods are used when we want subclasses to change the behavior of a method.
#Static methods are created by using the @staticmethod decorator.
#Class methods are created by using the @classmethod decorator.

#Application of using decorators in Access Control
def requires_authentication(func):
    def wrapper(user, *args, **kwargs):
        if not user.is_authenticated:
            raise PermissionError("User is not authenticated.")
        return func(user, *args, **kwargs)

    return wrapper


class User:
    def __init__(self, name, authenticated):
        self.name = name
        self.is_authenticated = authenticated


@requires_authentication
def view_dashboard(user):
    return f"Welcome to the dashboard, {user.name}!"


user = User("Alice", True)
print(view_dashboard(user))  # Output: Welcome to the dashboard, Alice!

unauthenticated_user = User("Bob", False)
print(view_dashboard(unauthenticated_user))  # Raises PermissionError