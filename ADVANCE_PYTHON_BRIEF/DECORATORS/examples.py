# Example 1: Basic Decorator

def logger(func):

    def wrapper():

        print("Function Started")

        func()

        print("Function Ended")

    return wrapper


@logger
def greet():
    print("Hello")


greet()

# Example 2: Decorator with Arguments

def logger(func):

    def wrapper(*args, **kwargs):

        print("Calling Function")

        result = func(*args, **kwargs)

        return result

    return wrapper


@logger
def add(a, b):
    return a + b


print(add(10, 20))

# Example 3: Timer Decorator

import time

def timer(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Execution Time:", end - start)

        return result

    return wrapper


@timer
def process():

    time.sleep(2)


process()
