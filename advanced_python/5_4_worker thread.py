#if you need team workers then we call it as worker thread.
#pooling of threads is called worker thread.
#worker thread is a thread that is used to perform background tasks in a program.
#worker threads are used to perform tasks that are not critical to the main program.

# Thread pool manages a pool of worker threads that can be used to perform tasks in parallel.

from concurrent.futures import ThreadPoolExecutor
import time

def task(message):
    time.sleep(2)
    return message

# Create a ThreadPoolExecutor with 3 worker threads
executor = ThreadPoolExecutor(max_workers=3)

# Submit a task to the executor
future = executor.submit(task, ("hello"))

# Wait for the task to complete
result = future.result()
print(result)

# Shutdown the executor

executor.shutdown()

# In this example, we create a function called task that takes a message as an argument.
# We then create a ThreadPoolExecutor with 3 worker threads.
# We submit a task to the executor using the submit() method.
# We wait for the task to complete using the result() method.
# We then shutdown the executor using the shutdown() method.
# The ThreadPoolExecutor class provides a simple way to create a pool of worker threads that can be used to perform tasks in parallel.

# real-life example -- web server that handles multiple requests concurrently - we can mention that
# from one Ip i can take only these many sessions

# Thread Pool executions
print("Thread Pool executions-example")
from concurrent.futures import ThreadPoolExecutor
import time


def task(name):
    print(f"Starting task {name}")
    time.sleep(2)
    print(f"Task {name} completed")


# Create a ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=2) as executor:
    futures = [executor.submit(task, i) for i in range(5)]

    for future in futures:
        future.result()