#promote code reuse and readability
# when a button is clicked it will call the function
# A high order function can take another function as an argument
# A high order function can return another function

#function as Return value
#make adder
 def make_adder(n):
     def adder(x):
         return x + n
            return adder
add_10 = make_adder(10)
print(add_10(5))  # Output: 15
add_20 = make_adder(20)
print(add_20(5))  # Output: 25
#The make_adder function returns the adder function.
#The adder function adds the argument n to the argument x.
#The adder function is called with the argument x.
#method is created multiple times with different values of n
# this is what we call as closure

# common higher order functions are map, filter, reduce
# custom higher order function are apply, call, bind, curry, partial, compose, pipe, etc
# map, filter, reduce are used to process the data in a list
# Composing function   f(g(x))  is a higher order function
# Partial applications and currying - functools.partial, functools.partialmethod, functools.partial, functools.partialmethod
# practical applications, sorting, filtering, and mapping data

students = [
    {'name': 'Alice', 'grade': 'A'},
    {'name': 'Bob', 'grade': 'B'},
    {'name': 'Charlie', 'grade': 'C'}
]

sorted_students = sorted(students, key=lambda student: student['grade'])
print(sorted_students)
