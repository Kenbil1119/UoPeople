grade_list = []
grade = ''
print("Enter student grade (digits ONLY!) or type 'done' if no more grades to enter")
print("------------------")
while True:
    grade = input("Student grade: ")
    if grade == 'done':
        break
    if float(grade) < 0.0 or float(grade) > 100:
        print("Invalid input!")
        continue
    grade_list.append(grade)
print(f"Student' grades: {grade_list}")

