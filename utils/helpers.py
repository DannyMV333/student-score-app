def highest_score(students):
    if not students:
        return None
    return max(student.score for student in students)


def lowest_score(students):
    if not students:
        return None
    return min(student.score for student in students)
