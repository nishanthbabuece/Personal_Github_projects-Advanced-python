import threading
import time
condition = threading.Condition()


def consumer():
    with condition:
        condition.wait()
        print("Consumer notified")


def producer():
    with condition:
        print("Producer notifying")
        condition.notify_all()


# Create threads
consumer_thread = threading.Thread(target=consumer)
producer_thread = threading.Thread(target=producer)

# Start threads
consumer_thread.start()
producer_thread.start()

# Wait for threads to complete
consumer_thread.join()
producer_thread.join()
# Output: Producer notifying, Consumer notified

# In this example, we create a condition object using the threading.Condition() function.
# We then create two functions called consumer and producer that use the condition object to synchronize the threads.
# We create two threads, one for the consumer and one for the producer.
# We start the threads using the start() method.
# We wait for the threads to complete using the join() method.
# The producer thread notifies the consumer thread using the notify_all() method.
# The consumer thread waits for the notification using the wait() method.
# The consumer thread is notified by the producer thread and prints "Consumer notified".
# The producer thread prints "Producer notifying".

"""
# Write a buffer -- producer consumer problem
# A datawarehouse with producer, consumer and datawarehouse class - datawarehouse class is shared one


import threading
import time

class product:
    # member variable product_name
    def __init__(self, product_name):
        self.product_name = product_name
class warehouse:
    # member max_capacity, collection of products - add, fetch
class producer:
    # produce method, creates products and adds to warehouse

class consumer:
    # consume method, fetches products from warehouse and consumes

class factory:
    # create producer, consumer, warehouse
    # start producer, consumer threads
    # wait for producer, consumer threads to
#main method to create and start the factory and stop it after 10 seconds and print the products consumed


"""

import threading
import time
import random

class Product:
    def __init__(self, product_name):
        self.product_name = product_name

class Warehouse:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.products = []
        self.condition = threading.Condition()

    def add_product(self, product):
        with self.condition:
            while len(self.products) >= self.max_capacity:
                self.condition.wait()
            self.products.append(product)
            self.condition.notify_all()

    def fetch_product(self):
        with self.condition:
            while not self.products:
                self.condition.wait()
            product = self.products.pop(0)
            self.condition.notify_all()
            return product

class Producer(threading.Thread):
    def __init__(self, warehouse):
        super().__init__()
        self.warehouse = warehouse

    def run(self):
        for _ in range(10):
            product_name = f"Product-{random.randint(1, 100)}"
            product = Product(product_name)
            self.warehouse.add_product(product)
            print(f"Produced: {product_name}")
            time.sleep(random.uniform(0.1, 0.5))

class Consumer(threading.Thread):
    def __init__(self, warehouse):
        super().__init__()
        self.warehouse = warehouse

    def run(self):
        for _ in range(10):
            product = self.warehouse.fetch_product()
            print(f"Consumed: {product.product_name}")
            time.sleep(random.uniform(0.1, 0.5))

class Factory:
    def __init__(self):
        self.warehouse = Warehouse(max_capacity=5)
        self.producer = Producer(self.warehouse)
        self.consumer = Consumer(self.warehouse)

    def start(self):
        self.producer.start()
        self.consumer.start()

    def stop(self):
        self.producer.join()
        self.consumer.join()

if __name__ == "__main__":
    factory = Factory()
    factory.start()
    time.sleep(10)
    factory.stop()