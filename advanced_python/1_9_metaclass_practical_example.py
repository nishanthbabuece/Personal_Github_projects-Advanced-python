#practical use case
# It can be used to enforce coding standards. - while creating a class, we can enforce that the class should have a specific method or attribute.
# While writing a framework, we can enforce that the classes should have specific methods or attributes.
# It can be used to create a singleton class. - A singleton class is a class that can have only one instance.
# It can be used to create a factory class. - A factory class is a class that creates objects of other classes.

#for example the method name enforcer can be used to enforce that all methods in a class should start with the word "do".
#The metaclass can be used to enforce this rule.

class MethodNameEnforcer(type):
    def __new__(cls, name, bases, dct):
        for attr_name in dct:
            if callable(dct[attr_name]) and not attr_name.startswith('method_'):
                raise ValueError(f"Method {attr_name} does not start with 'method_'")
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MethodNameEnforcer):
    def method_valid(self):
        pass

    # Uncommenting the following method will raise an error
    # def invalid_method(self):
    #     pass
# this can be used in doing "backward compatibility" checks in the codebase.
# Automatic Registration and attribute validation
