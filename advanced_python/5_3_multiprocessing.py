

"""

import multiprocessing
import time


def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)


def print_letters():
    for letter in 'abcde':
        print(letter)
        time.sleep(1)


# Create processes
process1 = multiprocessing.Process(target=print_numbers)
time.sleep(5)
process2 = multiprocessing.Process(target=print_letters)

# Start processes
process1.start()
process2.start()

# Wait for processes to complete
process1.join()
process2.join()

# second example for multi-threading
import multiprocessing
import time


def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)


def print_letters():
    for letter in 'abcde':
        print(letter)
        time.sleep(1)


# Create processes
process1 = multiprocessing.Process(target=print_numbers)
process2 = multiprocessing.Process(target=print_letters)

# Start processes
process1.start()
process2.start()

# Wait for processes to complete
process1.join()

# Wait for processes to complete
process2.join()

# In this example, we create two functions called print_numbers and print_letters that print numbers and letters respectively.
# We then create two processes using the Process class from the multiprocessing module.
# We start each process using the start() method.
# We wait for each process to complete using the join() method.
"""

import multiprocessing
import time

def print_numbers():
    for i in range(5):
        for i in range(1,100000):
            pass
        print(i)
        #time.sleep(1)

def print_letters():
    for letter in 'abcde':
        print(letter)
        time.sleep(1)

if __name__ == '__main__':
    # Create processes
    process1 = multiprocessing.Process(target=print_numbers)
    process2 = multiprocessing.Process(target=print_letters)

    # Start processes
    process1.start()
    process2.start()

    # Wait for processes to complete
    process1.join()
    process2.join()

# if thread is in stall state use multiprocessing
# if we need more memory and processing then its better to use multiprocessing
# if we need to share data between processes then its better to use multiprocessing
# if we need to run multiple tasks in parallel then its better to use multiprocessing
