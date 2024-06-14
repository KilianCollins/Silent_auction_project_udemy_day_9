
student_scores = {
    "Harry": 81,
    "Ron": 70,
    "Heromine": 100,
    "Draco": 85,
    "Neville": 92,
    "johny test": 45
}

student_grades = {}

for student in student_scores:
    if student_scores[student] < 70:
        student_grades[student] = "Fail"
    elif student_scores[student] >= 70 and student_scores[student] <= 80:
        student_grades[student] = "Acceptable"
    elif student_scores[student] >80 and student_scores[student] <=90:
        student_grades[student] = "Good"
    elif student_scores[student] >90 and student_scores[student] <=100:
        student_grades[student] = "Excellent"


print(student_grades)







