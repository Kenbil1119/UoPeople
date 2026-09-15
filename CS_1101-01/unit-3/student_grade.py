grade_list = []
grade = ''
print("Enter student grade (digits ONLY!) or type 'done' if no more grades to enter")
print("------------------")
while True:
    grade = input("Student grade: ")
    if grade == 'done':
        break
    if int(grade) < 0:
        continue
    grade_list.append(grade)
print(f"Student' grades: {grade_list}")

