# Ask user to enter age
age = int(input("Please enter your age (number only!): "))

# Check eligibility of age
if age < 18:
    print("You are eligible for the Teen Fitness Program\n")
elif 18 <= age <= 40:
    print("You are eligible for the Regular Fitness Program\n")
else:
    print("You are eligible for the Senior Wellness Program\n")


# Ask about user medical condition if age is 40 or above
medical = False

if age >= 40:
    while True:
        medical = input("Do you have any medical conditions?(yes/no): ")

        if medical == 'yes' or medical == 'Yes':
            medical = True
            print("\nMedical clearance required before joining.\n")
            break

        elif medical == 'no' or medical == 'No':
            medical = False
            print("You can proceed with registration\n")
            break

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


# Membership Plan
Plan = {
    '1': "Basic",
    '2': "Premium"
}

plan = '0'
print(f"SmartFit offers two membership types:\n1. {Plan['1']}\n2. {Plan['2']}")

while True:
    plan = input("Choose a Plan ('1' or '2'): ")
    if plan == '1' or plan == '2':
        break
    else:
        print("\tInvalid respond!\nReply with: '1' or '2'\n")
        print(f"1. {Plan['1']}\n2. {Plan['2']}")

# Track whether Basic uers wants personal training
personal_training = False

if Plan[plan] == 'Basic':
    while True:
        reply = input("Do you want a personal training? (yes/no): ")
        if reply == 'yes' or reply == 'Yes':
            personal_training = True
            print("Basic Plan with Personal Training: $45 per month.")
            break
        elif reply == 'no' or reply == 'No':
            personal_training = False
            print("Basic Plan: $30 per month")
            break
        else:
            print("Reply with 'yes' or 'no'")
else:
    print("Premium Plan: $60 per month")


'''
If the user has Premium membership and their age is under 30, print: "You qualify for a youth discount! 10% off your plan."
If the user has Basic membership and does not want personal training, print: "Consider upgrading to Premium for more benefits!"
If the user has a medical condition and chooses Premium, print: "We recommend a free consultation before starting.”
'''

if Plan[plan] == 'Premium' and age < 30:
    print("You qualify for a youth discount! 10% off your plan.")

if Plan[plan] == 'Basic' and not personal_training:
    print("Consider upgrading to Premium for more benefits!")

if Plan[plan] == 'Premium' and medical:
    print("We recommend a free consultation before starting.")
