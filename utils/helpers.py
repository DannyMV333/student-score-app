def highest_score(students):
    return max(student["score"] for student in students)


def lowest_score(students):
    return min(student["score"] for student in students)
