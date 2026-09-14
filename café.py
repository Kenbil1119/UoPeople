#!/usr/bin/env python3
print('Time to record menu items')
print("Please, press 'ENTER' Key after you have complete inputting a field")

respond = (input("\nAre you ready to input menu items data? ('Y/N'): "))
if respond == 'Y' or respond == 'y':
    respond = 1
else:
    respond = 0

item_data = []

while respond:
    item_dict = {
            'name': input("Name of menu: "),
            'price': float(input("Price of menu: $")),
            'quantity': int(input("How many left in stock? "))
            }
    item_data.append(item_dict)

    respond = input("Do you have other items? (Y/N)")
    if respond == 'Y' or respond == 'y':
        respond = 1
    else:
        respond = 0
print(f"Menu items in stock:\n{item_data}")
