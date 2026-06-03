# Decorators in Python

## Definition

A decorator is a function that takes another function as input, adds extra functionality, and returns a new function.

Decorators allow us to modify the behavior of functions without changing their source code.

---

## Why Use Decorators?

Without decorators:

```python
start_timer()
function()
stop_timer()
```

would need to be repeated for every function.

Decorators allow us to write the logic once and reuse it everywhere.

---

## Syntax

```python
@decorator
def my_function():
    pass
```

Equivalent to:

```python
my_function = decorator(my_function)
```

---

## How Decorators Work

A decorator:

1. Receives a function
2. Creates a wrapper function
3. Adds extra behavior
4. Returns the wrapper

---

## Components of a Decorator

### Function as Object

Functions can be passed as arguments.

```python
def greet():
    print("Hello")
```

---

### Nested Functions

Functions inside functions.

```python
def outer():

    def inner():
        print("Inner")
```

---

### Closures

Inner functions can remember variables from outer functions.

```python
def outer():

    message = "Hello"

    def inner():
        print(message)

    return inner
```

---

## Benefits

* Code Reusability
* Separation of Concerns
* Logging
* Authentication
* Performance Monitoring
* Caching

---

## Common Built-in Decorators

### @property

```python
@property
def name(self):
    return self._name
```

### @staticmethod

```python
@staticmethod
def add(a, b):
    return a + b
```

### @classmethod

```python
@classmethod
def create(cls):
    return cls()
```

---

## Interview Definition

A decorator is a higher-order function that takes another function, extends its behavior without modifying its code, and returns a new callable object.
