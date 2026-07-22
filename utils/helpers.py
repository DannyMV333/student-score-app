import statistics


def highest_score(students):
    if not students:
        return None
    return max(student.score for student in students)


def lowest_score(students):
    if not students:
        return None
    return min(student.score for student in students)


def average_score(students):
    if not students:
        return None
    return statistics.mean(student.score for student in students)


def median_score(students):
    if not students:
        return None
    return statistics.median(student.score for student in students)


def pass_count(students):
    return sum(1 for s in students if s.score >= 50)


def fail_count(students):
    return sum(1 for s in students if s.score < 50)
