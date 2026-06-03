##STUDENT MANAGEMENT SYSTEM

from typing import Optional

class Student:

    def __init__(
        self,
        name: str,
        age: int
    ):
        self.name = name
        self.age = age

    def display(self) -> str:
        return f"{self.name} ({self.age})"


def find_student(
    students: list[Student],
    name: str
) -> Optional[Student]:

    for student in students:

        if student.name == name:
            return student

    return None


students = [
    Student("Kanika", 20),
    Student("Rahul", 21)
]

result = find_student(
    students,
    "Kanika"
)

print(result.display())
