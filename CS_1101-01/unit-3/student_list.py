students = ["Alice", "Ben", "Chloe", "David"]

print("Please, enter the student name and press ENTER for another field. (Input 'done' if no other name)")
while True:
    name = input("Name: ")
    students = name
    if name == 'done' or name == 'Done':
        break

# Display students' name
print(f"Below is the names of students in the students list:")
index = 0
name = 0
for name in students:
    index += 1
    print(f"{index}. {name}")
