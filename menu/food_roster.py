# Import useful libraries
import random
from datetime import datetime

days = ('SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY')
# Fetch current month from the system using datetime library
month = datetime.today().strftime('%B')

# Open menu list file
with open('menu_list.txt', 'r') as menu_list:
    menus = menu_list.readlines()
# Open quotes file
with open('food_quotes.txt', 'r') as quotes:
    quotes = quotes.readlines()
# Print the present month menu roster
print(f"{'-----===' f' {month} ' 'Menu Roster===-----':^50}")
for week in range(4):
    print(f"{' __________________':^50}")
    print(f"{'| WEEK' f' {week + 1} ' 'menu list |':^50}")
    print(f"{' ------------------':^50}")
    print(random.choice(quotes))
    for day in days:
        print(f"{day:^20}")
        for meal in ('Breakfast', 'Launch', 'Dinner'):
            print(f"{meal}: {random.choice(menus)}", end='')
        print()
