#multi-threading

import threading
import time

def myfunction(i):
    print ("function called by thread %i\n"  % i)
    time.sleep(2)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=myfunction, args=(i,))
    threads.append(t)
    t.start()
    t.join()

for t in threads:
    t.join()
print ("Main thread done\n")
# In this example, we create a function called myfunction that takes an argument i.
# We then create a list called threads to store the threads.
# We create a for loop that creates 5 threads and appends them to the threads list.
# We then start each thread using the start() method.


#second example
print("second example for multi-threading")
import threading
import time


def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)


def print_letters():
    for letter in 'abcde':
        print(letter)
        time.sleep(1)


# Create threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start threads
thread1.start()
thread2.start()

# Wait for threads to complete
thread1.join()
thread2.join()

"""
second example for multi-threading
0
a
1
b
c2

d
3
e4

"""