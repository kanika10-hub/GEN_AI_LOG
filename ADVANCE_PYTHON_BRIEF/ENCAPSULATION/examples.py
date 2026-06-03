#public attribute 

class Student:
    def __init__(self):
        self.name = "Kanika"

s = Student()

print(s.name)

#protected attribute 
class Student:
    def __init__(self):
        self._name = "Kanika"

s = Student()

print(s._name)

#(Accessible, but by convention should be treated as internal.)

#private 
class Student:
    def __init__(self):
        self.__name = "Kanika"

s = Student()

# print(s.__name)
#this causes Attributeerror
