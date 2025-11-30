no_of_courses = int(input("What number of courses are your offering? "))
credit_unit = []
courses = []
grade = []
grade_value = []
total_gradepoint = 0
total_creditunit = 0


for i in range(no_of_courses):
    courses.append(input("Type the name of the course: "))
    grade.append(input("Type in the grade for the course: "))
    credit_unit.append(int(input("Type the credit uint for the course: ")))
    if grade[i] == "A" or "a":
        grade_value.append(5)
    elif grade[i] == "B" or "b":
        grade_value.append(4) 
    elif grade[i] == "C" or "c":
        grade_value.append(3)
    elif grade[i] == "D" or "d":
        grade_value.append(2)
    elif grade[i] == "E" or "e":
        grade_value.append(1)
    elif grade[i] == "F" or "f":
        grade_value.append(0)

for i, value in enumerate(grade_value):
    total_gradepoint += (value * credit_unit[i])
    total_creditunit += credit_unit[i]

gpa = total_gradepoint / total_creditunit

print("\nThis is your result\n")
for i in range(no_of_courses):
    print(courses[i],    grade[i])

print("Your GPA is: ", gpa)


