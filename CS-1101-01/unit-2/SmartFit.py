# Ask user to enter age
age = int(input("Please enter your age (number only!): "))
# Check eligibility of age
if age < 18:
    print("You are eligible for the Teen Fitness Program\n")
elif age >= 18 and age <= 40:
    print("You are eligible for the Regular Fitness Program\n")
else:
    print("You are eligible for the Senior Wellness Program\n")

# Ask about user medical condition if age is 40 or above
if age >= 40:
    reply = input("Do you have any medical conditions?\nReply with 'yes' or 'no': ")
    if reply == 'yes' or reply == 'Yes':
        print("Medical clearance required before joining.\n")
        exit()
    elif reply == 'no' or reply == 'No':
        print("You can proceed with registration\n")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
# Proceed if age is below 40
else:
    print("You can proceed with registration\n")

'''
Ask the user to choose a membership type.
If the user selects Basic, ask if they want personal training (yes/no):
If yes, print: "Basic plan with personal training: $45 per month."
If no, print: "Basic plan: $30 per month."
If the user selects Premium, print: "Premium plan: $60 per month."
'''

# Membership Type

plan = {
        '1': "Basic",
        '2': "Premium"
        }

print(f"SmartFit offers two membership types:\n1. {plan['1']}\n2. {plan['2']}")

loop = 1    # To iterate reply on wrong input
while loop:
    reply = input("Choose a Plan ('1' or '2'): ")
    if reply == '1' or reply == '2':
        break
    else:
        print("\tInvalid respond!\nReply with: '1' or '2'\n")
        print(f"1. {plan['1']}\n2. {plan['2']}")

if plan[reply] == 'Basic':
    while loop:
        reply = input("Do you want a personal training? (yes/no): ")
        if reply == 'yes' or reply == 'Yes':
            print("Basic Plan with Personal Training: $45 per month.")
            loop = 0
        elif reply == 'no' or reply == 'No':
            print("Basic Plan: $30 per month")
            loop = 0
        else:
            print("Reply with 'yes' or 'no'")
            loop = 1
else:
    print("Premium Plan: $60 per month")
