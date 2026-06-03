# Encapsulation

## What is Encapsulation?

Encapsulation is the process of bundling data and methods together inside a class while controlling access to that data.

It helps protect an object's internal state from unintended modification.

---

## Why Use Encapsulation?

- Data Security
- Data Validation
- Better Code Organization
- Easier Maintenance

---

## Access Modifiers in Python

### Public

Accessible from anywhere.

```python
class Student:
    def __init__(self):
        self.name = "Kanika"
```

---

### Protected

Convention: single underscore.

```python
self._name
```

Should not be accessed directly outside the class.

---

### Private

Double underscore.

```python
self.__name
```

Cannot be accessed directly from outside.

---

## Getters and Setters

Used to safely access and modify private data.

Getter:
- Reads value

Setter:
- Updates value with validation

---

## Key Takeaways

- Hide implementation details
- Control data access
- Improve security and maintainability
