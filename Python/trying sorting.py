students = ["May", "Mary", "Jane", "Julie", "Amilia"]

students.sort()
print(students)
students.sort(reverse=True)
print(students)
students.sort(key=lambda x: x.lower())
print(students)

students = ('Alice', 'Bonny', 'Frida', 'Martine')

sake = sorted(students)

for a in sake:
    print(a)

student_grade = [
    ("Alice", "F", 10),
    ("Bonny", "A", 95),
    ("Frida", "B", 80),
    ("Martine", "C", 75),
    ("Amilia", "D", 50)
]

name = lambda name: name[0]
score = lambda score: score[2]
grade = lambda grades:grades[1]

student_grade.sort(key=name, reverse=True)
for names in student_grade:
    print(names[0])

student_grade.sort(key=score)
for scores in student_grade:
    print(scores[2])

student_grade.sort(key=grade)
for grades in student_grade:
    print(grades[1])