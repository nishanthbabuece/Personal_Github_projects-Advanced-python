from itertools import count
for i in count(10, 3):
    if i >= 20:
        break
    print(i)

# The count() function returns an iterator that generates numbers starting from a specified number.
# The count() function takes two arguments: start and step.
# The start argument is the starting number.
# The step argument is the step size.
# The count() function generates numbers starting from the start number.

#itertools.cycle() is used to cycle through a sequence.
#The cycle() function takes a sequence as input and returns an iterator.
#The iterator cycles through the sequence indefinitely.
#The cycle() function can be used to repeat a sequence.
from itertools import cycle
counter = 0
for item in cycle('ABCD'):
    if counter > 7:
        break
    print(item)
    counter += 1

#itertools.repeat() is used to repeat a value a specified number of times.
#The repeat() function takes two arguments: value and times.
#The value argument is the value to repeat.
#The times argument is the number of times to repeat the value.
#The repeat() function returns an iterator that generates the value the specified number of times.
print('iter tools - Repeat Example')
from itertools import repeat
for item in repeat('hello', 3):
    print(item)

#itertools.chain() is used to chain multiple iterables together.
#The chain() function takes multiple iterables as input and returns an iterator.
#The iterator chains the iterables together.
#The chain() function can be used to combine multiple iterables into a single iterable.
from itertools import chain
print('iter tools - Chain Example')
for item in chain([1, 2, 3], ['a', 'b', 'c']):
    print(item)

#itertools islice() is used to slice an iterable.
#The islice() function takes three arguments: iterable, start, and stop.
#The iterable argument is the iterable to slice.
#The start argument is the starting index.
#The stop argument is the stopping index.
#The islice() function returns an iterator that generates the sliced elements.
from itertools import islice
print('iter tools - islice Example')
for item in islice(range(10), 2, 8):
    print(item)

#itertools combinations() is used to generate all possible combinations of a sequence.
#The combinations() function takes two arguments: iterable and r.
#The iterable argument is the sequence to generate combinations from.
#The r argument is the length of the combinations.
#The combinations() function returns an iterator that generates all possible combinations of the sequence.
from itertools import combinations
print('iter tools - combinations Example')
for item in combinations('ABCD', 2):
    print(item)
    