"""Helper functions for student score calculations.

Provides utility functions for computing statistics on a list
of Student objects, including highest, lowest, average, median,
pass count, and fail count.
"""

import statistics
from typing import List, Optional

from students import Student


def highest_score(students: List[Student]) -> Optional[int]:
    """Return the highest score from a list of students.

    Args:
        students: A list of Student objects.

    Returns:
        The maximum score found, or None if the list is empty.
    """
    if not students:
        return None
    return max(student.score for student in students)


def lowest_score(students: List[Student]) -> Optional[int]:
    """Return the lowest score from a list of students.

    Args:
        students: A list of Student objects.

    Returns:
        The minimum score found, or None if the list is empty.
    """
    if not students:
        return None
    return min(student.score for student in students)


def average_score(students: List[Student]) -> Optional[float]:
    """Return the average (mean) score using the statistics module.

    Args:
        students: A list of Student objects.

    Returns:
        The arithmetic mean score, or None if the list is empty.
    """
    if not students:
        return None
    return statistics.mean(student.score for student in students)


def median_score(students: List[Student]) -> Optional[float]:
    """Return the median score using the statistics module.

    Args:
        students: A list of Student objects.

    Returns:
        The median score, or None if the list is empty.
    """
    if not students:
        return None
    return statistics.median(student.score for student in students)


def pass_count(students: List[Student]) -> int:
    """Count the number of students who passed (score >= 50).

    Args:
        students: A list of Student objects.

    Returns:
        The number of students with a score of 50 or higher.
    """
    return sum(1 for s in students if s.score >= 50)


def fail_count(students: List[Student]) -> int:
    """Count the number of students who failed (score < 50).

    Args:
        students: A list of Student objects.

    Returns:
        The number of students with a score below 50.
    """
    return sum(1 for s in students if s.score < 50)
