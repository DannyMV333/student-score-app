from students import students
from utils.helpers import highest_score, lowest_score


print("Student Scores")

for student in students:
    print(student["name"], "-", student["score"])

print("Highest score:", highest_score(students))
print("Lowest score:", lowest_score(students))
