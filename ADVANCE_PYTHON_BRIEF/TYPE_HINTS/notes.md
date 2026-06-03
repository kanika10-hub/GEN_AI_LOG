# Type Hints

## What are Type Hints?

Type hints allow us to specify the expected data type of variables,
function arguments, and return values.

Example:

```python
def greet(name: str) -> str:
    return f"Hello {name}"
```

---

## Why Use Type Hints?

- Better readability
- Better IDE support
- Easier debugging
- Self-documenting code
- Helps large teams

---

## Basic Syntax

```python
name: str = "Kanika"
age: int = 20
height: float = 5.4
is_student: bool = True
```

---

## Function Type Hints

```python
def add(a: int, b: int) -> int:
    return a + b
```

---

## Common Types

- int
- float
- str
- bool
- list
- tuple
- dict
- set

---

## Benefits

Type hints improve code quality but are NOT enforced by Python at runtime.

They are mainly for developers and tools.
