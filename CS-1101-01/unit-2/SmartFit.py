# Ask user to enter age
age = int(input("Please enter your age (number only!): "))
# Check eligibility of age
if age < 18:
    print("You are eligible for the Teen Fitness Program")
elif age >= 18 and age <= 40:
    print("You are eligible for the Regular Fitness Program")
else:
    print("You are eligible for the Senior Wellness Program")

# Ask about user medical condition if age is 40 or above
if age >= 40:
    reply = input("Do you have any medical conditions?\nReply with 'yes' or 'no': ")
    if reply == 'yes' or reply == 'Yes':
        print("Medical clearance required before joining.")
    elif reply == 'no' or reply == 'No':
        print("You can proceed with registration")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")
# Proceed if age is below 40
else:
    print("You can proceed with registration")
