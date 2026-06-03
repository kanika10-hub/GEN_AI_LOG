#variable type hints 
name: str = "Kanika"

age: int = 20

cgpa: float = 8.5

print(name)

#functional argument
def greet(name: str) -> str:
    return f"Hello {name}"


print(greet("Kanika"))

#list type hints
numbers: list[int] = [1, 2, 3, 4]

print(numbers)

#dictionary type hints
student: dict[str, int] = {
    "math": 90,
    "science": 85
}

#optional type hints
from typing import Optional

def get_name() -> Optional[str]:
    return None

#meaning-str | None


#union 
from typing import Union

def process(value: Union[int, str]):
    print(value)


#type alias
type Student = dict[str, str]

student: Student = {
    "name": "Kanika"
}

#generic function
from typing import TypeVar

T = TypeVar("T")

def identity(value: T) -> T:
    return value
