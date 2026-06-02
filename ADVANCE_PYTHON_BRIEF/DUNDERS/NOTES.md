# Dunder Methods (Magic Methods)

## What are Dunder Methods?

Dunder stands for "Double Underscore".

They are special methods that allow us to customize the behavior of objects.

Examples:

 __init__
__str__
 __repr__
 __len__
 __add__
 __eq__
 __getitem__

## Why Use Them?

They allow custom objects to behave like built-in Python objects.

Example:

```python
len(my_object)
```

calls

```python
my_object.__len__()
```

## Common Dunder Methods



| __init__ | Constructor |
| __str__ | Human-readable representation |
| __repr__ | Developer representation |
| __len__ | Length |
| __add__ | + operator |
| __sub__ | - operator |
| __eq__ | == operator |
| __lt__ | < operator |
| __getitem__ | obj[index] |
| __call__ | obj() |

## Key Takeaways

- Enable operator overloading
- Make custom classes more Pythonic
- Frequently used in frameworks and libraries
