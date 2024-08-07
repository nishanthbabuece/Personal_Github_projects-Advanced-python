#asynchronous programming
# It is a way of programming that allows a program to run multiple operations concurrently in the background.
# This is a very useful feature as it can dramatically improve the efficiency of a program.

# Process management , virtual memory, file system, network, etc. are some of the examples of asynchronous programming.

#asyncio module
# The asyncio module provides a framework that allows you to perform asynchronous programming in Python.

# this cn be useful when we need to run two task engines in parallel
import asyncio


async def fetch_data():
    print("Start fetching data...")
    await asyncio.sleep(2)
    print("Data fetched")


async def main():
    await asyncio.gather(fetch_data(), fetch_data())


# Run the asyncio event loop
asyncio.run(main())