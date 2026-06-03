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
