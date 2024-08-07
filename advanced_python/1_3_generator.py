# this shows all the values within a loop
def generator():
    for i in range(10):
        yield i
g=generator()
print(next(g)) # Output: 0
print(next(g)) # Output: 1
print(next(g)) # Output: 2
print(next(g)) # Output: 3

########################another method belo#####################
def my_generator(start, end):
    current = start
    while current <= end:
        yield current
        current += 1


for value in my_generator(1, 5):
    print(value)  # Output: 1, 2, 3, 4, 5