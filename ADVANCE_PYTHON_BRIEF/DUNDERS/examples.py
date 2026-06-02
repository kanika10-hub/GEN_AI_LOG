

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student: {self.name}"

s = Student("Kanika")
print(s)

# __add__

class Vector:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Vector(self.x + other.x)

    def __str__(self):
        return str(self.x)

v1 = Vector(10)
v2 = Vector(20)

print(v1 + v2)


similarly we use different dunder methods for different purpose 
