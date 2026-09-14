password = "password"
chance = 3
try_again = {
        '1': True,
        '2': False
        }
print("\tWelcome back Usman, to your Fit space!")
# Ask user for login details
while chance:
    enter_password = input("Enter Password: ")
    if enter_password == password:
        print("Login Successful")
        break
    elif chance ==  2:
        print("This is your last chance, else a link will be sent to your backup email: us****de@gmail.com")
    else:
        print("\tIncorrect Password")
    chance -= 1
