from dataclasses import dataclass


@dataclass
class Student:
    name: str
    score: int


students = [
    Student("James", 45),
    Student("Deborah", 82),
    Student("Amaka", 76),
    Student("Daniel", 90),
    Student("Tunde", 68),
]
