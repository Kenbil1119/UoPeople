# Import date 
from datetime import datetime

date = datetime.today()

# Define Class attributes
class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = datetime.strptime(due_date, "%Y-%m-%d")

        if date.date() >= self.due_date.date():
            self.status = "Completed"
        else:
            self.status = "Pending"

    def settask(self):
        if self.status == "Pending":
            print(f"The task for '{self.name}' has been set to '{self.due_date.date()}' successfull! And is still '{self.status}'")
        else:
            print(f"The task for '{self.name}' has been marked '{self.status}' on '{self.due_date.date()}'")

# Creating multiple task using the Task class
Assignment = Task("Assignment Submission", "2026-10-29")
Assignment.settask()
print("- - - - - - - \n")

Registration = Task("Next Term Registration", "2026-10-21")
Registration.settask()
print("- - - - - - - \n")

Payment = Task("Course Payment", "2026-11-01")
Payment.settask()
print("- - - - - - - -\n")

Practice = Task("Python Practice", "2026-10-27")
Practice.settask()
