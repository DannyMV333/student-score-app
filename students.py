"""Student data module for the student score application.

This module defines the Student dataclass and provides a list of
sample student data for use by the application.
"""

from dataclasses import dataclass
from typing import List


@dataclass
class Student:
    """Represents a student with a name and a numerical score.

    Attributes:
        name: The student's full name.
        score: The student's numerical score (0-100).
    """
    name: str
    score: int


# Sample student dataset for testing and demonstration.
# Each entry contains a student's name and their corresponding score.
students: List[Student] = [
    Student(name="James", score=45),
    Student(name="Deborah", score=82),
    Student(name="Amaka", score=76),
    Student(name="Daniel", score=90),
    Student(name="Tunde", score=68),
]
