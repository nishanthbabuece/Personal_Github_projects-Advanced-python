generator = (x * x for x in range(5))
for value in generator:
   print(value)  # Output: 0, 1, 4, 9, 16
# In the above code, we have created a generator using a generator expression.