"""Main application script for the student score application.

This script imports student data and helper functions, then displays
a formatted report showing individual scores and summary statistics.
"""

from students import students
from utils.helpers import (highest_score, lowest_score, average_score,
                           median_score, pass_count, fail_count)


def main() -> None:
    """Run the student scores report.

    Prints a formatted table of all students and their scores,
    followed by summary statistics (highest, lowest, average,
    median, pass count, fail count).
    """
    print("=" * 40)
    print("           STUDENT SCORES REPORT")
    print("=" * 40)
    print(f"{'Name':<12} {'Score':<6}")
    print("-" * 40)

    for student in students:
        print(f"{student.name:<12} {student.score:<6}")

    print("-" * 40)
    print(f"{'Highest:':<12} {highest_score(students):<6}")
    print(f"{'Lowest:':<12} {lowest_score(students):<6}")
    print(f"{'Average:':<12} {average_score(students):>6.1f}")
    print(f"{'Median:':<12} {median_score(students):<6}")
    print(f"{'Pass:':<12} {pass_count(students):<6}")
    print(f"{'Fail:':<12} {fail_count(students):<6}")
    print("=" * 40)


if __name__ == "__main__":
    main()
